# SuperStore Sales Analytics & Dashboard

An end-to-end data analytics and business intelligence project analyzing **5,900+ sales transactions** from a U.S. SuperStore dataset (2019–2020). This project covers data inspection, cleaning, exploratory data analysis using **Python**, and interactive dashboard visualization using **Power BI**.

---

## 📌 Executive Summary

* **Total Revenue (Sales):** $1,565,804.32
* **Total Profit:** $175,262.11
* **Total Units Sold:** 22,317
* **Total Unique Orders:** 3,003
* **Unique Customers:** 773

---

## 📊 Key Business Insights

* **Technology:** Primary profit driver (~$90.4K profit across 4,061 units) due to higher margins per unit.
* **Office Supplies:** Highest volume and revenue contributor (~$643.7K sales, 13,625 units sold).
* **Furniture:** Strong revenue generator (~$451.5K sales) but lower net profit margins (~$10.0K profit).

---

## 📁 Repository Structure

```text
SuperStore_Sales_Analytics/
├── 01_Data/
│   ├── SuperStore_Sales_DataSet_original.xlsx      # Raw, untouched dataset
│   └── SuperStore_Sales_DataSet_data_cleaning.xlsx # Processed dataset
├── 02_Scripts/
│   └── read_data.py                                # Data loading & verification script
├── 03_PowerBI/
│   └── SuperStore_Sales_Dashboard.pbix            # Interactive Power BI dashboard
├── README.md                                       # Project documentation
└── requirements.txt                                # Python dependencies
