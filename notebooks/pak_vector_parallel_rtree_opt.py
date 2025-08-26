#################### ============================================================ ################################
## IMPORT PACKAGES AND LIBRARIES

# System
import sys
import os
from os.path import join, expanduser
from pathlib import Path
# Avoid warnings to pop up
import warnings
warnings.filterwarnings('ignore')
# Visualization tools
# import folium as flm
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.gridspec as gridspec
from rasterio.plot import plotting_extent
from rasterio.plot import show
from mpl_toolkits.axes_grid1 import make_axes_locatable
import contextily as ctx
import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import seaborn as sns
# Processing 
import numpy as np
import geopandas as gpd
import pandas as pd
from gadm import GADMDownloader

# Raster
import rasterio as rio
from rasterio.features import shapes
from shapely.geometry import box
from rasterio.features import geometry_mask
from rasterstats import zonal_stats
from shapely.geometry import Polygon, box, Point
from shapely.geometry import mapping
import skimage.graph as graph
from scipy.signal import convolve2d

# Graph
import pickle
import networkx as nx
import osmnx as ox

# for facebook data
# from pyquadkey2 import quadkey
# Parallelization
import multiprocessing
import dask
import dask_geopandas as dask_gpd
import rioxarray as rioxr
# Define your path to the Repositories

sys.path.append(join(expanduser("/home/jupyter-wb618081"), 'Repos', 'gostrocks', 'src'))
sys.path.append(join(expanduser("/home/jupyter-wb618081"), 'Repos', 'GOSTNets_Raster', 'src'))
sys.path.append(join(expanduser("/home/jupyter-wb618081"), 'Repos', 'GOSTnets'))
sys.path.append(join(expanduser("/home/jupyter-wb618081"), 'Repos', 'GOST_Urban', 'src', 'GOST_Urban'))
sys.path.append(join(expanduser("/home/jupyter-wb618081"), 'Repos', 'health-equity-diagnostics', 'src', 'modules'))
sys.path.append(join(expanduser("/home/jupyter-wb618081"), 'Repos', 'INFRA_SAP'))

import GOSTnets as gn
from GOSTnets.load_osm import *
import GOSTRocks.rasterMisc as rMisc
from GOSTRocks.misc import get_utm
import GOSTNetsRaster.market_access as ma
import UrbanRaster as urban

from infrasap import aggregator
from infrasap import osm_extractor as osm   

from utils import download_osm_shapefiles

#################### ============================================================ ################################
## IMPORT DATA

data_dir = join(expanduser("/home/jupyter-wb618081"), 'data')
scratch_dir = join(expanduser("/home/jupyter-wb618081"), 'Health-Access-Metrics')
out_path = join(expanduser("/home/jupyter-wb618081"), 'Health-Access-Metrics', 'Output')

epsg = "EPSG:4326"
epsg_utm = "EPSG:32736"
iso = 'PAK'

## Import FLOOD
# Import multiple rasterio .tif file as a dictionary
# Keys are return periods
# Values are rasterio arrays

# inland waters and oceans: 999
# not-flooded areas: -999 (Fluvial)
# not-flooded areas: 0 (Pluvial)
# Other values represent the flood depth (in m)

flood_fluvial_path = join(data_dir, iso,'FLOOD_SSBN','fluvial_undefended')
flood_pluvial_path = join(data_dir, iso,'FLOOD_SSBN','pluvial')

files=os.listdir(flood_fluvial_path)
flood_dict_fluvial = {}
for file in files:
    key = file.split('_')[1].split('.')[0]
    value = rio.open(join(flood_fluvial_path,file)) #.read(1)
    flood_dict_fluvial[key] = value

files=os.listdir(flood_pluvial_path)
flood_dict_pluvial = {}
for file in files:
    key = file.split('_')[1].split('.')[0]
    value = rio.open(join(flood_pluvial_path,file)) #.read(1)
    flood_dict_pluvial[key] = value

# Preserve the maximum flood depth
flood_dict = {}
for f,key in enumerate(flood_dict_pluvial.keys()):
    out_flood_path = join(data_dir, iso,'FLOOD_SSBN', 'Fmax_' + key +'.tif')
    if os.path.isfile(out_flood_path):
        value = rioxr.open_rasterio(out_flood_path, chunks = 1000)
        # value = rio.open(out_flood_path)
        flood_dict[key] = value
    else:
        out_meta = flood_dict_pluvial[key].meta
        flood_max = np.fmax(flood_dict_fluvial[key].read(1),flood_dict_pluvial[key].read(1))
        flood_dict[key] = flood_max
        # flood_dict[key][flood_dict[key] == 0] = -999
        # Write the output raster
        out_flood_path = join(data_dir, iso,'FLOOD_SSBN', 'Fmax_' + key +'.tif')
        with rio.open(out_flood_path, 'w', **out_meta) as dst:
            dst.write(flood_max, 1)
        # Read the output raster
            # rioxarray
        # value = rioxr.open_rasterio(out_flood_path, chunks = 100)
            # rasterio
        value = rio.open(out_flood_path)
        flood_dict[key] = value

# Free up memory
for f,key in enumerate(flood_dict.keys()):
        del flood_dict_fluvial[key]
        del flood_dict_pluvial[key]

