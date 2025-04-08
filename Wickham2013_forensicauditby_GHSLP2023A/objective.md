# README.md

## Forensic Audit of "Very Rural" Classifications in Wickham et al. (2013)

### Project Overview
This repository contains a forensic, methodological audit of the rural station classifications used by Wickham et al. (2013). Their study employed outdated MODIS 500m land cover data to select 15,000 "very rural" temperature stations, claiming negligible influence from urban heat islands (UHI) on global temperature trends. With advances in geospatial analysis and AI-driven satellite technology, specifically the GHSL P2023A 10-meter multispectral dataset derived from Sentinel-2 imagery, we critically reassess these classifications.

### Original Study Under Audit
Wickham, C., Curry, J., Groom, D., Jacobsen, R., Muller, R., Perlmutter, S., Rohde, R., Rosenfeld, A., & Wurtele, J. (2013). *Influence of urban heating on the global temperature land average using rural sites identified from MODIS classifications*. Journal of Geophysical Research: Atmospheres, 118(5), 1890–1900. https://doi.org/10.1002/jgrd.50202

### Context and Motivation

The Wickham et al. (2013) paper has become a frequently cited reference to downplay the effect of urbanization on temperature records. Yet upon inspection, the foundation of its argument collapses under modern scrutiny. Several critical methodological and ethical flaws render its conclusions untestable and irreproducible:

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

- **Aggregation as obfuscation**: Fragmented, non-continuous datasets aggregated to hide methodological gaps. Scientific replication becomes impossible by design.

- **No transition to modern tools**: Despite the availability of GHSL, Sentinel-2, and Google Earth Engine, the original team continues to rely on deprecated, low-resolution data and unsupported classification logic.

- **False equivalence**: The paper’s conclusion that rural and urban trends are similar is statistically constructed on flawed categorization, not empirical reality.

In summary: the 2013 study is methodologically hollow by today’s standards. It was built in an era when 500m pixels were a constraint. Today, with GHSL P2023A’s 10m AI-analyzed, parametric urbanization layers and sub-meter imagery available in Google Earth, the truth is visible—down to the last road, house, or warehouse. No paper can hide behind resolution anymore.

Recent critics have resurrected this outdated study to dispute current high-resolution urban analyses, such as GHSL. This is akin to relying on an obsolete 1-megapixel black-and-white photograph to challenge the validity of today's AI-analyzed, multispectral, 2500-megapixel imagery.

### Audit Objectives
- Extract and verify the "very rural" stations listed in prior audits (McIntyre 2011, Connolly 2014).
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

### Why GHSL P2023A?
- **Resolution and Quality**: GHSL provides 10m multispectral, parametric data—a 2500-fold improvement in resolution over MODIS 500m.
- **AI-Driven Analysis**: Automated, reproducible classification with high accuracy and transparency.
- **Time-Series Capability**: Continuous updates allow tracking of urban sprawl and historical analysis.

### Analogical Explanation
Comparing MODIS 500m to GHSL 10m is analogous to using a primitive 1-megapixel monochrome camera to dispute the clarity and validity of modern, AI-processed, multispectral 2500-megapixel images. Just as early neuronal models from 2010 cannot be credibly used today to dispute the capabilities of modern language models (LLMs), outdated MODIS classifications cannot credibly challenge modern GHSL urbanization analyses.

### Audit Procedure
1. **Station Reconstruction**:
   - Utilized prior forensic reconstructions (McIntyre 2011, Connolly 2014) for station lists.

2. **High-Resolution Validation**:
   - Applied GHSL data at radii of 250m, 1km, and 10km.
   - Cross-checked visually via Google Earth Pro (Sentinel-2 imagery).

3. **Classification Analysis**:
   - Parametric GHSL metrics versus binary MODIS labels.

4. **Documentation and Reproducibility**:
   - Clear geospatial documentation, numerical urbanization scores, and transparent audit trail for each site.

### Expected Outcome
We anticipate that most stations originally labeled "very rural" by Wickham et al. (2013) will exhibit measurable urban characteristics under GHSL analysis, significantly compromising their original claims. The expectation is that few, if any, stations will match the rigorous quality standards exemplified by modern NOAA USCRN sites.

### Files and Resources
- [`BE_site_detail_Connolly2014_McIntyre2011.txt`](https://github.com/orwell2024/GHCN-tools/blob/main/Wickham2013_forensicauditby_GHSLP2023A/BE_site_detail_Connolly2014_McIntyre2011.txt): Verified source list for forensic audit.
- GHSL classification outputs (in preparation).

### Ethical and Licensing Statement
This forensic audit adheres strictly to scientific reproducibility standards, employing publicly available datasets under appropriate academic licensing. The focus is methodological rigor and transparency rather than attribution of intent.

### Final Note
Just as modern LLMs easily expose plagiarism in decades-old doctoral theses, modern satellite imagery and AI-driven urban metrics will expose historical inadequacies in station classification. Wickham et al. (2013), conducted with primitive resolution, cannot credibly serve as evidence against contemporary, high-quality urban classification datasets. This audit is critical to restoring methodological rigor and scientific accuracy to climate data assessment.

---

> The integrity of scientific conclusions depends entirely on the integrity of the data classification. Outdated tools obscure realities; modern technologies reveal them.

> The absence of evidence is not evidence of absence—especially when your resolution is a balck & white 500m pixel.
