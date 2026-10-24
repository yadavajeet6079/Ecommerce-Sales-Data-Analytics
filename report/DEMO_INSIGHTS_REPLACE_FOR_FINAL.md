# Demo Findings — Replace After Loading Public Dataset

**These findings are calculated from the included simulated practice dataset, not from a real company. Do not submit them as the final dataset's findings.**

- Technology is the largest sales category in the demo dataset.
- West records the highest total profit among regions in the demo dataset.
- Central is the lowest-profit region and should be reviewed for product mix, discounts and operating costs.
- Consumer contributes the largest share of sales by customer segment.
- 213 order-line records have negative profit; these are candidates for margin review.
- The correlation between discount and profit is -0.18; treat this as an association, not proof that discounts cause profit changes.

## Recommendation templates
- Review discount levels and profit margin by category and sub-category before expanding promotions; use controlled tests to measure incremental profit.
- Investigate the Central region's low profit using product mix, shipping mode, discount and customer-segment filters; set a margin improvement target after validation.

After running the notebook on the public Sample Superstore CSV, replace this file with at least five observations and two recommendations supported by your own calculated results.