flood_dict[key]

## Import ROADS
# Load the Road network
roads = dask_gpd.read_file(join(data_dir, iso, "pakistan-latest-free.shp", 'gis_osm_roads_free_1.shp'), npartitions = 8)
roads = roads.to_crs(epsg)

def get_num(x):
    try:
        return(int(x))
    except:
        return(5)
# roads.rename(columns = {"fclass":"OSMLR_num"}, inplace = True)
roads['OSMLR_num'] = roads['fclass'].apply(lambda x: get_num(str(x)[-1]))
# Floods can impact all the roads, except the bridges in primary and secondary roads
safe = ((roads['bridge'] == "T") & ((roads['OSMLR_num'] == 1) | (roads['OSMLR_num'] == 2)))
roads_safe = roads[safe][["osm_id", "fclass","bridge","geometry","OSMLR_num"]]
roads_flood = roads[~safe][["osm_id", "fclass","bridge","geometry","OSMLR_num"]]
roads_safe = roads_safe.compute()
roads_flood = roads_flood.compute()

#################### ============================================================ ################################
## PARALLEL COMPUTATION OF ROADS/FLOOD DISRUPTION

import psutil
import multiprocessing

def raster_to_vect(mask, transform):
    polygons = []
    for index, value in np.ndenumerate(mask):
        row, col = index
        if value:
            top_left_x, top_left_y = transform * (col, row)
            bottom_right_x, bottom_right_y = transform * (col + 1, row + 1)
            polygon = box(top_left_x, bottom_right_y, bottom_right_x, top_left_y)
            polygons.append(polygon)
    return polygons

# Function to perform intersection
def rtree_intersect(roads_flood_gdf, flood_gdf):
    intersection_gdf = gpd.GeoDataFrame(columns=roads_flood.columns, crs=roads_flood.crs)
    flood_gdf = flood_gdf.unary_union
    flood_gdf = ox.utils_geo._quadrat_cut_geometry(flood_gdf, 0.5)
    for poly in flood_gdf.geoms:
        spatial_index = roads_flood_gdf.sindex
        possible_matches_index = list(spatial_index.intersection(poly.bounds))
        possible_matches = roads_flood_gdf.iloc[possible_matches_index]
        precise_matches = possible_matches[possible_matches.intersects(poly)]
        intersection_gdf = gpd.GeoDataFrame(pd.concat([intersection_gdf, precise_matches], ignore_index=True), crs=roads_flood.crs)
    intersection_gdf.drop_duplicates(subset="osm_id", inplace=True)
    return intersection_gdf

# Function to perform parallel intersections
def parallel_intersects(roads_flood_gdf, flood_gdf, chunk_size):
    chunks = []
    rows, _ = flood_gdf.shape
    for r in range(0, rows, chunk_size):
        chunk_flood_poly = flood_gdf.iloc[r:r+chunk_size]
        chunks.append(chunk_flood_poly)
    with multiprocessing.Pool() as pool:
        results = pool.starmap(rtree_intersect, zip([roads_flood_gdf]*len(chunks), chunks))
    matches = gpd.GeoDataFrame(pd.concat(results, ignore_index=False), crs=roads_flood_gdf.crs)
    matches.crs = epsg
    return matches

# Main code
if __name__ == "__main__":
    cpun = multiprocessing.cpu_count()
    print("Number of CPU:", cpun)
    cpu_percent = psutil.cpu_percent()
    print("CPU Usage:", cpu_percent)

    memory_info = psutil.virtual_memory()
    print("Memory Total: GB", memory_info.total/(10**9))
    print("Memory Used: GB", memory_info.used/(10**9))
    print("Memory Free: GB", memory_info.free/(10**9))

    for scen in list(flood_dict.keys()):
        
        start_time = time.time()
        print("VECTORIZATION started...")
        ## VECTORIZATION CODE
        # Rioxarray (chunks = 1000)
        flood_road = flood_dict[scen].copy()
        # If water level is more than 20 cm, the road is disrupted       
        transf = flood_road.rio.transform()
        mask = (flood_road >= 0.2).isel(band = 0)
        # Vectorize the masked cells
        flood_poly = raster_to_vect(mask, transf)
        flood_poly_gdf = gpd.GeoDataFrame(geometry=flood_poly, crs=epsg)  # Make sure to set the correct CRS
        end_time = time.time()
        duration = end_time - start_time
        print("VECTORIZATION Duration:", duration/60, "minutes")

        start_time = time.time()
        print("INTERSECTION started...")
        ## INTERSECTION CODE
        matches = parallel_intersects(roads_flood, flood_poly_gdf, chunk_size=100000) #, chunk_size=75000
        end_time = time.time()
        duration = end_time - start_time
        print("INTERSECTION Duration:", duration/60, "minutes")

        print("SAVING Roads disrupted", scen)
        # Save results
        file = join(out_path,iso,"roads_impact_"+scen+"_new.shp")
        roads_flood_impact = roads_flood.drop(matches.index)
        roads_flood_impact = pd.concat([roads_flood_impact, roads_safe], axis = 0)
        matches.to_file(file, index = False)
    
        # Free up memory
        del flood_road
        del flood_poly
        del flood_poly_gdf
        del matches
        del roads_flood_impact
    
