# README.md

## Forensic Audit of "Very Rural" Classifications in Wickham et al. (2013)

### Project Overview

This repository contains a forensic, methodological audit of the rural station classifications used by [Wickham et al. (2013)]([https://doi.org/10.1002/jgrd.50202](https://www.scitechnol.com/influence-urban-heating-global-temperature-land-average-using-rural-sites-identified-from-modis-classifications-vwBQ.php?article_id=588)). Their study employed outdated MODIS 500m land cover data to select 15,000 "very rural" temperature stations, claiming negligible influence from urban heat islands (UHI) on global temperature trends. With advances in geospatial analysis and AI-driven satellite technology—specifically the GHSL P2023A 10-meter multispectral dataset derived from Sentinel-2 imagery—we critically reassess these classifications.

### Original Study Under Audit

[Wickham, C., et al. (2013)]([https://doi.org/10.1002/jgrd.50202](https://www.scitechnol.com/influence-urban-heating-global-temperature-land-average-using-rural-sites-identified-from-modis-classifications-vwBQ.php?article_id=588)). *Influence of urban heating on the global temperature land average using rural sites identified from MODIS classifications*. Journal of Geophysical Research: Atmospheres, 118(5), 1890–1900.

### Context and Motivation

The Wickham et al. (2013) paper has become a frequently cited reference to downplay the effect of urbanization on temperature records. Yet upon inspection, the foundation of its argument collapses under modern scrutiny. Several critical methodological and ethical flaws render its conclusions untestable and irreproducible:

- **Study weakness exposed by ************************[Steve McIntyre (2011)](https://climateaudit.org/2011/12/20/berkeley-very-rural-data/)************************ and ************************[Connolly et al. (2014)](https://doi.org/10.6084/m9.figshare.1005090.v1)************************.**
- **Unaware of previous exposures of the Berkeley Earth malice (and the 2013 garbage paper), an independent analysis was conducted as detailed in ************************[this tweet](https://x.com/orwell2022/status/1843661171498594813)************************.**
- **Undefined classification criteria**: The term “very rural” is never quantified. No threshold, no benchmark, no methodology—only assertion.
- **No station list provided**: A basic reproducibility requirement was ignored. Without the list, verification is impossible.
- **Use of obsolete MODIS 500m data**: Each pixel covers 250,000 m²—orders of magnitude too coarse to detect localized urbanization. GHSL P2023A offers 10m resolution with AI-driven multispectral classification, a 2500x improvement.
- **Binary classification flaw**: The study reduces urbanization to a yes/no label. Modern science requires parametric inputs—e.g., m²/m² built-up fraction as used in GHSL.
- **No ground-truthing**: No site photos, no Google Earth review, no validation. Assumptions were accepted without visual inspection or spatial audit.
- **Non-continuous station usage**: The ensemble is not fixed in time, preventing any reproducible experiment. This is methodological evasion, not science.
- **No uncertainty bounds**: The classification lacks error margins or statistical confidence levels. The assumption of accuracy is unjustified.
- **Ongoing evasion of critique (2022–2025)**: Repeated refusal by Berkeley Earth (BE) to address technical audits. Instead: public deflection, silence, and coordinated ad hominem responses.
- **Ethical lapses**:
  - Inclusion of authors without permission (e.g., J. Curry in preliminary reports).
  - Ignoring formal feedback from the scientific community.
  - Weaponizing social media to attack independent reviewers instead of addressing substance.
  - Retracted the station list used to prevent scrutiny.
  - BEST: full pseudoscience applied. The method **does not** require the baseline to exist as measured data. They fabricate it with statistical modeling. Even at the station level, the data is a computer model—not measurement. This is not science but **malicious deception**.
- **Aggregation as obfuscation**: Fragmented, non-continuous datasets aggregated to hide methodological gaps. Scientific replication becomes impossible by design.
- **No transition to modern tools**: Despite the availability of GHSL, Sentinel-2, and Google Earth Engine, the original team continues to rely on deprecated, low-resolution data and unsupported classification logic.
- **False equivalence**: The paper’s conclusion that rural and urban trends are similar is statistically constructed on flawed categorization, not empirical reality.

In summary: the 2013 study is methodologically hollow by today’s standards. It was built in an era when 500m pixels were a constraint. Today, with GHSL P2023A’s 10m AI-analyzed, parametric urbanization layers and sub-meter imagery available in Google Earth, the truth is visible—down to the last road, house, or warehouse. No paper can hide behind resolution anymore.

Recent critics have resurrected this outdated study to dispute current high-resolution urban analyses, such as GHSL. This is akin to relying on an obsolete 1-megapixel black-and-white photograph to challenge the validity of today's AI-analyzed, multispectral, 2500-megapixel imagery.

### Audit Objectives

- Extract and verify the "very rural" stations listed in prior audits ([McIntyre 2011](https://climateaudit.org/2011/12/20/berkeley-very-rural-data/), [Connolly 2014](https://doi.org/10.6084/m9.figshare.1005090.v1)).
- Apply the state-of-the-art GHSL P2023A dataset (10m resolution, AI-analyzed, parametric built-up fraction in m²/m²) to each site.
- Conduct manual, sub-10m visual inspections with Sentinel-2 imagery via Google Earth to confirm urban characteristics.
- Highlight methodological inadequacies of the MODIS 500m data used previously.

### Advanced Analytical Tools

- **GHSL P2023A (EC-JRC)**: 10m multispectral raster with parametric urbanization metrics.
- **Sentinel-2 Imagery via Google Earth**: Provides visual ground-truth at sub-10m accuracy.
- **Custom Python Tooling**: Scripts for precise spatial analysis, zonal urbanization statistics, and detailed error-checking.

### Methodological Critique of Original Study

- **Opaque Classification System**: Wickham et al. (2013) omitted essential details on station selection criteria, preventing reproducibility.
- **Unverified Station Data**: Absence of a published station list hinders independent verification.
- **Technological Obsolescence**: MODIS 500m pixel size (250,000 m² per pixel or 25ha) is grossly inadequate, missing urban encroachments detectable with GHSL’s 10m pixels (100 m² per pixel or 0.01 ha).

### Toolset for Modern Urban Classification Audits

Today, any independent researcher with basic technical literacy and an internet connection can perform a high-resolution, parametric urban classification audit using free tools. Google Earth Engine (GEE) provides direct access to over **70 petabytes of satellite data**, including the full GHSL catalog and Sentinel-2 imagery, available globally at 10-meter resolution.

The code to initiate your own classification is available [here](https://github.com/orwell2024/gearth/blob/main/pick_loc_size.js). Simply paste it into the [Google Earth Engine code editor](https://code.earthengine.google.com), modify the coordinates and cell size, and run the script.

To download images, click "Run" in the Console's Tasks section and follow the prompt to save outputs to your Google Drive.

See the [GEE GHSL Project Overview](https://gee-community-catalog.org/projects/ghsl/) for instructions and example scripts.

This democratization of access—once restricted to national meteorological agencies—makes it impossible to justify reliance on outdated 500m MODIS classifications. With GEE, visual inspection, parametric built-up surface metrics, and temporal trend analysis are instantly available to the public. A concise demonstration is provided in [this tweet](https://x.com/orwell2022/status/1848465401195397532), showing real-time classification at sub-10m resolution using GHSL and Earth Engine.

While we worked with BU (built-up surface) using the GHSL, we can also leverage BU\_V (built-up volume) to see where urban centers like New York City are growing vertically. These datasets complement one another:

- [BU (Built-Up Surface)](https://developers.google.com/earth-engine/datasets/catalog/JRC_GHSL_P2023A_GHS_BUILT_S): Detects the horizontal spread of urban structures. See this [tweet demonstration](https://x.com/orwell2022/status/1845801061535162407) for a visual walkthrough using GHSL surface data in Earth Engine.
- [BU\_V (Built-Up Volume)](https://developers.google.com/earth-engine/datasets/catalog/JRC_GHSL_P2023A_GHS_BUILT_V): Highlights the vertical expansion and density of construction. See this [tweet demonstration](https://x.com/orwell2022/status/1845801061535162407) showing New York City's vertical growth patterns with GHSL BU\_V.

[https://github.com/orwell2024/gearth/blob/main/pick\_loc\_size.js](https://github.com/orwell2024/gearth/blob/main/pick_loc_size.js)

[https://x.com/orwell2022/status/1810402372511994323](https://x.com/orwell2022/status/1810402372511994323)

[https://x.com/orwell2022/status/1830981277144826185](https://x.com/orwell2022/status/1830981277144826185)

[https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS\_S2\_SR\_HARMONIZED](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS\_S2\_SR\_HARMONIZED)

Overall view GHSL: try any location you like. Use your google account. It's free.

[https://developers.google.com/earth-engine/datasets/catalog/JRC_GHSL_P2023A_GHS_BUILT_C](https://code.earthengine.google.com/?scriptPath=Examples%3ADatasets%2FJRC%2FJRC_GHSL_P2023A_GHS_BUILT_C)

### Minimum Applicable Standards

- **ISO 9001 Quality Management**: Alignment with internationally recognized standards for process control and documentation.
- **NOAA USCRN Site Quality Criteria**: Reference-class site design with rigorous metadata, siting verification, and instrumentation calibration. See:
  - [Why USCRN Matters – NOAA NCEI](https://www.ncei.noaa.gov/access/crn/why.html)
  - [Official Site Listings](https://www.ncei.noaa.gov/access/crn/sites.html)
  - [Baker Presentation on Climate Reference Networks (NOAA ARL)](https://www.arl.noaa.gov/wp_arl/wp-content/uploads/Review/Presentations/Baker_ClimateReferenceNetworks.pdf)
  - [Independent Summary and Commentary](https://orwell2024.substack.com/p/quality-requirements-proposal-for)
- **WMO Class 1 Minimum Standard**: Ensures optimal siting free from artificial heat sources and structures. See: [MET Report 16-2016](https://www.met.no/publikasjoner/met-report/met-report-2016/_/attachment/download/ece77c3c-90a7-4013-bf1d-c50acf5b41fb%3A35bb6ec95375a950cb518b75842109e6c2e4d555/MET-report-16-2016.pdf) — Norway's meteorological guidelines on climate station suitability.
- **Photographic Evidence**: Archival and current site pictures to confirm surroundings and site integrity.
- **Station Inventory Validation**: Visual and metadata-based checks to confirm operational consistency.
- **Raw Data at Source**: Availability and auditability of original measurement series, not derived products.

### Expected Outcome

We anticipate that most stations originally labeled "very rural" by Wickham et al. (2013) will exhibit measurable urban characteristics under GHSL analysis, significantly compromising their original claims. The expectation is that few, if any, stations will match the rigorous quality standards exemplified by modern [NOAA USCRN](https://www.ncei.noaa.gov/access/crn/) sites.

### Files and Resources

- [`BE_site_detail_Connolly2014_McIntyre2011.txt`](https://github.com/orwell2024/GHCN-tools/blob/main/Wickham2013_forensicauditby_GHSLP2023A/BE_site_detail_Connolly2014_McIntyre2011.txt): Verified source list for forensic audit.
- [`very_rural_unique_ids.txt`](http://www.climateaudit.info/data/station/berkeley/very_rural_unique_ids.txt)
- [`BE_site_detail_Connolly2014_McIntyre2011.txt`](https://raw.githubusercontent.com/orwell2024/GHCN-tools/main/Wickham2013_forensicauditby_GHSLP2023A/BE_site_detail_Connolly2014_McIntyre2011.txt)
- [`GHCNv4_stations_with_BI_BU_orwell2022.csv`](https://raw.githubusercontent.com/orwell2024/GHCN-tools/main/GHCNv4_stations_with_BI_BU_orwell2022.csv)
- [`ghcnd-stations.txt`](https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt)
- [`ghcnd-inventory.txt`](https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-inventory.txt)
- [`v4.temperature.inv.txt`](https://data.giss.nasa.gov/gistemp/station_data_v4_globe/v4.temperature.inv.txt)
- [Climate Audit: Berkeley "Very Rural" Data (2011)](https://climateaudit.org/2011/12/20/berkeley-very-rural-data/)
- [Connolly (2014) Supplementary Data](https://doi.org/10.6084/m9.figshare.1005090.v1)
- [Wickham et al. (2013)](https://berkeley-earth-wp-offload.storage.googleapis.com/wp-content/uploads/2022/12/03232406/UHI-GIGS-1-104.pdf)
- #### Google Earth Engine Datasets Used
- `MODIS/061/MCD12Q1` — MODIS Land Cover (500m, yearly)
- `JRC/GHSL/P2023A/GHS_BUILT_S/2020` — GHSL P2023A Built-up Surface (10m)
- `ESA/WorldCover/v100/2020` — ESA WorldCover 2020 (10m)
- `ESA/WorldCover/v200/2021` — ESA WorldCover 2021 (10m, improved version)
- `COPERNICUS/Landcover/100m/Proba-V/Global` — Copernicus Global Land Cover (100m)

### Ethical and Licensing Statement

This forensic audit adheres strictly to scientific reproducibility standards, employing publicly available datasets under appropriate academic licensing. The focus is methodological rigor and transparency rather than attribution of intent.

### Final Note

Just as modern LLMs easily expose plagiarism in decades-old doctoral theses, modern satellite imagery and AI-driven urban metrics will expose historical inadequacies in station classification. Wickham et al. (2013), conducted with primitive resolution, cannot credibly serve as evidence against contemporary, high-quality urban classification datasets. This audit is critical to restoring methodological rigor and scientific accuracy to climate data assessment.

---

> The integrity of scientific conclusions depends entirely on the integrity of the data classification. Outdated tools obscure realities; modern technologies reveal them.

> The absence of evidence is not evidence of absence—especially when your resolution is a black & white 500m pixel.

![image](https://github.com/user-attachments/assets/16561fe6-d694-4202-b07b-dd602b7284bf)

### Appendix: Google Earth Engine Code — GHSL + MODIS Cropland + Urban

This script loads and visualizes three key land-use indicators in Google Earth Engine:

1. **GHSL P2023A Built-up (2020)** — expanded to 3×3 neighborhood, shown in **purple**
2. **MODIS Cropland (2020)** — class codes 12 and 14, shown in **yellow**
3. **MODIS Urban (2020)** — class code 13, shown in **red**

```javascript
// ---- GHSL Built-up Surface (2020) ----
var ghsl = ee.Image('JRC/GHSL/P2023A/GHS_BUILT_S/2020')
              .select('built_surface')
              .gt(0);  // Built-up presence

// Expand GHSL to 3x3 pixels
var kernel = ee.Kernel.square(1);
var ghslExpanded = ghsl.focal_max({kernel: kernel, iterations: 1});

// ---- MODIS Land Cover (2020) ----
var modis = ee.ImageCollection("MODIS/061/MCD12Q1")
              .filter(ee.Filter.calendarRange(2020, 2020, 'year'))
              .first()
              .select('LC_Type1');

// MODIS cropland: classes 12 and 14
var modisCrop = modis.eq(12).or(modis.eq(14));

// MODIS urban: class 13
var modisUrban = modis.eq(13);

// ---- Layer 1: GHSL built-up (purple) ----
Map.addLayer(ghslExpanded.updateMask(ghslExpanded), 
             {palette: ['purple']}, 
             'GHSL Built-up (Expanded 3x3)');

// ---- Layer 2: MODIS cropland (yellow) ----
Map.addLayer(modisCrop.updateMask(modisCrop), 
             {palette: ['yellow']}, 
             'MODIS Cropland (12 + 14)');

// ---- Layer 3: MODIS urban (red) ----
Map.addLayer(modisUrban.updateMask(modisUrban), 
             {palette: ['red']}, 
             'MODIS Urban (13)');

// ---- Center the map to example region ----
Map.setCenter(5, 52, 8);
![image](https://github.com/user-attachments/assets/43138a0a-5f3f-4777-b344-df6e263c7a69)
![image](https://github.com/user-attachments/assets/415220f6-34c7-49f4-862c-1a4ceee8da9d)
![image](https://github.com/user-attachments/assets/9d7cc9c0-fc81-4cff-a7c7-ba7f6d389d6d)


