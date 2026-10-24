# Power BI Dashboard Guide

## Import and prepare
1. Open Power BI Desktop.
2. Select **Get data → Text/CSV** and import `data/processed/cleaned_sales_data.csv`.
3. Confirm `Order Date` and `Ship Date` are Date types; `Sales`, `Profit`, `Discount`, and `Quantity` are numeric.
4. Create a date hierarchy if needed. Sort `Order Month` by a date/month key if you create one.

## Suggested layout
**Title:** E-commerce Sales & Profit Overview

**KPI cards (at least 3):**
- Total Sales
- Total Profit
- Total Orders

**Visuals (at least 4):**
- Line chart: Sales by Order Date (month)
- Bar chart: Sales by Category
- Bar chart: Profit by Region
- Column chart: Sales by Sub-Category
- Donut chart: Sales by Segment (optional extra)

**Slicers:** Order Date, Region, Category, Segment.

## DAX measures
```DAX
Total Sales = SUM('cleaned_sales_data'[Sales])

Total Profit = SUM('cleaned_sales_data'[Profit])

Total Orders = DISTINCTCOUNT('cleaned_sales_data'[Order ID])

Total Quantity = SUM('cleaned_sales_data'[Quantity])

Profit Margin % = DIVIDE([Total Profit], [Total Sales], 0)

Average Order Value = DIVIDE([Total Sales], [Total Orders], 0)
```

Change the table name in DAX if Power BI uses a different name.

## Formatting checklist
- Use one consistent theme and readable fonts.
- Use currency formatting for Sales and Profit.
- Use percentage formatting for Profit Margin %.
- Add meaningful titles and axis labels.
- Keep slicers aligned and avoid clutter.
- Test that each slicer filters all relevant visuals.
- Save as `powerbi/Ecommerce_Sales_Dashboard.pbix`.
- Export a screenshot to `screenshots/dashboard.png`.

## Submission note
This repository provides the build guide and measures. You must open Power BI Desktop, build and save the actual `.pbix`, and capture your own screenshot before submission.
