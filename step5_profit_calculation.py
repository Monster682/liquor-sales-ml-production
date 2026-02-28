import pandas as pd

# LOAD REQUIRED DATA
pos = pd.read_csv("data/pos_transactions.csv")
product = pd.read_csv("data/product_master.csv")
pricing = pd.read_csv("data/pricing_tax.csv")

# MERGE DATASETS
df = pos.merge(product, on="sku_id", how="left")
df = df.merge(pricing, on="sku_id", how="left")

# FIX DATA TYPES
df["quantity_sold"] = df["quantity_sold"].astype(int)
df["selling_price"] = df["selling_price"].astype(float)
df["cost_price"] = df["cost_price"].astype(float)

df["excise_tax_pct"] = df["excise_tax_pct"].astype(float)
df["vat_pct"] = df["vat_pct"].astype(float)


# PROFIT CALCULATIONS

# Gross Revenue
df["gross_revenue"] = df["quantity_sold"] * df["selling_price"]

# Cost of Goods Sold (COGS)
df["cogs"] = df["quantity_sold"] * df["cost_price"]

# Tax per unit
df["excise_tax"] = df["selling_price"] * df["excise_tax_pct"] / 100
df["vat_tax"] = df["selling_price"] * df["vat_pct"] / 100

# Total tax per transaction
df["total_tax"] = (df["excise_tax"] + df["vat_tax"]) * df["quantity_sold"]

# Net Profit
df["net_profit"] = df["gross_revenue"] - df["cogs"] - df["total_tax"]


# SAVE OUTPUT FOR NEXT STEPS
df.to_csv("data/profit_data.csv", index=False)

print("STEP 5 COMPLETED: Profit Calculated & Saved")
print(df[["gross_revenue", "cogs", "total_tax", "net_profit"]].head())
