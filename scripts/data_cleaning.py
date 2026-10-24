"""Clean the Superstore-style sales CSV and save a Power BI-ready file.

Run from the repository root:
    python scripts/data_cleaning.py
"""
from pathlib import Path
import pandas as pd
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "data" / "raw" / "sales_data.csv"
if not source.exists():
    source = ROOT / "data" / "raw" / "sales_data_demo.csv"
output = ROOT / "data" / "processed" / "cleaned_sales_data.csv"
output.parent.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(source)
df.columns = [c.strip() for c in df.columns]
for col in ["Order Date", "Ship Date"]:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors="coerce")
for col in ["Sales", "Quantity", "Discount", "Profit"]:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

before = len(df)
df = df.drop_duplicates()
for col in ["Sales", "Quantity"]:
    if col in df.columns:
        df = df[df[col].notna()]
if "Sales" in df.columns:
    df = df[df["Sales"] >= 0]
if "Quantity" in df.columns:
    df = df[df["Quantity"] > 0]
for col in ["Segment", "Category", "Region", "Sub-Category"]:
    if col in df.columns and df[col].isna().any():
        mode = df[col].mode(dropna=True)
        df[col] = df[col].fillna(mode.iloc[0] if not mode.empty else "Unknown")
if "City" in df.columns:
    df["City"] = df["City"].fillna("Unknown")
if "Discount" in df.columns and df["Discount"].isna().any():
    df["Discount"] = df["Discount"].fillna(df["Discount"].median())

if "Order Date" in df.columns:
    df["Order Year"] = df["Order Date"].dt.year
    df["Order Month"] = df["Order Date"].dt.to_period("M").astype(str)
if {"Sales", "Profit"}.issubset(df.columns):
    df["Profit Margin"] = np.where(df["Sales"].ne(0), df["Profit"] / df["Sales"], 0)

df.to_csv(output, index=False)
print(f"Rows before cleaning: {before:,}")
print(f"Rows after cleaning:  {len(df):,}")
print(f"Removed rows:         {before-len(df):,}")
print(f"Saved: {output}")
