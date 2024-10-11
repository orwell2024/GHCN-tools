# GHCN-tools

## Overview
This repository contains tools and datasets related to the analysis of GHCN (Global Historical Climatology Network) data. The main focus is on extracting and analyzing brightness information (BI) and built-up area (BU) for climate stations, using datasets from Google Earth Engine (GEE). The repository contains multiple files, each with a specific purpose:

- **GHCNv4_stations_with_BI_BU_orwell2022.csv**: This file contains metadata and analysis results for GHCN stations, including BI and BU values.
- **Extract_BI_for_GHCN.ipynb**: A Jupyter notebook that details the process of extracting brightness information for GHCN stations.
- **GHCN_US-vs-global.ipynb**: A Jupyter notebook that compares temperature trends between US stations and global stations.

## Fields Explained
### Built-up Area (BU)
- **BU** values represent the built-up area percentage around each station, indicating urbanization levels. The data is derived from the Global Human Settlement Layer (GHSL) dataset.
- The **BU** values are available for the following years: 1975, 1990, 2000, and 2014.
- **BU Source**: [Global Human Settlement Layer (GHSL)](https://ghsl.jrc.ec.europa.eu/)

### Brightness Information (BI)
- **BI** values represent the average brightness around each station, extracted from satellite night-time lights data. This data helps in understanding the level of human activity and light pollution around the station.
- **BI** values are provided for the years 2012, 2017, 2020, and 2023.
- Additional columns calculated from **BI** values:
  - **BI_2020_lsq**: Linear least squares estimate for brightness in the year 2020.
  - **BI_trend_lsq**: Trend of brightness values calculated using a linear least squares regression.
- **BI Source**: [NOAA VIIRS Nighttime Lights](https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_DNB_MONTHLY_V1_VCMCFG)

## Parameters in `GHCNv4_stations_with_BI_BU_orwell2022.csv`
The CSV file contains the following columns:

- **ID**: Unique identifier for each station.
- **Station_Name**: Name of the station.
- **Lat**: Latitude of the station.
- **Lon**: Longitude of the station.
- **Elevation**: Elevation of the station (in meters).
- **BU_1975**, **BU_1990**, **BU_2000**, **BU_2014**: Built-up area percentage for different years.
- **BI_2012**, **BI_2017**, **BI_2020**, **BI_2023**: Brightness values for different years.
- **BI_2020_lsq**: Linear least squares estimate for brightness in 2020, calculated using all available **BI** values.
- **BI_trend_lsq**: Linear trend of brightness over the years, derived using linear regression.

## GEE Data Sources
- **Built-up Area (BU)**: The **BU** values are extracted from the [Global Human Settlement Layer (GHSL)](https://ghsl.jrc.ec.europa.eu/), available in GEE.
- **Brightness Information (BI)**: The **BI** values are extracted from the [NOAA VIIRS Nighttime Lights dataset](https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_DNB_MONTHLY_V1_VCMCFG), available in GEE.

## `GHCN_US-vs-global.ipynb` Notebook
This notebook provides a comparative analysis of temperature trends between US stations and global stations, using GHCN data. It includes visualizations and statistical comparisons to understand how temperature trends differ regionally and globally.

## How to Use
- To analyze brightness or built-up area data, use the `Extract_BI_for_GHCN.ipynb` notebook, which provides step-by-step instructions on extracting and processing the data.
- The CSV file `GHCNv4_stations_with_BI_BU_orwell2022.csv` can be used directly for statistical analysis or visualization in any tool of choice, such as Python (Pandas), R, or Excel.

