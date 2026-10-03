# SuperStore Sales Analytics & Dashboard

An end-to-end data analysis, cleaning, and visualization project leveraging **Python** and **Power BI** to uncover revenue trends, profit drivers, regional performance, and customer segment insights across 5,900+ sales transactions (2019–2020).

---

## 📊 Business Key Metrics

* **Total Revenue:** $1,565,804.32
* **Total Profit:** $175,262.11
* **Total Units Sold:** 22,317
* **Total Unique Orders:** 3,003
* **Unique Customers:** 773

---

## 📌 Performance Summary

* **Technology:** Highest profit driver (~$90.4K profit across 4,061 units) due to higher unit margins.
* **Office Supplies:** Highest order volume and revenue (~$643.7K sales, 13,625 units sold).
* **Furniture:** Strong revenue (~$451.5K sales) but lower profit margins (~$10.0K profit) due to higher shipping and category expenses.

---

## 📁 Repository Structure

```text
SuperStore_Sales_Analytics/
├── 01_Data/
│   ├── SuperStore_Sales_DataSet_original.xlsx      # Raw, untouched dataset
│   └── SuperStore_Sales_DataSet_data_cleaning.xlsx # Cleaned dataset
├── 02_Scripts/
│   └── read_data.py                                # Data inspection & ETL script
├── 03_PowerBI/
│   └── SuperStore_Sales_Dashboard.pbix            # Interactive Power BI report
├── README.md                                       # Project documentation
└── requirements.txt                                # Python dependencies
