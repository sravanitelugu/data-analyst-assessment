import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
raw_path = BASE / "data" / "customer_purchase_engagement_raw.csv"
clean_path = BASE / "data" / "customer_purchase_engagement_cleaned.csv"
visuals = BASE / "visuals"
visuals.mkdir(exist_ok=True)

df = pd.read_csv(raw_path)

# 1) Data cleaning
df = df.dropna(subset=["customer_id", "purchase_date"]).copy()
df["product_category"] = df["product_category"].replace({"electronics": "Electronics"})
df["marketing_channel"] = df["marketing_channel"].fillna("Unknown")
df["session_duration_min"] = df["session_duration_min"].fillna(df["session_duration_min"].median())
df["purchase_amount_usd"] = df["purchase_amount_usd"].fillna(df["purchase_amount_usd"].median())
df["purchase_date"] = pd.to_datetime(df["purchase_date"])
df = df.drop_duplicates(subset=[c for c in df.columns if c != "transaction_id"])

# 2) Feature engineering
df["month"] = df["purchase_date"].dt.to_period("M").astype(str)
df["is_weekend"] = df["purchase_date"].dt.weekday >= 5

# 3) Save cleaned dataset
df.to_csv(clean_path, index=False)

# 4) Summary metrics
summary = {
    "total_revenue": round(df["purchase_amount_usd"].sum(), 2),
    "total_orders": len(df),
    "unique_customers": df["customer_id"].nunique(),
    "avg_order_value": round(df["purchase_amount_usd"].mean(), 2)
}
print(summary)

# 5) Charts
monthly = df.groupby("month")["purchase_amount_usd"].sum()
plt.figure(figsize=(8, 5))
monthly.plot(marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (USD)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(visuals / "monthly_revenue_trend.png", dpi=180)
plt.close()

category = df.groupby("product_category")["purchase_amount_usd"].sum().sort_values()
plt.figure(figsize=(8, 5))
category.plot(kind="barh")
plt.title("Revenue by Product Category")
plt.xlabel("Revenue (USD)")
plt.ylabel("Product Category")
plt.tight_layout()
plt.savefig(visuals / "revenue_by_category.png", dpi=180)
plt.close()

channel = df.groupby("marketing_channel")["purchase_amount_usd"].mean().sort_values(ascending=False)
plt.figure(figsize=(8, 5))
channel.plot(kind="bar")
plt.title("Average Order Value by Marketing Channel")
plt.xlabel("Marketing Channel")
plt.ylabel("Average Order Value (USD)")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig(visuals / "aov_by_channel.png", dpi=180)
plt.close()

weekend = df.groupby(df["is_weekend"].map({True: "Weekend", False: "Weekday"}))["purchase_amount_usd"].mean()
plt.figure(figsize=(7, 5))
weekend.plot(kind="bar")
plt.title("Average Order Value: Weekend vs Weekday")
plt.xlabel("")
plt.ylabel("Average Order Value (USD)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(visuals / "weekend_vs_weekday_aov.png", dpi=180)
plt.close()
