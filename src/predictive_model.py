import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib  # <-- NEW: Used to save the model
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')

def run_model():
    print("--- TRAINING PREDICTIVE MODEL ---")
    df_train = pd.read_csv(os.path.join(DATA_DIR, 'historical_sales.csv'))
    
    X_train = df_train[['Population', 'Avg_Income', 'Competitors']]
    y_train = df_train['Annual_Sales']
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # --- NEW: SAVE THE MODEL ---
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    model_path = os.path.join(OUTPUT_DIR, 'sales_model.pkl')
    joblib.dump(model, model_path)
    print(f"Model successfully saved to {model_path}!")

if __name__ == "__main__":
    run_model()