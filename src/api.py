from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import os

# 1. Initialize the API app
app = FastAPI(title="MarketScope AI Predictor", version="1.0")

# 2. Load the saved model
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'output', 'sales_model.pkl')

# Load the model into memory when the API starts
model = joblib.load(MODEL_PATH)

# 3. Define what data the user MUST send (Data Validation)
class CityData(BaseModel):
    Population: int
    Avg_Income: int
    Competitors: int

# 4. Create the Prediction Endpoint
@app.post("/predict")
def predict_sales(data: CityData):
    # Convert user JSON input into a pandas DataFrame (what the model expects)
    input_df = pd.DataFrame([data.dict()])
    
    # Make the prediction
    prediction = model.predict(input_df)[0]
    
    # Return a clean JSON response
    return {
        "Status": "Success",
        "Input_Data": data.dict(),
        "Projected_Annual_Sales_USD": round(prediction, 2)
    }