    # ============================================================
# RETAIL SALES ANALYSIS & CUSTOMER SEGMENTATION DASHBOARD
# ============================================================

# Import required libraries
import streamlit as st
import pandas as pd
import plotly
import plotly.express as px

import os

# ------------------------------------------------------------
# Page configuration
# ------------------------------------------------------------
st.set_page_config(
    page_title="Retail Sales Dashboard",
    layout="wide"
)

# ------------------------------------------------------------
# Load data files
# ------------------------------------------------------------

# Get absolute path of current file (app.py)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define correct data paths
retail_data_path = os.path.join(BASE_DIR, "data", "processed", "cleaned_retail.csv")
customer_data_path = os.path.join(BASE_DIR, "data", "processed", "customer_segments.csv")




# Load datasets
retail_df = pd.read_csv(retail_data_path)
customer_df = pd.read_csv(customer_data_path)

# ------------------------------------------------------------
# Dashboard title and description
# ------------------------------------------------------------
st.title("📊 Retail Sales Analysis & Customer Segmentation Dashboard")

st.markdown("""
This dashboard presents insights from retail transaction data, including:
- Overall sales performance
- Product and customer analysis
- Customer segmentation using K-Means clustering
""")

# ------------------------------------------------------------
# Sidebar filters
# ------------------------------------------------------------
st.sidebar.header("🔎 Filters")

# Country filter
countries = ["All"] + sorted(retail_df["Country"].unique().tolist())
selected_country = st.sidebar.selectbox("Select Country", countries)

# Apply country filter
if selected_country == "All":
    filtered_df = retail_df
else:
    filtered_df = retail_df[retail_df["Country"] == selected_country]

# ------------------------------------------------------------
# KPI Section
# ------------------------------------------------------------

# Calculate KPIs
total_revenue = filtered_df["TotalSales"].sum()
total_customers = filtered_df["CustomerID"].nunique()
total_transactions = filtered_df["InvoiceNo"].nunique()

# Display KPIs in columns
col1, col2, col3 = st.columns(3)

col1.metric("💰 Total Revenue", f"${total_revenue:,.0f}")
col2.metric("👥 Total Customers", total_customers)
col3.metric("🧾 Total Transactions", total_transactions)

# ------------------------------------------------------------
# Monthly Revenue Trend
# ------------------------------------------------------------

# Group sales by month
monthly_sales = (
    filtered_df
    .groupby("Month")["TotalSales"]
    .sum()
    .reset_index()
)

# Line chart for monthly revenue
monthly_fig = px.line(
    monthly_sales,
    x="Month",
    y="TotalSales",
    markers=True,
    title="📈 Monthly Revenue Trend"
)

st.plotly_chart(monthly_fig, use_container_width=True)

# ------------------------------------------------------------
# Top 10 Products by Revenue
# ------------------------------------------------------------

# Calculate top products
top_products = (
    filtered_df
    .groupby("Description")["TotalSales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

# Bar chart for top products
product_fig = px.bar(
    top_products,
    x="TotalSales",
    y="Description",
    orientation="h",
    title="🏆 Top 10 Products by Revenue"
)

st.plotly_chart(product_fig, use_container_width=True)

# ------------------------------------------------------------
# Customer Segmentation Overview
# ------------------------------------------------------------

st.subheader("👥 Customer Segmentation Overview")

# Count customers in each cluster
cluster_counts = (
    customer_df["Cluster"]
    .value_counts()
    .reset_index()
)

cluster_counts.columns = ["Cluster", "CustomerCount"]

# Pie chart for customer segments
cluster_fig = px.pie(
    cluster_counts,
    names="Cluster",
    values="CustomerCount",
    title="Customer Segment Distribution"
)

st.plotly_chart(cluster_fig, use_container_width=True)

# ------------------------------------------------------------
# Customer Segmentation Scatter Plot
# ------------------------------------------------------------

scatter_fig = px.scatter(
    customer_df,
    x="Frequency",
    y="Monetary",
    color="Cluster",
    title="Customer Segmentation (Frequency vs Monetary)",
    labels={
        "Frequency": "Purchase Frequency",
        "Monetary": "Total Spending"
    }
)

st.plotly_chart(scatter_fig, use_container_width=True)

# ------------------------------------------------------------
# Business Insights Section
# ------------------------------------------------------------

st.subheader("📌 Key Business Insights")

st.markdown("""
- A small percentage of customers generate the majority of revenue  
- Sales peak during festive months (November–December)  
- High-value customers have both high purchase frequency and high spending  
- Customer segmentation enables targeted marketing strategies  
""")

# ------------------------------------------------------------
# Footer
# ------------------------------------------------------------
st.markdown("---")
st.markdown("Built using **Python, Pandas, Plotly, and Streamlit** 🚀")
