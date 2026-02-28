import pandas as pd
import os
import json

# Load your feature dataset
df = pd.read_csv("data/feature_data.csv")

print("Dataset loaded successfully")

# Create folder for reports
os.makedirs("validation_reports", exist_ok=True)

# 1. Missing values report
missing = df.isnull().sum()
missing.to_csv("validation_reports/missing_values.csv")

# 2. Duplicate rows
duplicates = df.duplicated().sum()

# 3. Save schema (column names + data types)
schema = {col: str(dtype) for col, dtype in df.dtypes.items()}

with open("validation_reports/schema.json", "w") as f:
    json.dump(schema, f, indent=4)

# 4. Save summary
with open("validation_reports/validation_summary.txt", "w") as f:
    f.write(f"Total rows: {len(df)}\n")
    f.write(f"Total columns: {len(df.columns)}\n")
    f.write(f"Duplicate rows: {duplicates}\n")

print("Validation reports created successfully")