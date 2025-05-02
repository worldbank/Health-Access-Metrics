# Physical Accessibility to Health Measurement

This project is being funded by the [Health Emergencies Preparedness and Response Program(HEPR)](https://www.healthemergencies.org). The goal of this project is to provide documentation to enable measurement of physical accessibility to health care across the globe. In particular, this repository provides tools (Python packages, sample code), frameworks and guidelines and best practices for measuring physical access to health care.


The <span style="color:#3EACAD">project </span> has three key components as follows:

1. **Physical accessiblity measurment toolkit (PAM-Toolkit)**. A Python which builds on existing Python pakages (e.g., GOSTnets) to provide functionality to generate accessibility metrics.
2. **Guidance note on data collection and preparation for physical accessibility measurement**. This provides documentation of best practices for collection, prepation and compiliation of data for accessibility analysis. 
3. **Training workshop**. A training to be conducted in 4 pilot countries where the toolkit will be tested.

1. Read the documentation about this project on the [project GitHub page]()
2. Download and use the [physical accessiblity measurment toolkit (PAM-Toolkit)]()

## User Guide

### 1. Project structure

The PAM-Toolkit is built using the Python programming language (see [Python documentation](https://docs.python.org/3/) for general info and how to get started) and is stored in a GitHub repository.
Additionally, the PAM-Toolkit analyses are presented here using [Jupyter notebooks](https://jupyter.org), interactive computational documents used for configuring and streamlining data-science workflows and sharing codes.

GitHub is a platform that enables users to develop, store, manage their code, Its versatility lies in the fact that it allows the sharing of code between users, as well as the simultaneous development of projects by working on local copies (clones) of the repository. To have access to this repository and its content, it is not necessary to have a GitHub account, unless active modifications are wanted to be made. In this case, please refer to the [GitHub documentaion](https://docs.github.com/en) about how to get started. 
The repository is organized as follows:

- **docs/**
    > This folder contains all documentation pertaining to the project such as the list of indicators, the guidance note and others.

- **data/**
    > This is a placeholder folder for data. This folder will mostly be empty as most of the data will not be shared on GitHub but is only accessible to few selected people. However, whereever data is used, proper documentation will be provided ton how to access the data.

- **src/**
    > All the Python code and others used in this repository will be kept here.

- **notebooks/**
    > This folder contains Jupyter notebooks which will provide example use cases using the toolkit.  



### 2. How to get started

To run the notebooks and start performing the analyses, the following prerequisites are needed and recommended:

- **Conda package manager**
- 
For a structured and tidy organization of the software requirements, the intallation of minicoda (Anaconda is heavier) is recommended. Conda allows to create virtual environments within which it is possible to manage packages and libraries by efficiently handling and resolving dependencies (i.e. packages that are the building blocks of other packages) in Linux, Windows and MacOS. Given that the PAM-Toolkit has been tested using a Linux platform, a Linux environment is recommended to exploit the full potential of the package (Windows users can install a Linux Subsystem following [here](https://learn.microsoft.com/en-us/windows/wsl/install)). However, 95% of the functionalities are also working on Windows platforms, therefore a Windows conda also serves its purpose: [How to install miniconda](https://www.anaconda.com/docs/getting-started/miniconda/install).
The following conda virtual environment is provided for both Linux and Windows users:
*environment.yml*
After the conda installation, create an environment from the *environment.yml* file by running on the computer [terminal](https://docs.jupyter.org/en/latest/glossary.html#term-command-line):
```
$ conda env create -f environment.yml
```
At this point, a virtual environment called *pam_tool* has been created, activate it with:
```
$ conda activate pam_tool
```
By following these two steps, it is possible to overcome the ex-novo installation of several Python libraries that are needed to perform the analyses. A complete list of those can be viewed with:
```
$ conda list
```
Please refer to the [Conda User Guide](https://docs.conda.io/projects/conda/en/stable/user-guide/index.html) for a comprehensive list of commands.

- **Jupyter IDE**
- 
Before running Jupyter Notebooks, an interface is needed. Having the *environment.yml* already installed Jupyter, the easiest way to start a Jupyter server is typing in the terminal:
```
$ jupyter notebook
```
This will open a Notebook Dashboard in your web browser, and you'll be able to navigate and open notebook files (.ipynb) in the same way as on your local machine.

- **Additional libraries**
- 
Some libraries used in this project are not available on conda, therefore it is needed to manually download them. The following have to be donwloaded from their GitHub repositories:

[*GOSTnets*](https://github.com/worldbank/GOSTnets) is a library useful for networkX analyses developed by GOST Team at The World Bank. It is used for vector-based accessibility studies, in particular harnessing OpenStreeMaps (OSM).

[*GostnetsRaster*](https://github.com/worldbank/GOSTnetsraster) is the raster-based version of the GOSTnets library, used with travel time or friction surfaces.

[*GOSTrocks*](https://github.com/worldbank/GOSTrocks) containing general useful functions and tools for working with geospatial data

[*GOSTUrban*](https://github.com/worldbank/GOSTurban) focusing on urban studies

[*INFRA_SAP*](https://github.com/worldbank/INFRA_SAP) containing miscellaneous functions 

### 3. Data requirements

All the data used in this project are open-source and publicly available.
To perform accessibility analyses and to estimate the disruption caused by floods, the following essential data are required:

```{table}
:name: essential_datasets

| **Dataset** | **Description**                            | **Required Attributes**      | **Other Attributes** |  **Format**| **Example** |                                                                                                                                                                                         
|:------------|:-------------------------------------------|------------------------------|----------------------|--------------|:-------------|
|Health facilities| This represents the supply-location of health infrastracture | Location (e.g., lat, lon)|Type of health facility (e.g, referral, primary etc), number of beds| .csv or .xlsx| [Malawi health facilities data](https://data.humdata.org/dataset/hotosm_mwi_health_facilities?force_layout=desktop)|
|Population|This represents the clients/demand|Location (e.g., gridded population)|Time (e.g., census year)| .tif, .nc|[World Pop, Malawi pop](https://hub.worldpop.org/geodata/summary?id=49647)|
|Travel Friction Surface|Raster layer with modelled travel time using road network and other layers|N/A|type of motorization (e.g., foot or car)|.tif|[Malaria Project 2019 friction surface](https://developers.google.com/earth-engine/datasets/catalog/Oxford_MAP_friction_surface_2019)|
|Road network|Road infrastructure required to travel|N/A|Road types (e.g., primary, bridges)| .osm.pbf, .shp|[OpenStreeMaps](https://download.geofabrik.de/)|
|Flood maps|Layer representing flood hazard or flooded area|Return Period (RP), Extent|Time (e.g., year), Scenario, Flood Depth|.tif, .shp, .nc|[WRI Aqueduct](https://www.wri.org/data/aqueduct-floods-hazard-maps)|
```

Let's describe in detail the dataset used:

- **Health Facilities**
Health facilities datasets come in the format of .csv (or similar) files as, in their simplest terms, the only required information needed is their geographical positioning represented by Longitude and Latitude coordinates and an identification name for the facility. Additional information regarding the type of facility (whether an hospital or a clinic), the number of beds and the specialization are somewhat facultative, despite they could increase the reliability of the assessment. These information are formatted in separate columns as shown below, with rows representing each health facility.

![HF_example](Health-Access-Metrics/docs/images/HF_example.PNG)

- **Population**
Population datasets are gridded representation of either population count (N° of people living within each grid-cell) or population density (N° of people living in the cell/pixel area). Being raster datasets, they are substantially a 2D (nlat*nlon) grid, usually formatted as GeoTiff files (.tif), but could also be stored in other grid-based formats, like NetCDF (.nc). The data represented are referring to a specific census year (e.g., 2020) and generally are built from people counts per administrative units using a top-down approach, ultimately generating a dataset of a specific resolution (e.g. 100m, 250m or 1km) and extent (global or country). In this project, [WorldPop population counts data](https://hub.worldpop.org/project/categories?id=3) are used, specifically the UN-adjusted, unconstrained ones, meaning data are generated using a machine-learning method over all land-areas and by adjusting the overall estimations with UN official population estimates (see below).   

![population_example](Health-Access-Metrics/docs/images/population_example.PNG)

- **Travel Friction surface**
One alternative to perform accessibility analysis relies on the use of raster data. Travel surfaces are raster layers representing the time required to cross a grid-cell either by foot or by means of motorized transportation, based on landscape characteristics and transportation infrastructure. This project uses the 1km resolution motorized friction surfaces developed by the Malaria Atlas Project, which are freely accessible and shared as GeoTiff files (.tif). Friction surfaces are useful as they allow for a faster, pixel-based computation of accessibility metrics compared to the usage of a road network. An example is shown below, representing the global map of travel time to cities (@weiss2018global)

![accessmap_example](Health-Access-Metrics/docs/images/accessmap_example.PNG)

- **Road Network**
Another approach for estimating accessibility parameters relies on the use of vectorized data. Therefore, a road network is needed in order to build a graph (see below an example) that connects the origin points of the map (each population grid-cell) to the destinations of their travel (in this case the health facilities). The road network is shared as either a shapefile (.shp) containing the vector geometries representing the streets, or in their native OSM data file (.osm.pbf). This project relies on the OpenStreetMap (OSM) shapefile of the road network in order to construct some specific indicators, which in Python is opened and managed with the help of the GeoPandas library. Geopandas relies on the same tabular structure of the Pandas library, handling GeoDataFrame data by storing the geographic and geometric information as a separate Geometry column, each one composed by a Shapely object.

![road_example](Health-Access-Metrics/docs/images/road_example.PNG)

- **Flood Maps** 
Flood maps are needed in order to model the disruption caused by flood events on either the travel friction surface or on the road network, consequently impacting the health infrastructures accessibility. For this purpose there could be used either hazard maps, representing the area impacted in the event of a flood of a specific statistical occurrence probability or climate scenario, or a flood extent map of a real event, as those produced during and after natural disasters. Being raster datasets, the minimal information needed in order to perfrom an accessibility analysis is their  spatial extent, usually represented as binary data (e.g., 0 and 1), representing flooded and unflooded surfaces. In the case of hazard maps, additional useful information is about the probability of occurrence expressed in Return Periods (RP), the flood depth (in meters), the type of flood (coastal, riverine of pluvial) and future climate scenario if considered in the generation of the dataset itself. Please note that [FATHOM flood hazard maps](https://www.fathom.global/product/global-flood-map/) have been used in this project as The World Bank Group has access to these data, but are not publicly available. As an alternative to FATHOM data, [WRI Aqueduct flood hazard maps](https://www.wri.org/data/aqueduct-floods-hazard-maps) are one of the most widely used open-source flood hazard maps that can be freely retrieved. 

### 4. Raster vs Vector analysis

The analysis can be performed adopting two frameworks, either a raster-based or a vector-based one.

- **Raster analysis**
Raster analysis has the advantage of working uniquely with gridded data, as also travel/friction surfaces are used apart from gridded population and flood maps. The major advantage of this analysis, after having properly scaled and adjusted the resolution of the datasets, fast numerical computations can be performed, allowing the assessment of large datasets with relatively little resource consumption. Additionally, this raster approach can be easily integrated with additional gridded data (e.g., wealth), and the complexity of the analysis is limited compared to the consideration of a vectorized road network. The drawback of this approach is that the highest precision of the analysis that could be achieved corresponds to the resolution of the travel friction dataset, usually 100m, therefore lacking a street level assessment of flood disruption. In this framework, flood disruption is considered by weighting the travel friction surface according to the flood depth value of the flood hazard map. Based on the work of [Pregnolato et. al, 2017](https://www.sciencedirect.com/science/article/pii/S1361920916308367), the motorized travel time is slowered following the flood depth disruption function shown below:

![Pregnolato et al](Health-Access-Metrics/docs/images/Pregnolato.jpg)

The application of this function is more accurate than the adoption of a simple threshold-based disruption approach.
The raster analysis allows for retrieving the following indicators:

*Population share within 2 hrs from the nearest Health Facility*
*Population share within 2 hrs from the nearest Hospital*

**Aggiungere i passaggi utilizzati di calcolo per la raster analysis**

- **Vector analysis**
Vector analysis is based on the usage of a vectorized road network to represent connectivity and assess accessibiilty compared to the travel friction surface. The biggest advantage of this approach is that it allows for a precise, street-by-street asessment of the flood impacts on the road network, and therefore permits a real-world comparison of the sensitivity of physical accessibility to extreme flood events. Considering the road network permits to investigate not only flood impacts on countries, but also within cities impacts, supporting the identification of most important escape routes and sensitive streets to flood events. This precision, however, comes at the cost of high time requirements for performing the analysis, especially if large areas are considered.
Using the vectorized road network, flood disruption is considered by applying a simple treshold-based approach, where 20 cm are necessary for disrupting the road accessibility (excluding bridges). 
The vector analysis allows for retrieving the following indicators:

*Health Facilities share with direct access (<100m) to an all season road*
*Health Facilities share within 2km from an all season road*

**Aggiungere i passaggi dei calcoli utilizzati per la vector analysis**


### 6. Notebooks summary

The jupyter notebooks are use cases where the deployment of the PAM-Toolkit is tested with different countires and configurations.
Both Malawi (MWI) and Pakistan (PAK) are tested as country use cases for both the raster and vector-based accessibility disruption analysis.
For Pakistan, conventional vector analysis is extremely slow due to the dimension of the country and of the road network dataset. Consequently, a parallel computing code has been developed for calculating the disrupted road network, and must be deployed as a stand-alone python code, given that multiprocessing libraries are not working on jupyter notebooks. The 

- **Flood disruption (raster) - Country assessment**
1. Function and libraries import
2. Dataset import and preprocessing
3. Flood impact of Health Facilities
4. Flood impact on friction surface
5. Travel time computation
6. Mapping accessibility to HF per flood scenario and ADM unit
7. Mapping accessibility to HF disaggregated per wealth quintile
 
- **Flood disruption (vector) - Country assessment**
1. Function and libraries import
2. Dataset import and preprocessing
3. Flood impact of Health Facilities
4. Flood impact on road network
5. Road accessibility computation
6. Mapping accessibility to HF per flood scenario and ADM unit
7. Mapping accessibility to HF disaggregated per wealth quintile

- **Flood disruption (vector) - City assessment**
1. Function and libraries import
2. Dataset import and preprocessing
3. Flood impact of Health Facilities
4. Flood impact on road network
5. Road accessibility computation
6. Betweeness centrality computation

- **Flood disruption (vector) - parallel computing**
1. Function and libraries import
2. Dataset import and preprocessing
3. Parallelization of flood impact on road network 
Subsequent points for the mapping of the accessibility disruption are implemented as a jupyter notebook

## Contacts

Matteo Mastropierro (mmastropierro@worldbank.org) \
Dunstan Matekenya (dmatekenya@worldbankgroup.org) \
Katie L. McWilliams (kmcwilliams@worldbankgroup.org) \

## License

The <span style="color:#3EACAD">template</span> is licensed under the [**World Bank Master Community License Agreement**](LICENSE). Remember to replace the [license](LICENSE.md) if necessary. If open source, [choose an open source license](https://choosealicense.com).
