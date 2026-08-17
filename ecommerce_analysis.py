import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# E-COMMERCE DATA ANALYSIS & VISUALIZATION

# Load cleaned dataset
df = pd.read_excel("ecommerc_dataset_cleaned.xlsx", sheet_name="Cleaned_Data")

# Inspect data
print(df.head())
print(df.columns.tolist())
print("Dataset shape:", df.shape)

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# 1. Sales by Category
category_sales = df.groupby("Category", as_index=False)["Sales"].sum().sort_values("Sales", ascending=False)
sns.barplot(data=category_sales, x="Category", y="Sales")
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Monthly Sales
monthly_sales = df.groupby(df["Order_Date"].dt.to_period("M"))["Sales"].sum().reset_index()
monthly_sales["Order_Date"] = monthly_sales["Order_Date"].dt.to_timestamp()
sns.lineplot(data=monthly_sales, x="Order_Date", y="Sales", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Top 10 Products
top_products = df.groupby("Product", as_index=False)["Sales"].sum().sort_values("Sales", ascending=False).head(10)
sns.barplot(data=top_products, x="Sales", y="Product")
plt.title("Top 10 Products by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Product")
plt.tight_layout()
plt.show()

# 4. State-wise Sales
state_sales = df.groupby("State", as_index=False)["Sales"].sum().sort_values("Sales", ascending=False)
sns.barplot(data=state_sales, x="Sales", y="State")
plt.title("Sales by State")
plt.xlabel("Total Sales")
plt.ylabel("State")
plt.tight_layout()
plt.show()

# 5. Customer Type
customer_sales = df.groupby("Customer_Type", as_index=False)["Sales"].sum()
sns.barplot(data=customer_sales, x="Customer_Type", y="Sales")
plt.title("Sales by Customer Type")
plt.xlabel("Customer Type")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# 6. Payment Method
payment_sales = df.groupby("Payment_Mode", as_index=False)["Sales"].sum().sort_values("Sales", ascending=False)
sns.barplot(data=payment_sales, x="Payment_Mode", y="Sales")
plt.title("Sales by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 7. Age Group
bins = [17, 25, 35, 45, 60, 100]
labels = ["18-25", "26-35", "36-45", "46-60", "61+"]
df["Age_Group"] = pd.cut(df["Age"], bins=bins, labels=labels)
age_sales = df.groupby("Age_Group", observed=False, as_index=False)["Sales"].sum()
sns.barplot(data=age_sales, x="Age_Group", y="Sales")
plt.title("Sales by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# 8. Discount vs Profit
sns.boxplot(data=df, x="Discount", y="Profit")
plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.tight_layout()
plt.show()

# 9. Sales vs Profit
sns.scatterplot(data=df, x="Sales", y="Profit", hue="Category")
plt.title("Sales vs Profit by Category")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.tight_layout()
plt.show()

# KPI Summary
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order_ID"].nunique()
average_order_value = total_sales / total_orders
average_rating = df["Rating"].mean()

print("\n===== KPI SUMMARY =====")
print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Total Orders:", total_orders)
print("Average Order Value:", average_order_value)
print("Average Rating:", average_rating)
