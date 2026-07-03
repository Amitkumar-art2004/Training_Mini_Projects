import numpy as np
import pandas as pd
np.random.seed(42)
n_rows = 1000
data = {
    "Order_ID": range(1001, 1001 + n_rows),
    "Date": pd.date_range(start="2025-01-01", periods=n_rows, freq="h"),
    "Region": np.random.choice(
        ["North", "South", "East", "West", "Central"], size=n_rows
    ),
    "Team_Lead": np.random.choice(
        ["Alpha", "Beta", "Gamma", "Delta"], size=n_rows
    ),
    "Product_Category": np.random.choice(
        ["Electronics", "Clothing", "Home Decor", "Sports", "Books"],
        size=n_rows,
    ),
    "Units_Sold": np.random.randint(1, 15, size=n_rows),
    "Unit_Price": np.random.uniform(10.0, 500.0, size=n_rows).round(2),
    "Discount": np.random.choice(
        [0.0, 0.05, 0.10, 0.15, np.nan], size=n_rows, p=[0.4, 0.3, 0.1, 0.1, 0.1]
    ),  # Introducing NaNs
    "Customer_Rating": np.random.choice(
        [1, 2, 3, 4, 5, np.nan], size=n_rows, p=[0.05, 0.05, 0.2, 0.3, 0.3, 0.1]
    ),  # Introducing NaNs
}

df = pd.DataFrame(data)

print("--- RAW DATA OVERVIEW ---")
print(df.info())
print("-" * 50)
# -------------------------------------------------------------------------
# STEP 1: DATA CLEANING & PREPARATION
# -------------------------------------------------------------------------

df["Discount"] = df["Discount"].fillna(0.0)

# Fill missing Customer Ratings with the median rating of that Product Category
df["Customer_Rating"] = df.groupby("Product_Category")[
    "Customer_Rating"
].transform(lambda x: x.fillna(x.median()))

# 2. Feature Engineering (Calculate Gross Revenue, Net Revenue, and Profit Margin)
df["Gross_Revenue"] = df["Units_Sold"] * df["Unit_Price"]
df["Total_Discount_Amt"] = df["Gross_Revenue"] * df["Discount"]
df["Net_Revenue"] = df["Gross_Revenue"] - df["Total_Discount_Amt"]

# Simulate Cost of Goods Sold (COGS) at 60% of Gross Price to calculate profit
df["COGS"] = (df["Units_Sold"] * df["Unit_Price"] * 0.60).round(2)
df["Profit"] = df["Net_Revenue"] - df["COGS"]

print("\n--- CLEANED DATA OVERVIEW ---")
print(df.isnull().sum())
print("-" * 50)


# -------------------------------------------------------------------------
# STEP 2: ANSWERING BUSINESS QUESTIONS
# -------------------------------------------------------------------------

print("\n=== BUSINESS ANALYSIS REPORT ===\n")

# Q1: What is the total Net Revenue and Profit generated across the entire dataset?
total_revenue = df["Net_Revenue"].sum()
total_profit = df["Profit"].sum()
print(
    f"Q1: Total Net Revenue: ${total_revenue:,.2f} | Total Profit: ${total_profit:,.2f}"
)

# Q2: Which Region generated the highest average Net Revenue per order?
avg_rev_per_region = (
    df.groupby("Region")["Net_Revenue"].mean().sort_values(ascending=False)
)
print(f"\nQ2: Top Region by Avg Revenue:\n{avg_rev_per_region.to_string()}")

# Q3: Which Team_Lead is driving the highest total profit?
profit_per_team = (
    df.groupby("Team_Lead")["Profit"].sum().sort_values(ascending=False)
)
print(f"\nQ3: Total Profit by Team Lead:\n{profit_per_team.to_string()}")

# Q4: What is the average customer rating for each Product Category?
avg_rating_category = (
    df.groupby("Product_Category")["Customer_Rating"]
    .mean()
    .sort_values(ascending=False)
)
print(
    f"\nQ4: Average Customer Rating by Category:\n{avg_rating_category.to_string()}"
)

# Q5: What is the breakdown of total Net Revenue by both Region AND Product Category?
region_category_pivot = df.pivot_table(
    values="Net_Revenue",
    index="Region",
    columns="Product_Category",
    aggfunc="sum",
)
print(f"\nQ5: Net Revenue Matrix (Region x Category):\n{region_category_pivot.round(2)}")

# Q6: High-Value Orders: How many orders generated more than $2,000 in Net Revenue?
high_value_orders = df[df["Net_Revenue"] > 2000]
print(
    f"\nQ6: Number of High-Value Orders (> $2,000): {high_value_orders.shape[0]}"
)

# Q7: What is the average discount percentage offered by each Team Lead?
avg_discount_team = (
    df.groupby("Team_Lead")["Discount"].mean().sort_values(ascending=False) * 100
)
print(
    f"\nQ7: Average Discount Offered by Team Lead (%):\n{avg_discount_team.round(2).to_string()}"
)

# Q8: Which month/day_of_week performed the best? (Time-series aggregation)
df["Day_of_Week"] = df["Date"].dt.day_name()
weekly_performance = (
    df.groupby("Day_of_Week")["Net_Revenue"].sum().sort_values(ascending=False)
)
print(f"\nQ8: Total Net Revenue by Day of Week:\n{weekly_performance.to_string()}")
