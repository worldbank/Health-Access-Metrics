# Physical Disruption of Healthcare Accessibility
Three emergencies dimensions for accessibility disruption are considered here.\
The first and one of the most widely considered concerns the role of floods, and is explored in depth in the following examples and analytics.\
The second situation mimics the diffusion of a pandemics (e.g. COVID-19), which more or less randomly disrupts the health facilities by fully occupying their hosting capacity.
The third dimension is conflicts, and the role they have in destroying/damaging the facilities, as well as the potential threatening they have on population, thus preventing their movement to HF in case needed.

## Floods disruption
Floods are a complex phenomenon, but it is possible to broadly classify this events as occuring either as a consequence of eccess in upstream precipitation, leading to fluvial hazards, or sustained in-loco precipitaion, leading to pluvial hazards, or a combination of the two (cite). Additionally, climate change is known to modify the spatial and temporal occurrence of precipitation extremes, which can be technically described in terms of Return Periods (RP), the likelihood of occurrence of an event according to their statistical distribution over time in a location. The RP represents the average time interval between two events of the same magnitude: the higher the RP, the higher the magnitude of the event. Climate change is, generally speaking, increasing the frequency of extreme events, thus making what decades ago was defined as uncommon relatively common (decreases the RP). 
Flood disruption emergency is therefore simulated for designated countries as being both of pluvial and fluvial origin, providing a worst-case scenario, for several RP. 

## Pandemics disruption
Pandemics are emergency events which are extremely difficult to forecast. However, health emergency plans are generally promoted in order to face their potential occurrence. Given the recent outbrakes of Ebola and most prominently COVID-19, and that those emergencies are likely to occur in the future as a consequence of environmental degradation and increased human-wildlife interactions, it could be theoretically possible to increase the preparedness of healthcare systems to these emergencies. To do so, a randomized procedure can be used to select healthcare facilities impacted as those that need to fully convert their activities to the treatment of patients, therefore making their access to common patients unfeasible. However, to properly model this situations, number of beds in hospitals and clinics has to be accounted for, but it currently not avaibale for the countries participating to the HEPR Program. This analysis is therefore not performed and not presented in this book.          

## Conflicts disruption
Wars and conflicts are events that disrupt the accessibility to healthcare facilities mainly in two ways. First, by destrying or severely damaging the healthcare facilities (clinics, hospitals) and the physical infrastructures (roads). Second, by discouraging or completely blocking the possibility for people to access healthcare, as a consequence of army presence in the streets, checkpoints, or rather explosions or firefights. However, given the complexity of the phenomenon analyzed, not all the conflicts are similar, and their effects may widely vary depending on the location occurrence. Whether it is possible to model the physically accessibility disruption to conflicts as a consequence of the destruction of healthcare facilities, it is rather complex to do so otherwise (e.g. without the occurrence of bombing or firefights). An attempt is presented in this book, stemming from the work of XXX, representing the case of actual Myanmar civil war.

### How to quantify disruption
It is possible to consider disruption to physically accessibility by laveraging two methodologies:

1. **Travel-time weighting** It is valid for raster-based measures of accessibility, and it consists of weighting the travel time of the raster travel surface by a defined amount, thus increasing the time needed to reach a HF location. 
2. **Roads impact** This method allows to use vector-based layers for the estimation of the accessibility (e.g. roads), and consists in disrupting the roads network according to defined criteria.
3. **HF impact** This is the simplest case when a healthcare facility is directly impacted by an event. The consequence is that population in its proximities has to physically reach a further HF.

**Inserire qualche immagine e spiegazione della disruption** 
