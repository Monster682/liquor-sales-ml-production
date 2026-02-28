# ===============================
# STEP 7 - MODEL TRAINING
# ===============================

import pandas as pd
import numpy as np
import os
import json
from datetime import datetime

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib

# ---------------------------------
# 1. Load Feature Dataset
# ---------------------------------

df = pd.read_csv("data/feature_data.csv")

print("Feature dataset loaded")

# ---------------------------------
# 2. Define Features & Target
# ---------------------------------

X = df.drop("net_profit", axis=1)
y = df["net_profit"]

# Keep numeric columns only
X = X.select_dtypes(include=[np.number])

# ---------------------------------
# 3. Train-Test Split
# ---------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Train-test split completed")

# ---------------------------------
# 4. Define Models
# ---------------------------------

models = {
    "LinearRegression": LinearRegression(),
    "RandomForest": RandomForestRegressor(random_state=42)
}

results = {}

# ---------------------------------
# 5. Train & Evaluate
# ---------------------------------

for name, model in models.items():

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    cv_scores = cross_val_score(
        model, X, y, cv=5, scoring="neg_mean_absolute_error"
    )

    results[name] = {
        "MAE": float(mae),
        "RMSE": float(rmse),
        "CV_MAE": float(-cv_scores.mean())
    }

    print("\nModel:", name)
    print("MAE:", mae)
    print("RMSE:", rmse)
    print("Cross Validation MAE:", -cv_scores.mean())

# ---------------------------------
# 6. Select Best Model
# ---------------------------------

best_model_name = min(results, key=lambda x: results[x]["RMSE"])
best_model = models[best_model_name]

print("\nBest Model:", best_model_name)

# ---------------------------------
# 7. Save Model
# ---------------------------------

os.makedirs("models", exist_ok=True)

joblib.dump(best_model, "models/model_v1.pkl")

# ---------------------------------
# 8. Save Feature Importance
# ---------------------------------

if best_model_name == "RandomForest":
    importance = pd.Series(
        best_model.feature_importances_,
        index=X.columns
    )
    importance.sort_values(ascending=False).to_csv(
        "models/feature_importance.csv"
    )
    print("Feature importance saved")

# ---------------------------------
# 9. Save Model Metadata
# ---------------------------------

model_info = {
    "version": "v1",
    "trained_on": str(datetime.now()),
    "best_model": best_model_name,
    "metrics": results
}

with open("models/model_info.json", "w") as f:
    json.dump(model_info, f, indent=4)

print("\nModel and metadata saved successfully")
print("STEP 7 COMPLETED")