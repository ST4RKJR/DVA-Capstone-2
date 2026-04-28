# Data Dictionary

This document describes the dataset used in the e-commerce analysis project.

---

## Dataset Overview

- Source: UCI Online Retail Dataset  
- Type: Transactional Data  
- Records: ~500,000+ rows  
- Format: CSV  

---

## Column Definitions

| Column Name   | Data Type | Description |
|--------------|----------|------------|
| Invoice       | String   | Unique transaction identifier |
| StockCode     | String   | Product/item code |
| Description   | String   | Product description |
| Quantity      | Integer  | Number of items purchased |
| InvoiceDate   | DateTime | Date and time of transaction |
| Price         | Float    | Price per unit of product |
| Customer ID   | Integer  | Unique identifier for each customer |
| Country       | String   | Country where the customer is located |

---

## Engineered Features

| Column Name   | Description |
|--------------|------------|
| TotalPrice    | Total transaction value (Quantity × Price) |
| Year          | Year extracted from InvoiceDate |
| Month         | Month extracted from InvoiceDate |
| Day           | Day extracted from InvoiceDate |

---

## Data Quality Issues Identified

- Missing values in Customer ID  
- Negative quantities indicating returns  
- Invalid or zero pricing values  
- Duplicate transaction records  

---

## Data Cleaning Summary

- Removed rows with missing Customer ID  
- Removed duplicate records  
- Filtered out negative quantities  
- Removed invalid pricing values  
- Created new features for analysis  

---