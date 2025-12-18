
# 📊 Retail Sales Data Analysis & Customer Segmentation

## 📌 Project Overview
This project demonstrates an **end-to-end retail sales data analysis pipeline** using a real-world e-commerce dataset.  
It focuses on understanding **sales performance, customer behavior, and revenue contribution**, and applies **machine learning (K-Means clustering)** to segment customers.  
Insights are delivered through an **interactive Streamlit dashboard**.

---

## 🎯 Business Objectives
- Analyze overall sales and revenue trends  
- Identify top-performing products and customers  
- Understand customer purchasing behavior  
- Segment customers for targeted marketing strategies  
- Deploy insights through an interactive dashboard  

---

## 📂 Dataset
- **Source:** Kaggle – Online Retail Dataset  
- **Size:** 540,000+ transaction records  
- **Type:** Real UK-based e-commerce data  

### Key Columns
- `InvoiceNo` – Transaction identifier  
- `CustomerID` – Unique customer ID  
- `Description` – Product name  
- `Quantity` – Units sold  
- `UnitPrice` – Price per unit  
- `InvoiceDate` – Date and time of purchase  
- `Country` – Customer country  

---

## 🛠️ Tools & Technologies
- **Python**
- **Pandas, NumPy** – Data cleaning and manipulation  
- **Matplotlib, Seaborn** – Exploratory data analysis  
- **Scikit-learn** – Customer segmentation (K-Means)  
- **Plotly** – Interactive visualizations  
- **Streamlit** – Dashboard development  
- **Git & GitHub** – Version control  

---

## 🔄 Project Workflow

### 1️⃣ Data Cleaning
- Handled missing customer IDs  
- Removed returns and invalid values  
- Fixed inconsistent date formats  
- Created derived features such as `TotalSales`  

### 2️⃣ Exploratory Data Analysis (EDA)
- Revenue and transaction KPIs  
- Monthly and yearly sales trends  
- Top products and customers  
- Pareto (80/20) revenue analysis  

### 3️⃣ Customer Segmentation
- Converted transactional data to customer-level data  
- Engineered Frequency and Monetary features  
- Applied feature scaling  
- Used Elbow Method to find optimal clusters  
- Implemented K-Means clustering  

### 4️⃣ Dashboard & Deployment
- Built an interactive Streamlit dashboard  
- Added KPIs, filters, and visualizations  
- Prepared project for cloud deployment  

---

## 📊 Key Insights
- A small percentage of customers contribute the majority of revenue  
- Sales peak during festive months (November–December)  
- A limited number of products drive most sales  
- Customer segmentation helps identify high-value customers for retention strategies  

---

## 🚀 Live Dashboard
(Add your Streamlit Cloud deployment link here)

Example:
```
https://retail-sales-analysis.streamlit.app
```

---

## 📁 Project Structure
```
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
```

---

## ▶️ How to Run the Project Locally

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Run the Streamlit dashboard
```bash
cd app
python -m streamlit run app.py
```

---

## 📌 Resume Bullet
> Built and deployed an end-to-end retail sales analytics project using Python, Pandas, Scikit-learn, and Streamlit; analyzed 540K+ transactions, applied K-Means customer segmentation, and delivered insights through an interactive dashboard.

---

## 🙌 Author
**Prem Rajpure**  
Aspiring Data Analyst | Python | Machine Learning | Data Visualization  

---

⭐ If you find this project useful, feel free to star the repository and explore further improvements!
