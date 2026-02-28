import subprocess

steps = [
    "step1_load_clean.py",
    "step2_join_data.py",
    "step3_eda.py",
    "step4_kpi.py",
    "step5_profit_calculation.py",
    "step6_feature_engineering.py",
    "step7_modeling.py",
    "step8_business_output.py"
]

for step in steps:
    print(f"Running {step}...")
    subprocess.run(["python", step])