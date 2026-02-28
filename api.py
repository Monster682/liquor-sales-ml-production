from fastapi import FastAPI
import joblib
import pandas as pd
import os
import logging

app = FastAPI()

# Create logs folder
os.makedirs("logs", exist_ok=True)

# Setup logging (Windows safe)
logging.basicConfig(
    filename="logs/api.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)

# Load trained model
model = joblib.load("models/model_v1.pkl")

@app.get("/")
def home():
    logging.info("Home endpoint called")
    return {"message": "Liquor Sales API Running"}

@app.get("/health")
def health():
    logging.info("Health endpoint called")
    return {"status": "healthy"}

@app.post("/predict")
def predict(data: dict):
    try:
        df = pd.DataFrame([data])

        # Get model expected feature columns
        expected_columns = model.feature_names_in_

        # Add missing columns as 0
        for col in expected_columns:
            if col not in df.columns:
                df[col] = 0

        # Keep only expected columns and correct order
        df = df[expected_columns]

        prediction = model.predict(df)

        logging.info(f"Prediction made: {prediction[0]}")

        return {"predicted_net_profit": float(prediction[0])}

    except Exception as e:
        logging.error(f"Prediction error: {str(e)}")
        return {"error": str(e)}