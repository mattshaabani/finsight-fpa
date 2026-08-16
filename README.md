# 📊 FInsight: Automated FP&A Pipeline & Scenario Engine

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25+-red.svg)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458.svg)](https://pandas.pydata.org/)
[![SEC EDGAR](https://img.shields.io/badge/Data-SEC_EDGAR_API-green.svg)](https://www.sec.gov/edgar/sec-api-documentation)

## 🎯 Executive Summary
FInsight is an end-to-end Financial Planning & Analysis (FP&A) data pipeline and interactive dashboard. It bridges the gap between raw financial accounting data and executive decision-making by automating data extraction, calculating margin efficiencies, performing variance analysis, and simulating future financial scenarios.

Instead of relying on static CSV downloads, this project dynamically connects to the **SEC EDGAR API** to parse raw XBRL accounting tags for Walmart (WMT), cleans the data, and feeds it into an interactive web application built for corporate leadership.

## 💡 Business Value & Key Features

*   **Automated Data Extraction:** Built a resilient XBRL parser that pulls 10-K filings directly from the SEC API. It uses a fallback taxonomy mapping system to handle shifting accounting tags (e.g., dynamically mapping `CostOfGoodsAndServicesSold` vs. `CostOfRevenue`).
*   **Financial Feature Engineering:** Transforms raw dollar amounts into critical FP&A KPIs, including YoY Growth Rates, Gross Margins, and Operating Margins. 
*   **Budget vs. Actuals (BvA) Variance Analysis:** Simulates corporate budgeting targets and calculates both absolute ($) and percentage (%) variances to identify operational overruns and margin compression.
*   **Driver-Based Scenario Engine:** An interactive Streamlit dashboard allowing executives to manipulate key operational levers (Revenue Growth, COGS %, Opex Growth) to instantly model FY2027 performance under Base, Bull, and Bear market conditions.

## 🏗️ Architecture & Pipeline

1.  **Extraction (`01_sec_data_pipeline.ipynb`):** REST API calls to SEC EDGAR, JSON parsing, and XBRL taxonomy mapping.
2.  **Transformation (`02_financial_eda.ipynb`):** Pandas-driven data cleaning, margin calculations, and executive visualizations using Seaborn/Matplotlib.
3.  **Variance Testing (`03_variance_analysis.ipynb`):** Budgeting simulations and Favorable/Unfavorable (F/U) variance flagging.
4.  **Forecasting & UI (`app.py`):** Streamlit-powered interactive dashboard for driver-based scenario modeling.

## 🚀 How to Run Locally

**1. Clone the repository**
```bash
git clone [https://github.com/yourusername/finsight-fpa-engine.git](https://github.com/yourusername/finsight-fpa-engine.git)
cd finsight-fpa-engine
```

**2. Create a virtual environment and install dependencies**
```bash
conda create -n finsight python=3.10
conda activate finsight
pip install pandas numpy requests matplotlib seaborn streamlit
```

**3. Run the data pipeline (Optional)**
If you want to pull fresh data from the SEC, run the Jupyter notebooks in the `notebooks/` directory in sequential order.

**4. Launch the Streamlit Dashboard**
```bash
streamlit run app.py
```

## 📂 Repository Structure
```text
├── data/
│   ├── raw/             # Raw JSON payloads from SEC API
│   ├── interim/         # Partially processed WMT data and BvA metrics
│   └── processed/       # Final enriched datasets ready for the dashboard
├── notebooks/
│   ├── 01_sec_data_pipeline.ipynb
│   ├── 02_financial_eda.ipynb
│   ├── 03_variance_analysis.ipynb
│   └── 04_forecasting_scenarios.ipynb
├── app.py               # The main Streamlit dashboard application
└── README.md
```

## 🧠 Future Enhancements
*   Integrate a DCF (Discounted Cash Flow) valuation model into the dashboard.
*   Expand the API pipeline to benchmark WMT against competitors like Target (TGT) or Costco (COST) in real-time.
*   Connect the data outputs to a cloud database (PostgreSQL/Snowflake) instead of local CSVs.