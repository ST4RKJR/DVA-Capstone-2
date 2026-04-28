# 📊 Online Retail II — Sales & Customer Analytics

End-to-end data analytics project analyzing customer behavior and revenue drivers in an e-commerce dataset using Python and Tableau.

---

## 🚀 Project Overview

This project analyzes transactional data from a UK-based online retailer (2009–2011) to uncover:

- Revenue trends  
- Customer purchasing behavior  
- Top-performing products and regions  
- Business growth opportunities  

Pipeline followed:
**Data Sourcing → ETL → EDA → Statistical Analysis → Dashboard → Insights**

---

## 🎯 Problem Statement

To analyze customer purchasing behavior and sales performance in an e-commerce dataset to:

- Identify key revenue drivers  
- Improve customer retention  
- Support data-driven business decisions  

---

## 📂 Dataset

- **Source:** UCI Machine Learning Repository  
- **Dataset:** Online Retail II  
- **Records:** ~1M+ rows  
- **Columns:** 8 → 11 (after feature engineering)  
- **Countries:** 43  

### Key Columns:
- Invoice  
- StockCode  
- Description  
- Quantity  
- InvoiceDate  
- Price  
- Customer ID  
- Country  

---

## ⚙️ Tech Stack

- Python (Pandas, NumPy, Matplotlib, Seaborn)  
- Jupyter Notebook  
- Tableau Public  
- Git & GitHub  

---

## 🔄 ETL & Data Cleaning

Performed in `notebooks/cleaning.ipynb`

### Steps:
- Removed cancelled invoices  
- Dropped missing Customer IDs  
- Removed negative/zero values  
- Converted InvoiceDate to datetime  
- Created new features:
  - Month  
  - Day  
  - Hour  
  - TotalPrice  

---

## 📊 KPI Framework

| KPI | Value |
|-----|------|
| Total Revenue | $17.4M |
| Total Orders | 36,969 |
| Unique Customers | 5,878 |
| Avg Order Value | $469 |
| Top Country | UK (~80%) |

---

## 📈 Key Insights

- UK contributes ~80% of total revenue  
- November is the peak sales month  
- Orders peak between 10 AM – 12 PM  
- Few products drive majority of revenue  
- Netherlands & EIRE show growth potential  

---

## 📊 Tableau Dashboard

🔗 **Live Dashboard:**  
https://public.tableau.com/views/OnlineRetail_SalesAnalytics/Dashboard1

### Features:
- KPI cards (Revenue, Orders, Customers, AOV)  
- Revenue trend  
- Top countries & products  
- Shopping hours analysis  
- Interactive filters (Country, Month)  

---

## 📁 Project Structure
DVA-Capstone-2/
│
├── data/
│ ├── raw/
│ └── processed/
│
├── notebooks/
│ ├── cleaning.ipynb
│ ├── eda.ipynb
│ ├── statistical_analysis.ipynb
│ └── final_load_prep.ipynb
│
├── tableau/
│ ├── screenshots/
│ └── dashboard_links.md
│
├── reports/
│ ├── project_report.pdf
│ └── presentation.pptx
│
├── docs/
│ └── data_dictionary.md
│
├── scripts/
│ └── etl_pipeline.py
│
└── README.md


---

## 💡 Business Recommendations

- Launch early Q4 campaigns  
- Expand into European markets  
- Optimize marketing timing (10–12 PM)  
- Maintain stock for top products  
- Improve customer retention  

---

## 📈 Impact

Estimated revenue uplift:
**$1.15M – $1.35M annually**

---

## 👨‍💻 Author

**Sahil Singh**  
B.Tech CSE (AI/ML)  
Newton School of Technology, Pune  

---

## ⭐ Highlights

- End-to-end analytics pipeline  
- Real-world dataset (1M+ records)  
- Business-focused insights  
- Interactive dashboard  

---