import pandas as pd

df = pd.read_csv("data/pos_transactions.csv")

df["quantity_sold"] = df["quantity_sold"].astype(int)
df["selling_price"] = df["selling_price"].astype(float)

# KPI 1: Total Quantity Sold
total_qty = df["quantity_sold"].sum()

# KPI 2: Total Revenue
df["revenue"] = df["quantity_sold"] * df["selling_price"]
total_revenue = df["revenue"].sum()

# KPI 3: Average Selling Price
avg_price = df["selling_price"].mean()

# KPI 4: Store-wise Sales
store_sales = df.groupby("store_id")["quantity_sold"].sum()

# KPI 5: Top Selling Products
top_products = (
    df.groupby("sku_id")["quantity_sold"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print("Total Quantity Sold:", total_qty)
print("Total Revenue:", total_revenue)
print("Average Selling Price:", avg_price)
print("Store-wise Sales:")
print(store_sales)
print("Top Products:")
print(top_products)
