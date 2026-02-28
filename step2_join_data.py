import pandas as pd

# Load cleaned data
pos = pd.read_csv("data/pos_transactions.csv")
store = pd.read_csv("data/store_city_master.csv")
product = pd.read_csv("data/product_master.csv")
pricing = pd.read_csv("data/pricing_tax.csv")
calendar = pd.read_csv("data/calendar.csv")

pos["date"] = pd.to_datetime(pos["date"])
calendar["date"] = pd.to_datetime(calendar["date"])

# Join POS + Store
df = pos.merge(store, on="store_id", how="left")

# Join Product
df = df.merge(product, on="sku_id", how="left")

# Join Pricing
df = df.merge(pricing, on="sku_id", how="left")

# Join Calendar
df = df.merge(calendar, on="date", how="left")

print(df.head())
