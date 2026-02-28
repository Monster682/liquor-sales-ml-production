import pandas as pd

# load profit data
df = pd.read_csv("data/profit_data.csv")
calendar = pd.read_csv("data/calendar.csv")

# convert date
df["date"] = pd.to_datetime(df["date"])
calendar["date"] = pd.to_datetime(calendar["date"])

# merge calendar
df = df.merge(calendar, on="date", how="left")

# SKU average selling price
df["sku_avg_price"] = df.groupby("sku_id")["selling_price"].transform("mean")

# margin percentage
df["margin_pct"] = (df["net_profit"] / df["gross_revenue"]) * 100

# weekend & festival flags
df["is_weekend"] = df["is_weekend"].fillna(0)
df["festival_flag"] = df["festival_flag"].fillna(0)

# sort for rolling
df = df.sort_values("date")

# rolling profit trends
df["profit_7d_avg"] = df.groupby("sku_id")["net_profit"].transform(
    lambda x: x.rolling(7, min_periods=1).mean()
)

df["profit_30d_avg"] = df.groupby("sku_id")["net_profit"].transform(
    lambda x: x.rolling(30, min_periods=1).mean()
)

# save for modeling
df.to_csv("data/feature_data.csv", index=False)

print("STEP 6 COMPLETED: Feature Engineering Done")
print(df.head())
