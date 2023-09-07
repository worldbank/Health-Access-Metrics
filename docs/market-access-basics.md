# Physical Accessibility to Health Care Measurement (PAHM)
Once again, the goal of this work is to provide tools, frameworks and best practices for measuring physical access to health care. In particular, our work focuses on access to health care in the context of health emergencies. 
## Physical Accessibility Basics
Physical accessibility to healhcare can be looked at as the relationship between the location of supply (health services) and the location of clients, taking into account clients' transportation resource and travel time, distance and cost. This is also referred to as *market access analysis* in GIS. 

### How to quantify access to healthcare
In most GIS systems, the outputs of accessibility measurement is often a quantiy such as distance and/or travel time. However, there are several ways to arrive at distance and/or travel time. For example,see below:

1. **The Euclidean Distance (ED)** This is the simplest method which provides straight-line distance between two points on a plane or  distance "as the crow flies,".
2. **Travel time**. This considered more comprehensive because it takes into account available infrastracture (e.g., roads) from the clients/population to the health services.

###  Required datasets for physcal access measurement
In order to do any PAHM analysis, the following datasets are required

```{table}
:name: foundational_datasets

| **Dataset** | **Description**                            | **Required Attributes**      | **Other Attributes** |  **Required**| **Example** |                                                                                                                                                                                         
|:------------|:-------------------------------------------|------------------------------|----------------------|--------------|:-------------|
|Health facilities| This represents the supply-location of health infrastracture | Location (e.g., lat, lon)|Type of health facility (e.g, referral, primary etc), number of beds| Yes| [Malawi health facilities data](https://data.humdata.org/dataset/hotosm_mwi_health_facilities?force_layout=desktop)|
|Population|This represents the clients/demand|Location (e.g., gridded population)|Time (e.g., census year)| Yes|[World Pop, Malawi pop](https://hub.worldpop.org/geodata/summary?id=49647)|
|Travel Friction Surface|Raster layer with modelled travel time using road network and other layers|N/A|N/A|No|[Malaria Project 2019 friction surface](https://developers.google.com/earth-engine/datasets/catalog/Oxford_MAP_friction_surface_2019)|
|Road network|Road infrastructure required to travel|Location (e.g., gridded population)|Time (e.g., census year)| Yes|[World Pop, Malawi pop](https://hub.worldpop.org/geodata/summary?id=49647)|


```


## Existing Tools for (PAHM)
Lets look at some of the existing tools for measuring physical accessibility. We do this by looking at World Bank Group internal tools separately from external tools.

### Internal Tools and Packages
These are packages and toolkits developed within the WBG.
##### GOSTnets
[GOSTnets](https://github.com/worldbank/GOSTnets) is a Python package developed by the GOST team. Its main capabilities is to provide functionality to Build, process, and analyze networks.Thus, this package can be used to calculate travel times and threfore measure physical accessibility.

##### GOSTnets_Raster
[GOSTnets_Raster](https://github.com/worldbank/GOSTnets) is also a Python package developed by the GOST team. Unlike GOSTnets which performs the network analysis using vector input datasets, GOSTnets_Raster focuses on utilizing raster based measures such as [Friction Surface](https://developers.google.com/earth-engine/datasets/catalog/Oxford_MAP_friction_surface_2019) developed by the Malaria Atlas project. 

### External Tools and Packages
### Desktop GIS Software
At the heart of physical accessibility measurement is the calculation of distances and travel time using available datasets. As such, given the right input datasets and GIS skills, one could potentially use any desktop GIS software to generate these type of metrics as well as conduct detailed market access analysis. We cannot provide an exhaustive list of GIS
### WHO AccessMod
The WHO has GIS plug-in called [AccessMod](https://www.who.int/tools/accessmod-geographic-access-to-health-care), the download page is [here](https://www.accessmod.org/). Its packaged as a stand-alone open source application that can run on different platforms (Windows, Linux, Mac) through the use of a virtual machine (VirtualBox) and allows the use of geospatial data created by different GIS software (ArcGIS, QGIS, GRASS,...). 

AccessMod is a free toolbox that has been developed by WHO in order to assist countries to examine the geographic aspects of their health system. It specifically addresses the first three layers of a well-known framework developed by Tanahashi (1978) to evaluate health service coverage (the specific three layers being: the target population, availability coverage and accessibility coverage). The package enables calculation of the following:

- Assessing travel time and thereby how physically accessible existing health services are to the target population.
- Taking into account the coverage capacity of each health facility to estimate the share of the target population that could be seen with a certain quantity of inputs (i.e., health workforce, infrastructure). As a next logical step, determining whether coverage capacity is (in)sufficient to provide care to everyone living within the facility’s catchment area.
- Calculating distance and travel time between different types of health system infrastructure - Referral analysis
Estimating the percentage share of the population with coverage in each sub national division to examine inequities - Zonal statistics.
- Identifying the optimal location for building new health facilities - Scaling up scenario analysis

## Limitations and challenges of current systems
### Data related challenges
One of the major obstacle when perfoming physical accessibility analysis is related to input datasets as follows:

- **Noisy input datasets**.
- **Lack of georeferenced health facilities data.** In some cases, the available health facilities data will need to be geocoded because it lacks geographic coordinates.
- **Lack of up to date roadnetwork data.** Accuracy of travel time estimation are tied to how accurate and update is the input data including the roadnetwork. However, in most cases, we end up using OSM data which doesnt have authoritative completeness or coverage details. Even when roadnetwork data is provided by local authorities in the country, it may also lack information on how up to date the data is.

### Tools Based Challenges
As mentioned earlier on, the process of generating physical accessibility metrics such as travel time can be done in commion standard desktop GIS software such as ArcGIS. Athough this process will be fairly easy in a high end software such as ArcGIS, we know that ArcGIS is very expensive and therefore not accessible to most users. The next option is to use opensource deskop GIS software such as QGIS. However, the challnge with QGIS is that the process of perfoming a market analysis is rather difficult and requires advanced GIS skills.

### Documentation and standards challenges

### Lack of season and scenario sensitive metrics


## Why another tool
## PAM-Kit Design Philosophy

