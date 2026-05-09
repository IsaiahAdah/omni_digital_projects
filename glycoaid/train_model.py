# ============================================================
# GLYCOAID - DIABETES RISK PREDICTION SYSTEM
# File: train_model.py
# Description: Loads the diabetes dataset directly from GitHub,
#              cleans the data, performs EDA, trains Logistic
#              Regression and Decision Tree models, compares
#              their performance, and saves the best model.
# ============================================================

import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


# ============================================================
# STEP 1: LOAD DATASET DIRECTLY FROM GITHUB URL
# ============================================================

URL = "https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv"

print("=== Loading Dataset from GitHub ===")
data = pd.read_csv(URL)

print(f"Dataset loaded successfully!")
print(f"Shape  : {data.shape}")
print(f"Columns: {list(data.columns)}")
print("\nFirst 5 rows:")
print(data.head())


# ============================================================
# STEP 2: EXPLORATORY DATA ANALYSIS (EDA)
# ============================================================

print("\n=== Exploratory Data Analysis ===")
print("\nDataset Info:")
print(data.info())

print("\nStatistical Summary:")
print(data.describe())

print("\nMissing Values:")
print(data.isnull().sum())

print("\nTarget Distribution (Outcome):")
print(data["Outcome"].value_counts())
print(f"  0 = No Diabetes : {data['Outcome'].value_counts()[0]} patients")
print(f"  1 = Diabetes     : {data['Outcome'].value_counts()[1]} patients")


# ============================================================
# STEP 3: HANDLE MISSING AND INVALID VALUES
# In this dataset, zeros in medical columns are biologically
# impossible and represent missing data that was recorded as 0.
# We replace them with the column median.
# ============================================================

print("\n=== Handling Invalid Zero Values ===")

# These columns cannot biologically be zero
cols_with_invalid_zeros = [
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI"
]

for col in cols_with_invalid_zeros:
    zero_count = (data[col] == 0).sum()
    if zero_count > 0:
        median_value = data[col].replace(0, np.nan).median()
        data[col]    = data[col].replace(0, median_value)
        print(f"  {col}: replaced {zero_count} zero(s) with median ({round(median_value, 2)})")

print("\nData after cleaning:")
print(data.describe())


# ============================================================
# STEP 4: SET INPUT (X) AND OUTPUT (y)
# ============================================================

X = data.drop("Outcome", axis=1)
y = data["Outcome"]

print(f"\nFeatures (X) shape : {X.shape}")
print(f"Target (y) shape   : {y.shape}")


# ============================================================
# STEP 5: TRAIN AND TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

print(f"\n=== Train/Test Split ===")
print(f"Training samples : {len(X_train)}")
print(f"Testing samples  : {len(X_test)}")


# ============================================================
# STEP 6: SCALE THE FEATURES
# Logistic Regression performs better when features are
# on the same scale. StandardScaler standardises each feature
# to have mean=0 and standard deviation=1.
# Decision Trees do not require scaling but we apply it
# consistently for fair comparison.
# ============================================================

scaler  = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)


# ============================================================
# STEP 7: TRAIN MODEL 1 - LOGISTIC REGRESSION
# ============================================================

print("\n=== Training Model 1: Logistic Regression ===")

lr_model = LogisticRegression(random_state=42, max_iter=1000)
lr_model.fit(X_train_scaled, y_train)

lr_pred     = lr_model.predict(X_test_scaled)
lr_accuracy = accuracy_score(y_test, lr_pred)

print(f"Logistic Regression Accuracy: {round(lr_accuracy * 100, 2)}%")
print("\nClassification Report:")
print(classification_report(y_test, lr_pred,
      target_names=["No Diabetes", "Diabetes"]))


# ============================================================
# STEP 8: TRAIN MODEL 2 - DECISION TREE CLASSIFIER
# ============================================================

print("\n=== Training Model 2: Decision Tree Classifier ===")

dt_model = DecisionTreeClassifier(random_state=42, max_depth=5)
dt_model.fit(X_train_scaled, y_train)

dt_pred     = dt_model.predict(X_test_scaled)
dt_accuracy = accuracy_score(y_test, dt_pred)

print(f"Decision Tree Accuracy: {round(dt_accuracy * 100, 2)}%")
print("\nClassification Report:")
print(classification_report(y_test, dt_pred,
      target_names=["No Diabetes", "Diabetes"]))


# ============================================================
# STEP 9: COMPARE MODEL PERFORMANCE
# ============================================================

print("\n=== Model Comparison ===")
print(f"{'Model':<30} {'Accuracy':<15}")
print("-" * 45)
print(f"{'Logistic Regression':<30} {round(lr_accuracy * 100, 2)}%")
print(f"{'Decision Tree Classifier':<30} {round(dt_accuracy * 100, 2)}%")

# Select the best model
if lr_accuracy >= dt_accuracy:
    best_model      = lr_model
    best_model_name = "Logistic Regression"
    best_accuracy   = lr_accuracy
else:
    best_model      = dt_model
    best_model_name = "Decision Tree Classifier"
    best_accuracy   = dt_accuracy

print(f"\nBest Model: {best_model_name} with {round(best_accuracy * 100, 2)}% accuracy")


# ============================================================
# STEP 10: SAVE THE BEST MODEL AND SCALER USING JOBLIB
# ============================================================

joblib.dump(best_model, "model.pkl")
joblib.dump(scaler,     "scaler.pkl")

print("\n=== Files Saved Successfully ===")
print("  - model.pkl  (trained model)")
print("  - scaler.pkl (feature scaler)")


# ============================================================
# STEP 11: TEST WITH A SAMPLE PREDICTION
# ============================================================

print("\n=== Sample Prediction Test ===")

sample = pd.DataFrame([[
    6, 148, 72, 35, 0, 33.6, 0.627, 50
]], columns=X.columns)

sample_scaled  = scaler.transform(sample)
prediction     = best_model.predict(sample_scaled)[0]
probability    = best_model.predict_proba(sample_scaled)[0]

result = "High Risk of Diabetes" if prediction == 1 else "Low Risk of Diabetes"
risk_percent = round(probability[1] * 100, 2)

print(f"Input       : Pregnancies=6, Glucose=148, BP=72, Skin=35, Insulin=0, BMI=33.6, DPF=0.627, Age=50")
print(f"Prediction  : {result}")
print(f"Risk Score  : {risk_percent}%")
