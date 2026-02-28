import pandas as pd

# Load datasets
pos = pd.read_csv("data/pos_transactions.csv")
store = pd.read_csv("data/store_city_master.csv")
product = pd.read_csv("data/product_master.csv")
pricing = pd.read_csv("data/pricing_tax.csv")
inventory = pd.read_csv("data/inventory.csv")
calendar = pd.read_csv("data/calendar.csv")

# Clean POS data
pos["date"] = pd.to_datetime(pos["date"])
pos = pos.dropna()
pos = pos.drop_duplicates()
pos["quantity_sold"] = pos["quantity_sold"].astype(int)
pos["selling_price"] = pos["selling_price"].astype(float)

# Clean Inventory
inventory["date"] = pd.to_datetime(inventory["date"])
inventory = inventory.fillna(0)


