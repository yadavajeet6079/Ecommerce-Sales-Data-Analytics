# E-commerce Sales Data Analytics

An end-to-end data analytics capstone project covering Git/GitHub workflow, data preparation, exploratory data analysis (EDA), visualization, a Power BI dashboard, business insights, and project presentation.

> **Dataset note:** `data/raw/sales_data_demo.csv` is a simulated practice dataset included so the code runs immediately. For the final assignment, download the public Sample Superstore CSV and save it as `data/raw/sales_data.csv`. The analysis scripts automatically prefer that file when present. Do not describe the demo data as real company data.

## Problem statement
A retail business needs a clear view of sales, profit, customer segments, product categories, regional performance, and changes over time. This project demonstrates how to turn order-level data into practical business reporting.

## Dataset
- **Recommended final dataset:** Sample Superstore (public educational dataset hosted on GitHub).
- **Source:** [SampleSuperstore.csv on GitHub](https://github.com/Wunmi-O/Superstore/blob/master/SampleSuperstore.csv)
- **Fields:** order and ship dates, customer segment, region, category, sub-category, sales, quantity, discount, and profit.
- **Demo file:** `data/raw/sales_data_demo.csv` (simulated data for testing only).

## Tools
- Python, pandas, NumPy
- Matplotlib and Jupyter Notebook
- Power BI Desktop
- Git and GitHub
- PowerPoint and PDF documentation

## Repository structure
```text
data/raw/             Raw source CSV and demo data
data/processed/       Cleaned Power BI-ready dataset
notebooks/            EDA notebook
scripts/              Reusable cleaning and analysis scripts
visualizations/       PNG charts
powerbi/              Dashboard instructions and DAX measures
screenshots/          Final Power BI screenshot
report/               Project report
presentation/         Project presentation
docs/                 Git workflow and submission checklist
```

## Setup
1. Download the Sample Superstore CSV from the source above.
2. Save it as `data/raw/sales_data.csv`.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Clean the data:
   ```bash
   python scripts/data_cleaning.py
   ```
5. Generate charts and summaries:
   ```bash
   python scripts/analyze_sales.py
   ```
6. Open `notebooks/sales_analysis.ipynb` in Jupyter and run all cells.

## Data cleaning process
- Standardize column names by trimming extra spaces.
- Parse order and ship dates as dates.
- Convert numeric fields to numeric types.
- Remove duplicate rows.
- Exclude rows without usable sales/quantity values and invalid negative sales or non-positive quantity.
- Fill missing categorical values using the mode, city with `Unknown`, and discount with its median.
- Add `Order Year`, `Order Month`, and `Profit Margin` fields.

Cleaning decisions should be reviewed against the actual downloaded dataset before submission.

## EDA and visualizations
The notebook includes shape/data types, missing-value and duplicate checks, descriptive statistics, category/region/segment summaries, correlation, IQR-based outlier counts, and charts. Example charts are in `visualizations/`. Regenerate them after switching to the public dataset.

## Power BI dashboard
Follow `powerbi/DASHBOARD_GUIDE.md` to build the `.pbix` file in Power BI Desktop. The `.pbix` itself must be saved from Power BI; it is not generated automatically by this repository.

## Key insights and recommendations
The demo charts can be used to understand the intended analysis flow only. After loading the public dataset, recalculate and replace every result with values from your own run. Then document at least five insights and two recommendations supported by the final data.

## Git workflow
See `docs/GIT_WORKFLOW.md` for a suggested sequence of meaningful commits. Use your own GitHub account and push the project from your computer.

## Deliverables checklist
- [ ] Public Sample Superstore CSV saved to `data/raw/sales_data.csv`
- [ ] Cleaning script run successfully
- [ ] Notebook run top-to-bottom using the public data
- [ ] At least five charts regenerated and checked
- [ ] Power BI `.pbix` saved in `powerbi/`
- [ ] Dashboard screenshot saved in `screenshots/`
- [ ] Five evidence-based insights and two recommendations updated
- [ ] Report and presentation updated with final results
- [ ] At least three meaningful commits pushed to GitHub
