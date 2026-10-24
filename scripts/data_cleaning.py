
"""Clean the sales dataset and prepare it for analysis in Power BI."""

from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "raw" / "sales_data.csv"
OUTPUT = ROOT / "data" / "processed" / "cleaned_sales_data.csv"

OUTPUT.parent.mkdir(parents=True, exist_ok=True)

if not SOURCE.exists():
    SOURCE = ROOT / "data" / "raw" / "sales_data_demo.csv"

if not SOURCE.exists():
    raise FileNotFoundError("No sales dataset found in data/raw/.")

df = pd.read_csv(SOURCE)
df.columns = df.columns.str.strip()

rows_before = len(df)
duplicates_removed = int(df.duplicated().sum())

df = df.drop_duplicates().copy()

# Convert available date columns into datetime format.
for column in ["Order Date", "Ship Date"]:
    if column in df.columns:
        df[column] = pd.to_datetime(df[column], errors="coerce")

# Convert numeric columns safely.
for column in ["Sales", "Quantity", "Discount", "Profit"]:
    if column in df.columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

# Remove records with missing or invalid sales and quantity values.
invalid_rows_removed = 0

if "Sales" in df.columns:
    invalid_sales = df["Sales"].isna() | (df["Sales"] < 0)
    invalid_rows_removed += int(invalid_sales.sum())
    df = df.loc[~invalid_sales].copy()

if "Quantity" in df.columns:
    invalid_quantity = df["Quantity"].isna() | (df["Quantity"] <= 0)
    invalid_rows_removed += int(invalid_quantity.sum())
    df = df.loc[~invalid_quantity].copy()

# Fill missing categorical values with the most frequent value.
for column in ["Segment", "Category", "Region", "Sub-Category"]:
    if column in df.columns and df[column].isna().any():
        mode_values = df[column].mode(dropna=True)
        fill_value = mode_values.iloc[0] if not mode_values.empty else "Unknown"
        df[column] = df[column].fillna(fill_value)

# Fill missing city values.
if "City" in df.columns:
    df["City"] = df["City"].fillna("Unknown")

# Fill missing discounts with the median.
if "Discount" in df.columns and df["Discount"].isna().any():
    median_discount = df["Discount"].median()
    df["Discount"] = df["Discount"].fillna(
        median_discount if pd.notna(median_discount) else 0
    )

# Add useful date columns for reporting.
if "Order Date" in df.columns:
    df["Order Year"] = df["Order Date"].dt.year
    df["Order Month"] = df["Order Date"].dt.to_period("M").astype("string")

# Calculate profit margin safely.
if {"Sales", "Profit"}.issubset(df.columns):
    df["Profit Margin"] = np.where(
        df["Sales"] != 0,
        df["Profit"] / df["Sales"],
        0
    )

df.to_csv(OUTPUT, index=False)

print("\n--- Data Cleaning Summary ---")
print(f"Source file:             {SOURCE.name}")
print(f"Rows before cleaning:    {rows_before:,}")
print(f"Duplicate rows removed:  {duplicates_removed:,}")
print(f"Invalid rows removed:    {invalid_rows_removed:,}")
print(f"Rows after cleaning:     {len(df):,}")
print(f"Total rows removed:      {rows_before - len(df):,}")
print(f"Remaining missing cells: {int(df.isna().sum().sum()):,}")
print(f"Output file:             {OUTPUT}")