# Project Support Files

This folder contains helper scripts, intermediate data, and generated exports that are not required for running the main web app.

## Files

- `analyze_poles.py` - helper script for inspecting pole data and finding patterns.
- `check_data.py` - validation script for checking data quality in the pole dataset.
- `check_issues.py` - script used to find problems or inconsistencies in the data.
- `convert_csv_to_dict.py` - converts the CSV pole file into a Python dictionary format.
- `excelToDict.py` - converts Excel data into a Python dictionary.
- `fix_commas.py` - cleanup script for correcting formatting issues in generated data.
- `json_to_excel.py` - converts JSON files into Excel workbooks.
- `json_to_excel_simple.py` - simpler version of the JSON to Excel converter without `argparse`.
- `make_poles_excel.py` - creates the formatted region-based Excel workbook.
- `reformat_gps.py` - reformats GPS-related data for easier use in the project.
- `test_coords.py` - test script for coordinate-related checks.
- `test_regex.py` - test script for regex pattern checks.
- `gps_coordinates - Sheet1.csv` - source CSV file containing pole coordinate data.
- `gps_coordinates.xlsx` - Excel version of the GPS coordinate source data.
- `gps_data.pdf` - exported reference document for the pole dataset.
- `poles_by_region.txt` - text export grouping poles by region.
- `poles_by_region.xlsx` - Excel export grouping poles by region.
- `venv_packages.txt` - list of packages from the Python environment.

## Main project files kept at the root

The following files remain in the project root because they are used by the application itself:

- `app.py`
- `gps_data_dict.py`
- `requirements.txt`
- `templates/`
- `static/`
- `Pole_image/`

## Notes

- `poles_by_region.xlsx` is still in the root because it was locked by another process when the cleanup ran.
- `~$poles_by_region.xlsx` is a temporary Excel lock file and can be ignored.

