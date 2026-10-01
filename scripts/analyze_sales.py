import pandas as pd

df = pd.read_csv("data/sales_data.csv")

print("Sales Analytics Report")
print("======================")

print(f"\nTotal Sales: ${df['Sales'].sum():,.2f}")
print(f"Total Profit: ${df['Profit'].sum():,.2f}")
print(f"Total Orders: {df['Order_ID'].nunique():,}")
print(f"Total Quantity: {df['Quantity'].sum():,}")

print("\nSales by Region:")
print(df.groupby("Region")["Sales"].sum().sort_values(ascending=False))

print("\nProfit by Category:")
print(df.groupby("Category")["Profit"].sum().sort_values(ascending=False))

print("\nTop Products by Sales:")
print(df.groupby("Product")["Sales"].sum().sort_values(ascending=False))
