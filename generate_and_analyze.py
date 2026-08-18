import os
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set visual theme
sns.set_theme(style="whitegrid")

def generate_indian_superstore_data():
    """
    Step 1: Generate realistic sample dataset for Indian Retail Superstore
    """
    np.random.seed(42)
    random.seed(42)
    
    n_samples = 1200
    
    # List of Major Indian Cities, States & Regions
    city_state_region = [
        ("Mumbai", "Maharashtra", "West"),
        ("Pune", "Maharashtra", "West"),
        ("Ahmedabad", "Gujarat", "West"),
        ("Delhi", "Delhi NCR", "North"),
        ("Noida", "Uttar Pradesh", "North"),
        ("Lucknow", "Uttar Pradesh", "North"),
        ("Jaipur", "Rajasthan", "North"),
        ("Bengaluru", "Karnataka", "South"),
        ("Chennai", "Tamil Nadu", "South"),
        ("Hyderabad", "Telangana", "South"),
        ("Kolkata", "West Bengal", "East"),
        ("Patna", "Bihar", "East"),
        ("Bhopal", "Madhya Pradesh", "Central"),
        ("Indore", "Madhya Pradesh", "Central")
    ]
    
    # Categories & Sub-Categories with Price Ranges in INR (₹)
    categories_dict = {
        "Electronics": {
            "Smartphones": (10000, 50000),
            "Laptops": (30000, 80000),
            "Headphones": (800, 4000),
            "Smartwatches": (2000, 10000)
        },
        "Fashion & Apparel": {
            "Men's Clothing": (600, 3000),
            "Women's Clothing": (800, 4000),
            "Footwear": (1000, 5000),
            "Ethnic Wear": (1200, 7000)
        },
        "Home & Kitchen": {
            "Cookware": (1000, 4000),
            "Furniture": (5000, 20000),
            "Home Decor": (500, 3000),
            "Appliances": (3000, 18000)
        },
        "Grocery & Essentials": {
            "Packaged Food": (100, 1000),
            "Personal Care": (150, 1200),
            "Beverages": (80, 600)
        }
    }
    
    segments = ["Consumer", "Corporate", "Small Business"]
    ship_modes = ["Standard Class", "Second Class", "First Class", "Same Day"]
    
    start_date = pd.to_datetime("2024-01-01")
    end_date = pd.to_datetime("2025-12-31")
    
    data = []
    
    for i in range(1, n_samples + 1):
        order_id = f"IND-2025-{1000 + i}"
        days_offset = random.randint(0, (end_date - start_date).days)
        order_date = start_date + pd.Timedelta(days=days_offset)
        
        loc = random.choice(city_state_region)
        city, state, region = loc[0], loc[1], loc[2]
        
        cat = random.choice(list(categories_dict.keys()))
        sub_cat = random.choice(list(categories_dict[cat].keys()))
        min_p, max_p = categories_dict[cat][sub_cat]
        
        unit_price = round(random.uniform(min_p, max_p), 2)
        quantity = random.randint(1, 6)
        
        # Discount percentages
        discount = random.choice([0.0, 0.05, 0.10, 0.15, 0.20, 0.30, 0.40])
        
        gross_sales = round(unit_price * quantity, 2)
        sales_after_discount = round(gross_sales * (1 - discount), 2)
        
        # Profit Margin logic
        margin_base = {
            "Electronics": random.uniform(0.12, 0.20),
            "Fashion & Apparel": random.uniform(0.25, 0.40),
            "Home & Kitchen": random.uniform(0.15, 0.28),
            "Grocery & Essentials": random.uniform(0.08, 0.15)
        }[cat]
        
        # Discounts greater than 20% hurt profit margins
        effective_margin = margin_base - (discount * 1.2)
        profit = round(sales_after_discount * effective_margin, 2)
        
        customer_name = f"Customer_{random.randint(100, 999)}"
        segment = random.choice(segments)
        ship_mode = random.choice(ship_modes)
        
        data.append({
            "OrderID": order_id,
            "OrderDate": order_date.strftime("%Y-%m-%d"),
            "CustomerName": customer_name,
            "Segment": segment,
            "City": city,
            "State": state,
            "Region": region,
            "ShipMode": ship_mode,
            "Category": cat,
            "SubCategory": sub_cat,
            "UnitPrice": unit_price,
            "Quantity": quantity,
            "Discount": discount,
            "GrossSales": gross_sales,
            "Sales": sales_after_discount,
            "Profit": profit
        })
        
    df = pd.DataFrame(data)
    csv_path = "indian_superstore_data.csv"
    df.to_csv(csv_path, index=False)
    print(f"[SUCCESS] Dataset generated: {csv_path} ({len(df)} rows)")
    return df

