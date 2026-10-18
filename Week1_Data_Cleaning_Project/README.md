# Week 1 — Data Acquisition, Cleaning, and Preprocessing

## Important note
This ZIP contains a **small practice dataset** so you can run the code immediately and learn the workflow offline. It is not the full public dataset required by the internship brief. For your final submission, download a public dataset from a reliable source (for example, the Titanic dataset on Kaggle or a public GitHub mirror), keep the source URL, and update `DATA_SOURCE` in `data_cleaning.py` to the downloaded CSV. Then rerun the script and refresh the report results/screenshots.

## Files and folders
- `data/practice_customer_data_raw.csv` — raw practice dataset with intentional data-quality issues.
- `data_cleaning.py` — Python cleaning and preprocessing script.
- `requirements.txt` — Python packages required.
- `outputs/` — generated output files and chart after running the script.
- `screenshots/` — place your own screenshots here; a guide is in the report.
- `Week1_Data_Cleaning_Report.docx` — editable report with method, code explanation, and screenshot checklist.

## Run on a Windows laptop
1. Install Python 3.11+ from https://www.python.org/downloads/ and tick **Add Python to PATH** during installation.
2. Extract this ZIP to a simple folder, for example `C:\Users\YourName\Documents\Week1_Data_Cleaning_Project`.
3. Open that folder in VS Code, or open Command Prompt in the folder.
4. Install packages:
   `py -m pip install -r requirements.txt`
5. Run:
   `py data_cleaning.py`
6. Open the `outputs` folder. Check `initial_profile.txt`, `cleaning_summary.txt`, `outlier_flags.csv`, `cleaned_customer_data.csv`, and `missing_values_before_after.png`.
7. Open the DOCX report and replace the practice-data note/results with the results from your chosen public dataset before submitting.

## Use a public dataset
1. Download a CSV dataset from a reliable public source. Keep the URL and dataset title.
2. Put the CSV inside the `data` folder.
3. Open `data_cleaning.py` in VS Code.
4. Change the line `DATA_SOURCE = DATA_DIR / "practice_customer_data_raw.csv"` to your filename, for example `DATA_SOURCE = DATA_DIR / "titanic.csv"`.
5. The cleaning script includes example column names (`age`, `annual_income`, `gender`). If the public dataset has different column names, adjust the cleaning rules to match that dataset; do not blindly run domain rules on unrelated columns.
6. Run the script again and capture your own screenshots of code, terminal output, and generated chart.

## GitHub upload (laptop)
1. Sign in to https://github.com/ and click **New repository**.
2. Repository name: `week1-data-cleaning-preprocessing`.
3. Set it to Public if your internship requires a public repo. Do not upload private/personal data.
4. Create the repository. If you are using the browser upload method, click **Add file > Upload files**.
5. Extract the ZIP locally. Open the project folder, select the project files/folders (`data`, `outputs`, `screenshots`, `data_cleaning.py`, `requirements.txt`, `README.md`, report DOCX), and upload them. Upload the contents, not the ZIP file alone.
6. In the commit message, type `Add Week 1 data cleaning project` and click **Commit changes**.
7. Open the repository and verify the files are visible. Copy the repository URL for your internship submission.
8. If using browser upload, upload generated outputs only after you have run the script and verified they are current. You can exclude the practice dataset if replacing it with the public dataset.

## Screenshot checklist
Take your own screenshots using `Win + Shift + S`:
- Python script open in VS Code (show the key cleaning steps).
- Terminal after running `py data_cleaning.py`.
- `cleaning_summary.txt` or output values.
- Generated missing-values chart.
- GitHub repository showing uploaded files.
Paste these screenshots into the DOCX report and optionally place copies in `screenshots/`.

## Caution
Do not claim the public dataset was used until you actually download it. Do not invent result values or screenshots. Keep a copy of the raw CSV and write down every cleaning decision.
