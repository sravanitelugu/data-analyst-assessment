# Data Analyst Technical Assessment

## Project Overview
This repository contains a complete take-home style data analysis project based on a customer purchase and engagement dataset.

The objective was to:
- clean and prepare the data
- perform exploratory data analysis
- identify key business insights
- create supporting visualizations
- provide business recommendations

## Tools Used
- Python
- Pandas
- Matplotlib
- CSV / GitHub-ready folder structure

## Repository Structure
```text
data-analyst-assessment-repo/
├── data/
│   ├── customer_purchase_engagement_raw.csv
│   └── customer_purchase_engagement_cleaned.csv
├── analysis/
│   ├── analysis.py
│   └── assessment_notebook.ipynb
├── visuals/
│   ├── monthly_revenue_trend.png
│   ├── revenue_by_category.png
│   ├── aov_by_channel.png
│   └── weekend_vs_weekday_aov.png
├── dashboard/
│   └── dashboard.html
└── README.md
```

## Data Cleaning Steps
The dataset was prepared by:
- removing rows with missing customer IDs or dates
- standardizing inconsistent category labels
- filling missing marketing channels with `"Unknown"`
- imputing missing numeric values with median values
- removing duplicate transaction records

## Exploratory Analysis Performed
The analysis focused on:
- total revenue
- total orders
- unique customers
- average order value
- revenue by product category
- average order value by marketing channel
- monthly revenue trend
- weekend vs weekday purchase behavior

## Key Findings
1. **Repeat customers drive most of the revenue**  
   Repeat customers contribute **51.3%** of total revenue, which highlights the value of retention and lifecycle marketing.

2. **Weekend orders are more valuable**  
   Average order value is **$188.02** on weekends versus **$171.28** on weekdays. This suggests that customers may be more willing to spend during weekends.

3. **Channel and category performance are uneven**  
   **Paid Search** is the top-performing acquisition channel by revenue, while **Electronics** is the strongest product category. These areas likely deserve more focused investment.

## Business Recommendations
- Invest in **retention campaigns** such as loyalty offers, personalized follow-ups, and re-engagement flows for existing customers.
- Schedule more **high-intent promotions on weekends** when purchase values are highest.
- Double down on the best-performing **marketing channels and product categories** to improve return on acquisition spend.

## Bonus
A lightweight dashboard is included in `dashboard/dashboard.html` to summarize the main KPIs and insights.

## Note
This package includes a **synthetic sample dataset** created for demonstration. If you receive an employer-provided dataset, you can replace the CSV file and rerun the notebook or script with the same workflow.
