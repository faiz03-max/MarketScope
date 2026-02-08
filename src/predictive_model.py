import pandas as pd
from sklearn.linear_model import LinearRegression
import os

# CONFIG
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')

def run_model():
    print("--- TRAINING PREDICTIVE MODEL ---")
    
    # 1. Load Data
    df_train = pd.read_csv(os.path.join(DATA_DIR, 'historical_sales.csv'))
    df_new = pd.read_csv(os.path.join(DATA_DIR, 'new_locations.csv'))
    
    # 2. Train Model (Linear Regression)
    # X = Features (Population, Income, Competitors)
    # y = Target (Sales)
    X_train = df_train[['Population', 'Avg_Income', 'Competitors']]
    y_train = df_train['Annual_Sales']
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    print(f"Model Trained! Coefficient (Impact of Income): {model.coef_[1]:.2f}")
    
    # 3. Predict Sales for New Locations
    print("Predicting sales for new cities...")
    X_new = df_new[['Population', 'Avg_Income', 'Competitors']]
    predictions = model.predict(X_new)
    
    df_new['Projected_Sales'] = predictions.round(2)
    
    # 4. Save Results for "What-If" Analysis
    # We add a column for "Rent_Scenario" to simulate costs later in Power BI/Excel
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    output_path = os.path.join(OUTPUT_DIR, 'final_projections.csv')
    df_new.to_csv(output_path, index=False)
    
    print(f"Projections saved to {output_path}")
    print(df_new)

if __name__ == "__main__":
    run_model()