# Cefas Plume Mapping Training (OCPP)
This repository was developed under Ocean Country Partnership Programme (OCPP) to provide training on how to use Sentinel-3 OLCI to map river plumes.
The repository contains multiple scripts, which are described below:

### 1. [Eumetsat_Download_General.ipynb](https://github.com/CefasRepRes/Cefas_Plume_Mapping_Training/blob/main/Eumetsat_Download_General.ipynb)
This script is a Jupyter Notebook that uses EUMETSAT API through eumdac library to query and download Sentinel-3 data. It can be used to download other
EUMETSAT products as well.

### 2. [eumetsat_AOI_download.py](https://github.com/CefasRepRes/Cefas_Plume_Mapping_Training/blob/main/eumetsat_AOI_download.py)
This script is a Python version of the above Jupyter Notebook and could be used in an automated method to download the product, for which you already know the
product ID. The script runs in conjunction with the [data store login script](https://github.com/CefasRepRes/Cefas_Plume_Mapping_Training/blob/main/data_store_login_details.csv), where users have to insert their consumer key and consumer secret in order to login into the EUMETSAT portal.

### 3. [fuClassifcation_SNAP.py](https://github.com/CefasRepRes/Cefas_Plume_Mapping_Training/blob/main/fuClassifcation_SNAP.py)
This script creates a command line string which uses the GPT JAVA functions that are automatically installed with the SNAP installation. The Python script calls the [fuGraph_nc.xml](https://github.com/CefasRepRes/Cefas_Plume_Mapping_Training/blob/main/fuGraph_nc.xml) that contains the specific SNAP GPT functions, namely subsetting geogrpahically,
calculating the Forel-Ule classes and exporting Forel-Ule, Latitute and Longitude as georeferenced netCDF file.

### 4. [FUME repository](https://github.com/jobel-openscience/FUME)

This repository contains Python open-source version of the SNAP FU Classification algorithm. We would recommend looking at the tutorials, where Polymer atmospheric correction
is compared to the baseline EUMETSAT atmospheric correctionn. The advantage of using Polymer is a higher resolution of Forel-Ule valies in estuaries and nearshore areas. These scripts could be used as an alternative to the SNAP FU Classification tool.

https://github.com/jobel-openscience/FUME/blob/master/fume.py

https://github.com/jobel-openscience/FUME/blob/master/forel_ule_OLCI.ipynb

https://github.com/jobel-openscience/FUME/blob/master/forel_ule_tutorial.ipynb

According to various studies such as, [citclops](http://www.citclops.eu/home) or the [GBR studies](https://pubmed.ncbi.nlm.nih.gov/31352278/), Forel-Ule value of greater or equalt to 10 is used as cut-off point for mapping the river plume. Having said that, this might change in your local area of interest, and therefore it is recommended to analyse Forel-Ule in conjuction with the water quality parameters, such as nutrients, turbidity, suspended particulate matter or chlorophyll.


### Authors:
1. Lenka Fronkova
2. Tiago Silva
3. Richard Harrod
