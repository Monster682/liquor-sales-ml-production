import pandas as pd
import os
import json

print("Starting drift monitoring...")

train_df = pd.read_csv("data/feature_data.csv")

# For now we simulate new data using same dataset
new_df = pd.read_csv("data/feature_data.csv")

drift_report = {}

for col in train_df.select_dtypes(include="number").columns:
    train_mean = train_df[col].mean()
    new_mean = new_df[col].mean()

    drift = abs(train_mean - new_mean)

    drift_report[col] = {
        "train_mean": float(train_mean),
        "new_mean": float(new_mean),
        "difference": float(drift)
    }

os.makedirs("monitoring", exist_ok=True)

with open("monitoring/drift_report.json", "w") as f:
    json.dump(drift_report, f, indent=4)

print("Drift report generated successfully")