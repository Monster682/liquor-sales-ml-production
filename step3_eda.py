import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/pos_transactions.csv")
df["date"] = pd.to_datetime(df["date"])

# Total sales
print("Total Quantity Sold:", df["quantity_sold"].sum())

# Sales by payment mode
payment = df.groupby("payment_mode")["quantity_sold"].sum()
payment.plot(kind="bar", title="Sales by Payment Mode")
plt.show()

# Daily sales trend
daily = df.groupby("date")["quantity_sold"].sum()
daily.plot(title="Daily Sales Trend")
plt.show()

# Top 5 products
top_products = (
    df.groupby("sku_id")["quantity_sold"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)
print("Top Products:")
print(top_products)
