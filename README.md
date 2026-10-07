# Indian Retail Superstore - Sales & Profit Analysis

**Data Analyst Portfolio Project** | Created by a Data Analyst Fresher

---

## 📌 Project Summary                           

Welcome to my **Indian Retail Superstore Sales & Profit Analysis** project! 

As an aspiring Data Analyst, I built this end-to-end project to analyze transactional data from an Indian retail chain operating across major cities (Mumbai, Delhi, Bengaluru, Pune, Hyderabad, Kolkata, etc.) in Indian Rupees (₹ - INR).

The main goal of this analysis is to identify why the store generates high gross revenue but suffers from low net profit margins, and to provide actionable business recommendations to improve profitability.

---

## 🛠️ Tools & Technologies Used

- **Programming Language**: Python 3.9+
- **Data Manipulation**: `Pandas`, `NumPy`
- **Data Visualization**: `Matplotlib`, `Seaborn`, `Plotly Express`
- **Interactive Dashboard**: `Streamlit`
- **Version Control**: Git & GitHub

---

## 📊 Key Business Questions Answered

1. **What is the overall financial health of the store?**
   - Total Sales (INR), Total Profit (INR), and Net Profit Margin (%).
2. **Which regions and cities generate the most revenue and profit?**
   - Performance comparison across West, South, North, East, and Central regions.
3. **Which product categories and sub-categories are profitable vs loss-making?**
   - Identifying top performers (e.g., Electronics, Fashion) vs profit-bleeding items.
4. **Does offering higher discounts increase profits or cause losses?**
   - Discount impact analysis evaluating discount rates (0% to 40%).

---

## 💡 Key Business Insights Discovered

- ⚠️ **Discount Trap**: Giving discounts greater than **20%** drastically reduces profit margins and causes over **45%** of orders to incur financial losses.
- 📍 **Top Regions**: West (Mumbai, Pune) and South (Bengaluru, Hyderabad) generated the highest gross sales revenue.
- 📦 **High Profit Margin**: Fashion & Apparel and Electronics contributed the highest overall net profit margin.

---

## 🚀 How to Run This Project Locally

### 1. Prerequisites
Ensure Python is installed on your computer.

### 2. Install Required Packages
```bash
pip install -r requirements.txt
```

### 3. Generate Dataset & Process Analysis Charts
```bash
python generate_and_analyze.py
```

### 4. Run the Streamlit Dashboard
```bash
streamlit run app.py
```
The interactive web app will open automatically in your browser at `http://localhost:8501`!

---

## 📁 Repository Structure

```
superstore_sales_analysis/
├── generate_and_analyze.py      # Python script to generate dataset & export PNG charts
├── app.py                       # Interactive Streamlit dashboard application
├── indian_superstore_data.csv   # Transaction dataset (1,200+ rows)
├── requirements.txt             # Project python dependencies
├── sales_profit_by_region.png   # Regional analysis chart artifact
├── monthly_trend_inr.png        # Monthly trend chart artifact
├── subcategory_profitability.png# Sub-category profitability chart artifact
├── discount_vs_profit_impact.png# Discount impact analysis chart artifact
└── README.md                    # Project documentation
```

---

## 👨‍💻 Author

**Data Analyst Fresher Portfolio**
- **Domain**: Data Analysis, Business Intelligence, Data Visualization
- **GitHub**: [github.com](https://github.com)
