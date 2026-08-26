print("My EDA Project Started")
import pandas as pd

data = pd.read_csv("superstore.csv")
print(data.head())
print(data.shape)
print(data.columns)
print(data.isnull().sum())
print(data.info())
print(data.describe())
print(data.duplicated().sum())
print(data.dtypes)
data["Order Date"] = pd.to_datetime(data["Order Date"])
data["Ship Date"] = pd.to_datetime(data["Ship Date"])
print(data["Sales"].describe())
print(data.groupby("Category")["Sales"].sum())
print(data.groupby("Category")["Profit"].sum())
print(data.groupby("Region")["Sales"].sum())
print(data.groupby("Region")["Profit"].sum())
print(data.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False))
print(data.groupby("Sub-Category")["Profit"].sum().sort_values(ascending=False))
print(data.groupby("Segment")["Sales"].sum().sort_values(ascending=False))
import matplotlib.pyplot as plt

data.groupby("Category")["Sales"].sum().plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.savefig("sales_by_category.png")
plt.close()
data.groupby("Region")["Sales"].sum().plot(kind="bar")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")

plt.savefig("sales_by_region.png")
plt.close()
data.groupby("Category")["Profit"].sum().plot(kind="bar")

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Total Profit")

plt.savefig("profit_by_category.png")
plt.close()
data.groupby("Region")["Profit"].sum().plot(kind="bar")

plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Total Profit")

plt.savefig("profit_by_region.png")
plt.close()
data["Month"] = data["Order Date"].dt.to_period("M")

monthly_sales = data.groupby("Month")["Sales"].sum()

monthly_sales.plot(kind="line")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.savefig("monthly_sales_trend.png")
plt.close()
top_products = data.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

print(top_products)
top_customers = data.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False).head(10)

print(top_customers)
loss_products = data.groupby("Product Name")["Profit"].sum().sort_values().head(10)

print(loss_products)
print("Total Sales:", data["Sales"].sum())
print("Total Profit:", data["Profit"].sum())
profit_margin = (data["Profit"].sum() / data["Sales"].sum()) * 100

print("Overall Profit Margin:", profit_margin, "%")
print(data[data["Postal Code"].isnull()]["Country"].value_counts())
import matplotlib.pyplot as plt
# Category-wise Sales
category_sales = data.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8, 5))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
# Category-wise Profit
category_profit = data.groupby("Category")["Profit"].sum()

plt.figure(figsize=(8, 5))
category_profit.plot(kind="bar")
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Total Profit")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
# Top 10 Products by Sales

top_products = data.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
top_products.plot(kind="bar")
plt.title("Top 10 Products by Sales")
plt.xlabel("Product Name")
plt.ylabel("Total Sales")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("top_10_products_by_sales.png")
plt.close()
