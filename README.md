# pyclimproj

**pyclimproj** is a Python package for downloading, pre-processing, and visualizing CMIP6-based hydroclimatic projection data hosted on the [ORNL HydroSource SWA9505V3 portal](https://hydrosource2.ornl.gov/files/SWA9505V3/).  
The SWA9505V3 archive contains CMIP6-based hydrologic projections (e.g., precipitation, temperature, snowpack, runoff) bias-corrected and spatially disaggregated to CONUS scales. This package simplifies the process of recursively browsing directories, filtering relevant NetCDF files by variable or scenario, and downloading them locally for further scientific analysis.
---

## Features

- **Recursive folder scanning** to explore model subdirectories
- **Selective NetCDF download** using variable keywords or file patterns
- **Base URL independence** — works with any structured file server like the ORNL HydroSource portal
- Easily integrates with `xarray`, `netCDF4`, or `matplotlib` for downstream analysis
- Organizes files locally while preserving folder structure

---

## Directory Structure Example

Example structure from ORNL HydroSource:

SWA9505V3/
├── ACCESS-CM2_ssp126_r1i1p1f1_DBCCA_Daymet/
│   ├── prcp/
│   │   ├── AACCESS-CM2_ssp126_r1i1p1f1_DBCCA_Daymet_VIC4_prcp_1980.nc
│   │   ├── AACCESS-CM2_ssp126_r1i1p1f1_DBCCA_Daymet_VIC4_prcp_1981.nc
│   │   └── ...
│   ├── tmin/
│   │   └── ACCESS-CM2_ssp126_r1i1p1f1_DBCCA_Daymet_VIC4_tmin_1980.nc
│   └── runoff/
│       └── ACCESS-CM2_ssp126_r1i1p1f1_DBCCA_Daymet_VIC4_runoff_1980.nc

---

## Installation

### Option 1: Install using pip

```bash
pip install pyclimproj
```

### Option 2: Clone and install locally

```bash
git clone https://github.com/your-username/pyclimproj.git
cd pyclimproj
pip install .
```

### Requirements
This package requires: requests and beautifulsoup4

You can install them manually if needed:
pip install requests beautifulsoup4

---

## API Overview
Downloader(base_url, out_dir="downloads", verbose=True)

    base_url: Root folder URL to start from

    out_dir: Local output folder

    verbose: Show download progress

.recursive_download(url, local_dir, match_pattern=None)

    url: Subfolder to begin scanning

    local_dir: Destination for downloads

    match_pattern: Filter files by keyword (e.g., prcp, runoff, swe)

### License
This project is licensed under the MIT License.

### Author
Surabhi Upadhyay
GitHub: @surabhiupadhyay

### Contributions
Issues, suggestions, or improvements are welcome!
Please open a GitHub issue or submit a pull request.






