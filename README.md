# MarketScope - Retail Expansion Simulator 📈🏪

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Machine Learning](https://img.shields.io/badge/Model-LinearRegression-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

## 📌 Project Overview
**MarketScope** is a predictive analytics tool designed for **Retail Strategy Consulting**. It helps stakeholders decide where to open new stores by forecasting potential sales based on demographic data.

The project mimics a **Site Selection Analysis**, using a Machine Learning model to predict revenue for prospective locations and allowing for "What-If" scenario planning on profitability.

---

## 💼 Business Scenario
**The Problem:**
A retail chain ("TechGear") wants to expand into 3 new cities but lacks data on which location will yield the highest ROI. Opening a store costs $2M+, making a wrong choice disastrous.

**The Solution:**
A **Predictive Model** that:
1.  **Analyzes** historical sales data from 100 existing stores.
2.  **Identifies** key drivers of revenue (Population, Average Income, Competitor Density).
3.  **Forecasts** annual sales for new candidate cities (Metro City, Suburbia, Rural Town).

---

## 🚀 Key Features
* **Synthetic Data Generation:** Python script that creates a realistic dataset of 100 stores with correlated variables (e.g., Higher Income = Higher Sales).
* **REST API Deployment:** Utilizes FastAPI to serve the trained Machine Learning model, allowing external applications to send JSON demographic data and receive instant sales projections.
* **Predictive Modeling:** Uses `scikit-learn` (Linear Regression) to train a model on historical data.
* **Scenario Output:** Generates a CSV report of projected sales, ready for ingestion into Power BI for "Rent vs. Revenue" stress testing.

---

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Libraries:** `pandas`, `scikit-learn` (Machine Learning), `numpy`
* **IDE:** VS Code

---

## 📂 Project Structure
```text
MarketScope/
│
├── data/                 # Input files (Historical Sales, New Locations)
│
├── output/               # Model Predictions (Final Report)
│   └── final_projections.csv
│
├── src/                  # Source code
│   ├── generate_data.py  # Creates mock historical data
│   ├── predictive_model.py # Trains model & predicts future sales
│
├── requirements.txt      # Python dependencies
└── README.md             # Documentation
