import pandas as pd
df = pd.read_csv("data/Telco-Customer-Churn-Cleaned.csv")
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())
print(df["Churn"].value_counts())
churn_count = (df["Churn"] == "Yes").sum()
total_customers = len(df)

churn_rate = (churn_count / total_customers) * 100

print("Churn Rate:", round(churn_rate, 2), "%")
print(df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())
print(df.dtypes)
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
print(df["TotalCharges"].dtype)
print("Missing TotalCharges:", df["TotalCharges"].isnull().sum())
print(df.dtypes)
print(df.shape)
df.to_csv("data/Telco-Customer-Churn-Cleaned.csv", index=False)
print(df["gender"].value_counts())
print(df.groupby("gender")["Churn"].value_counts())
print(pd.crosstab(df["gender"], df["Churn"], normalize="index") * 100)
print(df["SeniorCitizen"].value_counts())
print(pd.crosstab(df["SeniorCitizen"], df["Churn"], normalize="index") * 100)
print(df["Partner"].value_counts())
print(pd.crosstab(df["Partner"], df["Churn"]))
print(pd.crosstab(df["Partner"], df["Churn"], normalize="index") * 100)
print(df["Dependents"].value_counts())
print(pd.crosstab(df["Dependents"], df["Churn"], normalize="index") * 100)
print(df["Contract"].value_counts())
print(pd.crosstab(df["Contract"], df["Churn"], normalize="index") * 100)
print(df.groupby("Churn")["MonthlyCharges"].mean())
print(df.groupby("Churn")["TotalCharges"].mean())
print(df.groupby("Churn")["tenure"].mean())
print(pd.crosstab(df["InternetService"], df["Churn"], normalize="index") * 100)
print(pd.crosstab(df["PaymentMethod"], df["Churn"], normalize="index") * 100)
print(pd.crosstab(df["OnlineSecurity"], df["Churn"], normalize="index") * 100)
print(pd.crosstab(df["TechSupport"], df["Churn"], normalize="index") * 100)
print(df["Churn"].value_counts())
print(df["Churn"].value_counts(normalize=True) * 100)
print(df.groupby("Churn")["MonthlyCharges"].mean())
print(pd.crosstab([df["Contract"], df["InternetService"]], df["Churn"], normalize="index") * 100)
print(df.groupby("Contract")["MonthlyCharges"].mean())
print(pd.crosstab(df["Contract"], df["Churn"], normalize="index") * 100)
df["TenureGroup"] = pd.cut(
    df["tenure"],
    bins=[-1, 12, 36, float("inf")],
    labels=["New", "Medium", "Long-term"]
)
print(df["TenureGroup"].value_counts())
print(pd.crosstab(df["TenureGroup"], df["Churn"], normalize="index") * 100)
print(pd.crosstab(
    [df["InternetService"], df["PaymentMethod"]],
    df["Churn"],
    normalize="index"
) * 100)