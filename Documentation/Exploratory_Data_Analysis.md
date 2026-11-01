# Day 73 – Exploratory Data Analysis (EDA)

## Project
Customer Churn Analysis & Retention Insights

## Dataset
IBM Telco Customer Churn Dataset

## Analysis Performed

### 1. Customer Demographics
- Female churn rate: 26.92%
- Male churn rate: 26.16%
- Senior citizen churn rate: 41.68%
- Customers without partners: 32.96%
- Customers without dependents: 31.28%

### 2. Contract Analysis

| Contract | Churn Rate |
|---|---:|
| Month-to-month | 42.71% |
| One year | 11.27% |
| Two year | 2.83% |

### 3. Charges and Tenure
- Average monthly charges (stayed): 61.27
- Average monthly charges (churned): 74.44
- Average total charges (stayed): 2555.34
- Average total charges (churned): 1531.80
- Average tenure (stayed): 37.57 months
- Average tenure (churned): 17.98 months

### 4. Customer Service and Payment Groups

| Customer Group | Churn Rate |
|---|---:|
| Fiber optic | 41.89% |
| DSL | 18.96% |
| No internet service | 7.40% |
| Electronic check | 45.29% |
| Bank transfer (automatic) | 16.71% |
| Credit card (automatic) | 15.24% |
| Mailed check | 19.11% |
| No Online Security | 41.77% |
| Has Online Security | 14.61% |
| No Tech Support | 41.64% |
| Has Tech Support | 15.17% |

## Key Business Insights

1. Month-to-month customers have substantially higher churn than long-term contract customers.
2. Senior citizens show a higher churn rate than non-senior customers.
3. Customers without partners or dependents have higher churn rates.
4. Churned customers have higher average monthly charges and shorter average tenure.
5. Fiber optic customers show higher churn than DSL customers.
6. Electronic check users have the highest churn among payment methods.
7. Customers without Online Security or Tech Support have higher churn rates.

## Business Recommendations

- Explore retention offers for month-to-month customers.
- Investigate pricing and service concerns among fiber optic customers.
- Improve support and service engagement for customers without Online Security or Tech Support.
- Review payment experience and encourage convenient automatic payment options.
- Focus retention efforts on newer customers.

## Skills Practiced

Python, Pandas, groupby(), mean(), value_counts(), crosstab(), normalize, and Exploratory Data Analysis.

## Conclusion

The analysis identified several customer groups associated with higher churn. Contract type, tenure, payment method, internet service, and support services show notable patterns. Further analysis is required to understand the underlying reasons and develop evidence-based retention strategies.