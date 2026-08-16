import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Page Configuration
st.set_page_config(page_title="WMT FP&A Dashboard", page_icon="📊", layout="wide")
st.title("Northstar Retail (WMT) - Executive FP&A Dashboard")
st.markdown("Interactive financial analysis, margin trends, and scenario forecasting.")
st.divider()

# 2. Load the Processed Data
@st.cache_data
def load_data():
    # Because app.py is in the root directory, we use the direct path to data/
    return pd.read_csv("data/processed/wmt_pl_enriched.csv")

df = load_data()
latest_actuals = df[df['FiscalYear'] == 2026].iloc[0]

# 3. Top Row: Key Performance Indicators (KPIs)
st.subheader("FY2026 Performance Snapshot")
col1, col2, col3, col4 = st.columns(4)

col1.metric(label="Revenue ($B)", 
            value=f"${latest_actuals['Revenue']:.2f}", 
            delta=f"{latest_actuals['Revenue_YoY_%']:.2f}% YoY")

col2.metric(label="Gross Profit ($B)", 
            value=f"${latest_actuals['GrossProfit']:.2f}")

col3.metric(label="Operating Income ($B)", 
            value=f"${latest_actuals['OperatingIncome']:.2f}")

col4.metric(label="Operating Margin", 
            value=f"{latest_actuals['OpMargin_%']:.2f}%")

st.divider()

# 4. Middle Section: Visualizing Historical Trends
st.subheader("Historical Volume vs. Efficiency")

fig, ax1 = plt.subplots(figsize=(12, 5))
sns.set_theme(style="whitegrid")

# Revenue Bars
sns.barplot(x='FiscalYear', y='Revenue', data=df, color='steelblue', alpha=0.7, ax=ax1)
ax1.set_ylabel('Revenue ($ Billions)', color='steelblue', fontweight='bold')

# Margin Lines on Secondary Axis
ax2 = ax1.twinx()
sns.lineplot(x=df.index, y='GrossMargin_%', data=df, color='darkorange', marker='o', linewidth=2.5, ax=ax2, label='Gross Margin %')
sns.lineplot(x=df.index, y='OpMargin_%', data=df, color='firebrick', marker='s', linewidth=2.5, ax=ax2, label='Operating Margin %')
ax2.set_ylabel('Margin (%)', color='dimgrey', fontweight='bold')
ax2.grid(False)

st.pyplot(fig)
st.divider()

# 5. Bottom Section: Interactive FY2027 Scenario Simulator
st.subheader("FY2027 Interactive Scenario Simulator")
st.markdown("Adjust the core operational drivers below to instantly model FY2027 P&L outcomes.")

# Create input controls in columns
scen_col1, scen_col2, scen_col3 = st.columns(3)

with scen_col1:
    rev_growth_pct = st.slider("Target Revenue Growth (%)", min_value=-5.0, max_value=15.0, value=4.5, step=0.5)

with scen_col2:
    cogs_margin_pct = st.slider("Target COGS as % of Revenue", min_value=70.0, max_value=80.0, value=75.1, step=0.1)

with scen_col3:
    op_expense_growth = st.slider("Target Operating Expense Growth (%)", min_value=-5.0, max_value=10.0, value=2.0, step=0.5)

# Calculate dynamic projections
proj_rev = latest_actuals['Revenue'] * (1 + (rev_growth_pct / 100))
proj_cogs = proj_rev * (cogs_margin_pct / 100)
proj_gp = proj_rev - proj_cogs

# Operating Expenses = Gross Profit - Operating Income (using FY26 as base)
base_opex = latest_actuals['GrossProfit'] - latest_actuals['OperatingIncome']
proj_opex = base_opex * (1 + (op_expense_growth / 100))
proj_op_inc = proj_gp - proj_opex
proj_op_margin = (proj_op_inc / proj_rev) * 100

# Display Results
st.markdown("### Projected FY2027 Results")
res_col1, res_col2, res_col3 = st.columns(3)
res_col1.metric("Projected Revenue", f"${proj_rev:.2f}B", f"{rev_growth_pct:.1f}%")
res_col2.metric("Projected Operating Income", f"${proj_op_inc:.2f}B")
res_col3.metric("Projected Op Margin", f"{proj_op_margin:.2f}%", f"{(proj_op_margin - latest_actuals['OpMargin_%']):.2f}% vs FY26")