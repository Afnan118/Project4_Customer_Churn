# Day 72: Python Data Cleaning

## Project
Customer Churn Analysis & Retention Insights

## Tasks Completed
- Checked missing values using `df.isnull().sum()`.
- Identified 11 blank values in `TotalCharges`.
- Confirmed all 11 affected customers have a tenure of 0 months.
- Checked duplicate records using `df.duplicated().sum()`.
- Found 0 duplicate rows.
- Converted `TotalCharges` from text to numeric using `pd.to_numeric()`.
- Verified that `TotalCharges` now uses the `float64` data type.
- Confirmed the dataset contains 7,043 rows and 21 columns.
- Exported a separate cleaned CSV file.

## Data Quality Decisions
- Preserved all customer records.
- Kept the 11 missing `TotalCharges` values as missing rather than inventing values.
- Preserved the original dataset.

## Skills Practiced
Pandas data cleaning, missing-value detection, duplicate checks, data type conversion, and CSV export.