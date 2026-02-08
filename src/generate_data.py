import pandas as pd
import random
import os

# CONFIG
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')

def generate_market_data():
    print("--- GENERATING HISTORICAL MARKET DATA ---")
    
    # 1. Create Mock Data for EXISTING Stores (Training Data)
    data = []
    for i in range(100):
        # Logic: Sales are roughly correlated with Income and Population
        pop = random.randint(50000, 500000)
        income = random.randint(40000, 120000)
        competitors = random.randint(0, 10)
        
        # The "Secret Formula" (Ground Truth): 
        # Sales = (Pop * 0.1) + (Income * 5) - (Competitors * 20000) + Random Noise
        sales = (pop * 0.1) + (income * 5) - (competitors * 20000) + random.uniform(-50000, 50000)
        
        data.append({
            "City_ID": i,
            "Population": pop,
            "Avg_Income": income,
            "Competitors": competitors,
            "Annual_Sales": round(sales, 2)
        })

    df_train = pd.DataFrame(data)
    
    # 2. Create Mock Data for NEW POTENTIAL Locations (Prediction Data)
    # These cities don't have sales yet. We need to predict them.
    new_locations = [
        {"City": "Metro City", "Population": 450000, "Avg_Income": 85000, "Competitors": 5},
        {"City": "Suburbia", "Population": 120000, "Avg_Income": 110000, "Competitors": 2},
        {"City": "Rural Town", "Population": 60000, "Avg_Income": 45000, "Competitors": 0},
    ]
    df_new = pd.DataFrame(new_locations)

    # Save to CSV
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
        
    df_train.to_csv(os.path.join(DATA_DIR, 'historical_sales.csv'), index=False)
    df_new.to_csv(os.path.join(DATA_DIR, 'new_locations.csv'), index=False)
    
    print(f"Data saved to {DATA_DIR}")

if __name__ == "__main__":
    generate_market_data()