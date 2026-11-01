# Day 75 - Advanced Churn Analysis

## 1. Objective

To investigate combinations of customer characteristics, identify high-risk customer segments, and discover deeper patterns associated with customer churn.

## 2. Contract Type + Internet Service

| Contract | Internet Service | Churn Rate |
|---|---|---:|
| Month-to-month | DSL | 32.22% |
| Month-to-month | Fiber optic | 54.61% |
| Month-to-month | No internet | 18.89% |
| One year | DSL | 9.30% |
| One year | Fiber optic | 19.29% |
| One year | No internet | 2.47% |
| Two year | DSL | 1.91% |
| Two year | Fiber optic | 7.23% |
| Two year | No internet | 0.78% |

**Finding:** Month-to-month Fiber optic customers have the highest churn rate at 54.61%.

**Recommendation:** Investigate Fiber optic service quality, pricing, competitor offers, and customer satisfaction.

## 3. Contract Type + Monthly Charges

| Contract | Average Monthly Charges | Churn Rate |
|---|---:|---:|
| Month-to-month | 66.40 | 42.71% |
| One year | 65.05 | 11.27% |
| Two year | 60.77 | 2.83% |

**Finding:** Month-to-month customers pay the highest average monthly charges and have the highest churn rate.

**Recommendation:** Review pricing structures, compare competitor plans, and investigate whether customers receive sufficient value.

## 4. Tenure Groups + Churn

Customers were divided into three groups:

- New: 0–12 months
- Medium: 13–36 months
- Long-term: More than 36 months

| Tenure Group | Stayed | Churned |
|---|---:|---:|
| New | 52.56% | 47.44% |
| Medium | 74.46% | 25.54% |
| Long-term | 88.07% | 11.93% |

**Finding:** New customers have the highest churn rate at 47.44%.

**Recommendation:** Improve onboarding, provide introductory offers, collect customer feedback, and monitor new customers regularly.

## 5. Internet Service + Payment Method

| Internet Service | Payment Method | Churn Rate |
|---|---|---:|
| DSL | Bank transfer | 9.36% |
| DSL | Credit card | 12.12% |
| DSL | Electronic check | 31.94% |
| DSL | Mailed check | 20.72% |
| Fiber optic | Bank transfer | 28.95% |
| Fiber optic | Credit card | 25.29% |
| Fiber optic | Electronic check | 53.23% |
| Fiber optic | Mailed check | 42.64% |
| No internet | Bank transfer | 5.42% |
| No internet | Credit card | 2.72% |
| No internet | Electronic check | 12.30% |
| No internet | Mailed check | 9.58% |

**Finding:** Fiber optic customers using electronic checks have the highest churn rate at 53.23%.

**Recommendation:** Investigate payment-related difficulties, Fiber optic service quality, and customer complaints.

## 6. High-Risk Customer Segments

The analysis identified the following groups with relatively high churn:

1. Month-to-month + Fiber optic: 54.61%.
2. Fiber optic + Electronic check: 53.23%.
3. New customers (0–12 months): 47.44%.
4. Month-to-month customers: 42.71%.
5. Customers without Tech Support: 41.64%.

These segments can overlap, and their churn rates should not be added together.

## 7. Key Business Recommendations

- Prioritise investigation of month-to-month Fiber optic customers.
- Review pricing and competitor offers.
- Improve onboarding for new customers.
- Investigate payment-related complaints.
- Improve technical support availability.
- Monitor customer churn across different segments.

## 8. Important Limitations

- These findings show associations, not proven causes of churn.
- Further customer feedback and competitor research are needed.
- Customer counts within each segment should be checked before prioritising business spending.
- Additional analysis is required to understand whether multiple risk factors overlap.

## 9. Conclusion

Advanced churn analysis helped identify customer segments with higher churn rates by combining contract type, internet service, tenure, and payment method.

The most important areas for further investigation are month-to-month Fiber optic customers, Fiber optic customers using electronic checks, and customers in their first year.

These findings can guide the company's next steps in improving customer retention.