# Day 71 — Data Exploration

## Project
Customer Churn Analysis & Retention Insights

## Dataset
IBM Telco Customer Churn dataset

## Dataset Overview
- Total customer records: 7,043
- Total columns: 21
- Python library used: Pandas

## Key Findings

| Metric | Finding |
|---|---:|
| Total customers | 7,043 |
| Customers who stayed | 5,174 |
| Customers who left | 1,869 |
| Churn rate | 26.54% |
| Average tenure | 32.37 months |
| Average monthly charges | 64.76 |

## Initial Data Quality Observation
The `TotalCharges` column was loaded as text (`str`) rather than a numeric data type. This will be investigated during Day 72 data cleaning.

## Python Skills Practiced
- Loading a CSV with `pd.read_csv()`
- Inspecting records with `df.head()`
- Checking dimensions with `df.shape`
- Reviewing columns with `df.columns`
- Inspecting data types with `df.info()`
- Summarizing numerical data with `df.describe()`
- Counting categories with `value_counts()`
- Calculating churn rate using Python

## Business Interpretation
Approximately 26.54% of customers in this dataset have a churn value of Yes. Further analysis is needed to identify customer groups associated with higher churn and develop evidence-based retention recommendations.

## Next Steps
Day 72 — investigate missing or blank values, duplicate records, and data types while preserving the original dataset.
