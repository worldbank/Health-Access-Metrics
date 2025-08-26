### 4. Notebooks summary

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
