# Day 76: Data Visualization

## Project: Customer Churn Analysis & Retention Insights

### Objective

Create clear and informative visualizations using Python to present customer churn patterns, compare customer segments, and highlight important retention risks.

### Tools Used
- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

### 1. Dashboard Visual Theme

Established a consistent visual theme across all charts using Seaborn and Matplotlib.

- Background: Light blue-grey (`#DCE6EE`)
- Primary colour: Navy (`#183B56`)
- Secondary colour: Teal (`#16A6A1`)
- Highlight colour: Gold (`#E5A33D`)
- Export resolution: 300 DPI

### 2. Visualizations Created

**1. Customer Churn Distribution**
- Created a donut chart showing stayed and churned customers.
- Total customers: 7,043.
- Stayed: 5,174 (73.46%).
- Churned: 1,869 (26.54%).

**2. Churn Rate by Contract Type**
- Compared churn rates across three contract types.
- Month-to-month: 42.71%.
- One year: 11.27%.
- Two year: 2.83%.

**3. Average Monthly Charges by Customer Status**
- Compared average monthly charges between stayed and churned customers.
- Stayed: ₹61.27.
- Churned: ₹74.44.

**4. Average Customer Tenure by Churn Status**
- Compared average customer tenure.
- Stayed: 37.57 months.
- Churned: 17.98 months.

**5. Churn Rate by Contract and Internet Service**
- Created a heatmap to identify high-risk customer segments.
- Highest churn: Month-to-month contract with Fiber optic service (54.61%).

**6. Churn Rate by Tenure Group**
- Divided customers into New, Medium, and Long-term groups.
- New: 47.44%.
- Medium: 25.54%.
- Long-term: 11.93%.

### 3. Visualization Export

All six visualizations were exported as high-resolution PNG files at 300 DPI.

Saved in the `Visualizations` folder:

1. `01_customer_churn_distribution.png`
2. `02_churn_by_contract.png`
3. `03_average_monthly_charges.png`
4. `04_average_customer_tenure.png`
5. `05_churn_contract_internet_heatmap.png`
6. `06_churn_by_tenure_group.png`

### 4. Key Findings

- Overall customer churn rate is 26.54%.
- Month-to-month customers have a significantly higher churn rate than customers on longer contracts.
- Customers who churned had higher average monthly charges.
- Customers who churned had shorter average tenure.
- Month-to-month Fiber optic customers represent the highest-churn segment.
- New customers have a higher churn rate than medium and long-term customers.

### 5. Outcome

Completed six visualizations using Python, Pandas, Matplotlib, and Seaborn. The charts present customer churn patterns and high-risk segments in a clear and consistent format.

**Status: Day 76 Completed**