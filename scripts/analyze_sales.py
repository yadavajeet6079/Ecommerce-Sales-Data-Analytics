
"""Perform exploratory data analysis and generate sales visualizations."""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Project paths
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed" / "cleaned_sales_data.csv"
OUT = ROOT / "visualizations"
OUT.mkdir(parents=True, exist_ok=True)

# Load cleaned dataset
df = pd.read_csv(DATA)

# Required columns for analysis
required_columns = [
    "Category",
    "Sub_Category",
    "Region",
    "Sales",
    "Quantity",
    "Discount",
    "Profit",
]

missing_columns = [col for col in required_columns if col not in df.columns]

if missing_columns:
    raise ValueError(f"Required columns are missing: {missing_columns}")

# Convert numerical columns safely
numeric_columns = ["Sales", "Quantity", "Discount", "Profit"]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

df = df.dropna(subset=numeric_columns)

# Dataset overview
print("\n--- Dataset Shape ---")
print(df.shape)

print("\n--- Data Types ---")
print(df.dtypes)

print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\n--- Descriptive Statistics ---")
print(df[numeric_columns].describe().round(2))

print("\n--- Sales by Category ---")
print(
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .round(2)
)

print("\n--- Profit by Region ---")
print(
    df.groupby("Region")["Profit"]
    .sum()
    .sort_values(ascending=False)
    .round(2)
)

print("\n--- Correlation Matrix ---")
print(df[numeric_columns].corr().round(2))

# Prepare data for visualizations
category_sales = df.groupby("Category")["Sales"].sum().sort_values()
region_profit = df.groupby("Region")["Profit"].sum().sort_values()
subcategory_sales = (
    df.groupby("Sub_Category")["Sales"]
    .sum()
    .nlargest(10)
    .sort_values()
)
region_sales = df.groupby("Region")["Sales"].sum().sort_values()
category_profit = df.groupby("Category")["Profit"].sum().sort_values()

# Define six visualizations
charts = [
    (
        "category_sales.png",
        category_sales,
        "Sales by Category",
        "Sales",
        "barh",
    ),
    (
        "profit_by_region.png",
        region_profit,
        "Profit by Region",
        "Profit",
        "bar",
    ),
    (
        "top_subcategories.png",
        subcategory_sales,
        "Top 10 Sub-Categories by Sales",
        "Sales",
        "barh",
    ),
    (
        "region_sales.png",
        region_sales,
        "Sales by Region",
        "Sales",
        "bar",
    ),
    (
        "category_profit.png",
        category_profit,
        "Profit by Category",
        "Profit",
        "barh",
    ),
]

for filename, series, title, ylabel, chart_type in charts:
    fig, ax = plt.subplots(figsize=(9, 5))

    series.plot(kind=chart_type, ax=ax)

    ax.set_title(title, fontsize=14, fontweight="bold")
    ax.set_xlabel(ylabel if chart_type == "barh" else "Category / Region")
    ax.set_ylabel("Category / Region" if chart_type == "barh" else ylabel)

    plt.tight_layout()
    plt.savefig(OUT / filename, dpi=160, bbox_inches="tight")
    plt.close(fig)

# Sixth chart: Sales vs Profit
fig, ax = plt.subplots(figsize=(9, 5))

ax.scatter(df["Sales"], df["Profit"], alpha=0.5)
ax.set_title("Sales vs Profit", fontsize=14, fontweight="bold")
ax.set_xlabel("Sales")
ax.set_ylabel("Profit")

plt.tight_layout()
plt.savefig(OUT / "sales_vs_profit.png", dpi=160, bbox_inches="tight")
plt.close(fig)

print(f"\nSix visualizations saved in: {OUT}")
print("\nEDA completed successfully!")