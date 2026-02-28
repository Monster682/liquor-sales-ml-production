import pandas as pd

# LOAD FEATURE DATA
df = pd.read_csv("data/feature_data.csv")

# SKU LEVEL PROFIT
sku_profit = (
    df.groupby("sku_id")["net_profit"]
    .sum()
    .reset_index()
)

# sort by profit
sku_profit = sku_profit.sort_values("net_profit", ascending=False)

# TOP 20% PROFIT SKUs
top_20_percent_count = int(len(sku_profit) * 0.2)

top_skus = sku_profit.head(top_20_percent_count)


# LOSS MAKING SKUs
loss_skus = sku_profit[sku_profit["net_profit"] <= 0]


# SAVE OUTPUTS
top_skus.to_csv("data/top_20_percent_skus.csv", index=False)
loss_skus.to_csv("data/loss_making_skus.csv", index=False)

print("BUSINESS OUTPUT GENERATED")
print("\nTop 20% Profit Generating SKUs:")
print(top_skus.head())

print("\nLoss Making / Low Profit SKUs:")
print(loss_skus.head())
