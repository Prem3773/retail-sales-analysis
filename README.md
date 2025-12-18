📊 Retail Sales Data Analysis & Customer Segmentation
📌 Project Overview

This project performs end-to-end retail sales data analysis on a real-world e-commerce dataset to understand sales performance, customer behavior, and revenue contribution.
It also applies machine learning (K-Means clustering) to segment customers and presents insights through an interactive Streamlit dashboard.

🎯 Business Objectives

Analyze overall sales and revenue trends

Identify top-performing products and customers

Understand customer purchase behavior

Segment customers for targeted marketing strategies

Deploy insights through an interactive dashboard

📂 Dataset

Source: Kaggle – Online Retail Dataset

Records: 540,000+ transactions

Type: Real UK-based e-commerce data

Key Columns:

InvoiceNo – Transaction ID

CustomerID – Customer identifier

Description – Product name

Quantity – Units sold

UnitPrice – Price per unit

InvoiceDate – Date of purchase

Country – Customer location

🛠️ Tools & Technologies Used

Python

Pandas & NumPy – Data cleaning and manipulation

Matplotlib & Seaborn – Exploratory analysis

Scikit-learn – K-Means clustering

Plotly – Interactive visualizations

Streamlit – Dashboard development

Git & GitHub – Version control

🔄 Project Workflow
1️⃣ Data Cleaning

Removed missing customer IDs

Handled returns and invalid values

Fixed date formats (day-first parsing)

Created derived features like TotalSales

2️⃣ Exploratory Data Analysis (EDA)

Revenue and transaction KPIs

Monthly and yearly sales trends

Top products and customers

Pareto (80/20) revenue analysis

3️⃣ Customer Segmentation

Converted transactional data to customer-level data

Used Frequency and Monetary value

Applied StandardScaler

Used Elbow Method to find optimal clusters

Implemented K-Means clustering

4️⃣ Dashboard & Deployment

Built an interactive Streamlit dashboard

Added KPIs, charts, filters, and segmentation views

Prepared project for cloud deployment

📊 Key Insights

A small percentage of customers contribute the majority of revenue

Sales peak during festive months (November–December)

Few products dominate overall sales

Customer segmentation helps identify high-value customers for loyalty programs

🚀 Live Dashboard

🔗 (Add your Streamlit Cloud link here after deployment)
Example:

https://retail-sales-analysis.streamlit.app

📁 Project Structure
retail-sales-analysis/
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   └── 03_customer_segmentation.ipynb
│
├── app/
│   └── app.py
│
├── data/
│   ├── raw/
│   │   └── online_retail.csv
│   └── processed/
│       ├── cleaned_retail.csv
│       └── customer_segments.csv
│
├── requirements.txt
├── README.md
└── .gitignore

▶️ How to Run Locally
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Run Streamlit dashboard
cd app
python -m streamlit run app.py

🙌 Author

Prem Rajpure
Data Analyst | Python | Machine Learning | Data Visualization

⭐ If you like this project

Give it a ⭐ on GitHub and feel free to fork or improve it!
