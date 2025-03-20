# GHCN-tools

## Overview

This repository contains tools and datasets related to the analysis of GHCN (Global Historical Climatology Network) data. The main focus is on extracting and analyzing brightness information (BI) and built-up area (BU) for climate stations, using datasets from Google Earth Engine (GEE). The repository contains multiple files, each with a specific purpose:

- **GHCNv4\_stations\_with\_BI\_BU\_orwell2022.csv**: This file contains metadata and analysis results for GHCN stations, including BI and BU values.
- **Extract\_BI\_for\_GHCN.ipynb**: A Jupyter notebook that details the process of extracting brightness information for GHCN stations.
- **GHCN\_US-vs-global.ipynb**: A Jupyter notebook that compares temperature trends between US stations and global stations.
- **Plot_T_anomalies_GHCN.ipynb**: A Jupyter notebook that compares temperature trends with various filter and binning options (BU...)

## Fields Explained

### Built-up Area (BU)

- **BU** values represent the built-up area percentage around each station, indicating urbanization levels. The data is derived from the Global Human Settlement Layer (GHSL) dataset.
- The **BU** values are available for the following years: 1975, 2020.
- **BU Source**: [Global Human Settlement Layer (GHSL)](https://ghsl.jrc.ec.europa.eu/)

### Brightness Information (BI)

- **BI** values represent the average brightness around each station, extracted from satellite night-time lights data. This data helps in understanding the level of human activity and light pollution around the station.
- Note: The **BI** values from older versions (like NASA-GISS) set all BI < 5 to 0, which might result in skewed data representation. The current **BI** values have been updated for accuracy.
- **BI** values are provided for the years 2012, 2017, 2020, and 2023.
- Additional columns calculated from **BI** values:
  - **BI\_2020\_lsq**: Linear least squares estimate for brightness in the year 2020.
  - **BI\_trend\_lsq**: Trend of brightness values calculated using a linear least squares regression.This data helps in understanding the level of human activity and light pollution around the station.
- **BI** values are provided for the years 2012, 2017, 2020, and 2023.
- Additional columns calculated from **BI** values:
  - **BI\_2020\_lsq**: Linear least squares estimate for brightness in the year 2020.
  - **BI\_trend\_lsq**: Trend of brightness values calculated using a linear least squares regression.
- **BI Source**: [NOAA VIIRS Nighttime Lights](https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_DNB_MONTHLY_V1_VCMCFG)

## Parameters in `GHCNv4_stations_with_BI_BU_orwell2022.csv`

The CSV file contains the following columns:

- **ID**: Unique identifier for each station.
- **Station**: Name of the station.
- **USCRN\_Y\_N**: Indicates if the station is part of the US Climate Reference Network (Yes/No).
- **Lat**: Latitude of the station.
- **Lon**: Longitude of the station.
- **Elev-m**: Elevation of the station (in meters).
- **BI**: Outdated brightness information from NASA-GISS (with values < 5 set to 0 by NASA obviously).
- **Built\_1975\_50km\_percent**, **Built\_2020\_50km\_percent**: Built-up area percentage at a 50km radius for the years 1975 and 2020.
- **Percentage\_Change\_50km**: Percentage change in built-up area at a 50km radius from 1975 to 2020.
- **Built\_1975\_10km\_percent**, **Built\_2020\_10km\_percent**: Built-up area percentage at a 10km radius for the years 1975 and 2020.
- **Percentage\_Change\_10km**: Percentage change in built-up area at a 10km radius from 1975 to 2020.
- **Built\_1975\_2km\_percent**, **Built\_2020\_2km\_percent**: Built-up area percentage at a 2km radius for the years 1975 and 2020.
- **Percentage\_Change\_2km**: Percentage change in built-up area at a 2km radius from 1975 to 2020.
- **USCRN\_Station**: Whether the station is part of the US Climate Reference Network.
- **BI\_2012**, **BI\_2017**, **BI\_2020**, **BI\_2023**: Brightness values for different years.
- **BI\_change\_decade**: Decadal change in brightness values from 2012 to 2023.
- **BI\_2020\_lsq**: Linear least squares estimate for brightness in 2020, calculated using all available **BI** values.
- **BI\_trend\_lsq**: Linear trend of brightness over the years, derived using linear regression.

## GEE Data Sources

- **Built-up Area (BU)**: The **BU** values are extracted from the [Global Human Settlement Layer (GHSL)](https://ghsl.jrc.ec.europa.eu/), available in GEE.
- **Brightness Information (BI)**: The **BI** values are extracted from the [NOAA VIIRS Nighttime Lights dataset](https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_DNB_MONTHLY_V1_VCMCFG), available in GEE. A 1km radius was used for brigness averaging.

## `GHCN_US-vs-global.ipynb` Notebook

This notebook provides a comparative analysis of temperature trends between US stations and global stations, using GHCN data. It includes visualizations and statistical comparisons to understand how temperature trends differ regionally and globally.

## How to Use

- To analyze brightness or built-up area data, use the `Extract_BI_for_GHCN.ipynb` notebook, which provides step-by-step instructions on extracting and processing the data.
- The CSV file `GHCNv4_stations_with_BI_BU_orwell2022.csv` can be used directly for statistical analysis or visualization in any tool of choice, such as Python (Pandas), R, or Excel.
- Use the file as meta data file for the GHCNv4 T file by NASA-GISS. Merge by station ID

## Some pictures and examples

  ![image](https://github.com/user-attachments/assets/2fdc64d5-44b3-4502-9f79-af54e719df4e)


![image](https://github.com/user-attachments/assets/af7c7161-b6cb-47e1-8089-15880c2d51da)

### Ineractive map showing all stations which deviate being BI = 0-0.1 both in old (NASA) and new (orwell2022) BI analysis.

![image](https://github.com/user-attachments/assets/8fb2989a-d58f-4725-bec6-c5722284351a)

### Mapping Brightness and Built-Up Indexes Across the Globe
In this analysis, we explore how NASA's Brightness Index (BI) compares to actual built-up areas around meteorological stations. Using data from NASA's GHCNv4 and VIIRS/NOAA, we mapped stations with minimal urbanization (BU_10km ≤ 1%).
Colors Explained:
Purple: Stations with a NASA flagged BI above 15.
Red: Stations with a a NASA flagged BI between 10 and 15
Blue: Stations with a a NASA flagged BI  6-10, 
Despite these classifications, all stations shown here have both BI_2020 < 1 and BU_10km < 1%, meaning they are in deep rural areas. This highlights how NASA's BI misclassifies these locations, suggesting the need for improved metrics (use of GHSL_S etc) to distinguish urban from rural areas.
Footnote:The colors are used to quickly highlight the most extreme misclassifications. All points are rural, with BU_10km < 1%.

![image](https://github.com/user-attachments/assets/052dd545-93a5-4135-a914-ab4eb83d8435)

### Correlation plot BI_2020_sqr versus BU_2km, colored by old BI values. 🔴 for BI>6.

Brightness Index (BI) is nearly a random number generator, failing to rigorously separate Rural 🔴 from Urban ⚫️ stations ("R", "U" mark the ensemble's weight centers). This is why no difference appears in the temperature curves either. Proper GHSL data should be used.

![image](https://github.com/user-attachments/assets/61b10884-cd20-4610-9f31-f707005e7458)

## Trend lines (added feature on Nov 6th 2024, due to US Election Boredout Syndrome)

Motivation - to compare with Java. E.g. here

![image](https://github.com/user-attachments/assets/7731940b-ebba-47d8-93e6-5c592a80aeba)

### What can you do with this? 

Extract trend slopes for various BU bins with a flexible start point.

![image](https://github.com/user-attachments/assets/2fa73016-5afd-4852-bc91-91c1f4c2fdbc)

The analysis on the right is done ad-hoc (just feed GPT with the trend values and do the plot). It depends on the experiment perfromed. 

![image](https://github.com/user-attachments/assets/df9b5052-9548-4a63-bb72-a44e5b65459c)

### Note on the output file 'GHCNv4_stations_with_BI_BU_orwell2022.csv'
https://github.com/orwell2024/GHCN-tools/blob/main/GHCNv4_stations_with_BI_BU_orwell2022.csv
The image provides a global map of GISS GHCN stations, comparing them against the GHSL built-up land data retrieval process.

Gray dots represent all existing stations in the dataset.
Red dots highlight 386 stations missing from the fetched GHSL dataset, meaning built-up data could not be retrieved for these locations.
The missing stations are primarily located in polar regions (e.g., above ~70°N and Antarctica), suggesting a limitation in GHSL data coverage for extreme latitudes.
This issue could be due to:
GHSL dataset gaps where satellite-derived built-up data is unavailable in remote locations.

Gray dots: Existing stations.
Red dots: Stations missing from the fetched GHSL dataset.
Total stations in fetched dataset: 27,519.
Stations missing from the fetched GHSL list: 386.
![image](https://github.com/user-attachments/assets/32f8accc-c7c3-4734-9b11-fb0f1a042794)