def analyze_and_export_charts(df):
    """
    Step 2: Perform Data Analysis & Save Visual Graphs
    """
    df["OrderDate"] = pd.to_datetime(df["OrderDate"])
    df["YearMonth"] = df["OrderDate"].dt.to_period("M").astype(str)
    
    # Financial Metrics Calculation
    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    profit_margin = (total_profit / total_sales) * 100
    total_orders = df["OrderID"].nunique()
    loss_orders = len(df[df["Profit"] < 0])
    
    print("\n==========================================")
    print("      INDIAN SUPERSTORE DATA SUMMARY      ")
    print("==========================================")
    print(f"Total Sales (INR): INR {total_sales:,.2f}")
    print(f"Total Profit (INR): INR {total_profit:,.2f}")
    print(f"Overall Profit Margin: {profit_margin:.2f}%")
    print(f"Total Orders: {total_orders}")
    print(f"Loss-Making Orders: {loss_orders} ({(loss_orders/len(df))*100:.1f}%)")
    print("==========================================\n")
    
    # Chart 1: Sales & Profit by Region
    plt.figure(figsize=(10, 5))
    region_summary = df.groupby("Region")[["Sales", "Profit"]].sum().reset_index()
    x = np.arange(len(region_summary["Region"]))
    width = 0.35
    
    plt.bar(x - width/2, region_summary["Sales"] / 1e5, width, label="Sales (Lakh INR)", color="#2b5c8f")
    plt.bar(x + width/2, region_summary["Profit"] / 1e5, width, label="Profit (Lakh INR)", color="#27ae60")
    plt.xticks(x, region_summary["Region"])
    plt.title("Regional Sales vs Profit (Lakh INR)", fontsize=13, fontweight="bold")
    plt.ylabel("Amount in Lakh INR")
    plt.legend()
    plt.tight_layout()
    plt.savefig("sales_profit_by_region.png", dpi=300)
    plt.close()
    print("[CHART SAVED] sales_profit_by_region.png")
    
    # Chart 2: Monthly Sales & Profit Trend
    plt.figure(figsize=(11, 5))
    monthly = df.groupby("YearMonth")[["Sales", "Profit"]].sum().reset_index()
    plt.plot(monthly["YearMonth"], monthly["Sales"] / 1e5, marker="o", color="#2b5c8f", linewidth=2, label="Sales (Lakh INR)")
    plt.plot(monthly["YearMonth"], monthly["Profit"] / 1e5, marker="s", color="#27ae60", linewidth=2, label="Profit (Lakh INR)")
    plt.xticks(rotation=45)
    plt.title("Monthly Sales & Profit Trend (2024 - 2025)", fontsize=13, fontweight="bold")
    plt.ylabel("Amount in Lakh INR")
    plt.legend()
    plt.tight_layout()
    plt.savefig("monthly_trend_inr.png", dpi=300)
    plt.close()
    print("[CHART SAVED] monthly_trend_inr.png")
    
    # Chart 3: Sub-Category Profitability
    plt.figure(figsize=(11, 6))
    subcat = df.groupby("SubCategory")["Profit"].sum().sort_values().reset_index()
    colors = ["#e74c3c" if p < 0 else "#27ae60" for p in subcat["Profit"]]
    
    plt.barh(subcat["SubCategory"], subcat["Profit"] / 1e3, color=colors)
    plt.title("Sub-Category Profitability (Thousand INR)", fontsize=13, fontweight="bold")
    plt.xlabel("Profit (Thousand INR)")
    plt.axvline(0, color="black", linestyle="--")
    plt.tight_layout()
    plt.savefig("subcategory_profitability.png", dpi=300)
    plt.close()
    print("[CHART SAVED] subcategory_profitability.png")
    
    # Chart 4: Discount vs Profit
    plt.figure(figsize=(9, 5))
    disc = df.groupby("Discount")["Profit"].mean().reset_index()
    plt.plot(disc["Discount"] * 100, disc["Profit"], marker="o", color="#8e44ad", linewidth=2)
    plt.axhline(0, color="red", linestyle="--", label="Loss Threshold")
    plt.title("Impact of Discount % on Average Profit per Order", fontsize=13, fontweight="bold")
    plt.xlabel("Discount (%)")
    plt.ylabel("Average Profit per Order (INR)")
    plt.legend()
    plt.tight_layout()
    plt.savefig("discount_vs_profit_impact.png", dpi=300)
    plt.close()
    print("[CHART SAVED] discount_vs_profit_impact.png")

if __name__ == "__main__":
    df = generate_indian_superstore_data()
    analyze_and_export_charts(df)
