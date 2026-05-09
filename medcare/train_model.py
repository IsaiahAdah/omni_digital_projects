# ============================================================
# MEDCARE - AI DISEASE PREDICTION SYSTEM
# File: train_model.py
# Description: Loads the dataset, encodes categorical columns,
#              trains a Decision Tree Classifier, evaluates it,
#              and saves all model files using Joblib.
#
# IMPORTANT: Run generate_dataset.py first to create the
#            disease_dataset.csv file before running this.
# Queens Hospital Akure - AI Engineering Team
# ============================================================

import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score


# ============================================================
# STEP 1: LOAD THE DATASET
# ============================================================

data = pd.read_csv("disease_dataset.csv")

print("=== Dataset Preview ===")
print(data.head(10))
print(f"\nDataset Shape  : {data.shape}")
print(f"Columns        : {list(data.columns)}")
print(f"\nDisease Distribution:")
print(data["Disease"].value_counts())


# ============================================================
# STEP 2: ENCODE CATEGORICAL COLUMNS
# Machine learning models only understand numbers.
# LabelEncoder converts text values into integers.
# ============================================================

le_gender     = LabelEncoder()
le_fever      = LabelEncoder()
le_cough      = LabelEncoder()
le_headache   = LabelEncoder()
le_body_pain  = LabelEncoder()
le_disease    = LabelEncoder()

data["Gender"]     = le_gender.fit_transform(data["Gender"])
data["Fever"]      = le_fever.fit_transform(data["Fever"])
data["Cough"]      = le_cough.fit_transform(data["Cough"])
data["Headache"]   = le_headache.fit_transform(data["Headache"])
data["Body_Pain"]  = le_body_pain.fit_transform(data["Body_Pain"])
data["Disease"]    = le_disease.fit_transform(data["Disease"])

print("\n=== Data After Encoding ===")
print(data.head())


# ============================================================
# STEP 3: SET INPUT (X) AND OUTPUT (y)
# X = features the model uses to make a prediction
# y = the answer the model is trying to predict
# ============================================================

X = data[["Age", "Gender", "Fever", "Cough", "Headache", "Body_Pain"]]
y = data["Disease"]


# ============================================================
# STEP 4: TRAIN AND TEST SPLIT
# 80% of data trains the model
# 20% of data tests the model
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
# STEP 5: TRAIN THE MODEL
# ============================================================

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

print("\n=== Model Trained Successfully ===")


# ============================================================
# STEP 6: EVALUATE THE MODEL
# ============================================================

y_pred   = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"\n=== Model Accuracy ===")
print(f"Accuracy: {round(accuracy * 100, 2)}%")


# ============================================================
# STEP 7: SAVE THE MODEL AND ENCODERS USING JOBLIB
# Joblib is more efficient than Pickle for large ML models
# ============================================================

joblib.dump(model,        "disease_model.pkl")
joblib.dump(le_gender,    "le_gender.pkl")
joblib.dump(le_fever,     "le_fever.pkl")
joblib.dump(le_cough,     "le_cough.pkl")
joblib.dump(le_headache,  "le_headache.pkl")
joblib.dump(le_body_pain, "le_body_pain.pkl")
joblib.dump(le_disease,   "le_disease.pkl")

print("\n=== Model and Encoders Saved Successfully ===")
print("Files created:")
print("  - disease_model.pkl")
print("  - le_gender.pkl")
print("  - le_fever.pkl")
print("  - le_cough.pkl")
print("  - le_headache.pkl")
print("  - le_body_pain.pkl")
print("  - le_disease.pkl")


# ============================================================
# STEP 8: TEST WITH A SAMPLE PREDICTION
# Patient: Age 30, Male, Fever Yes, Cough No,
#          Headache Yes, Body Pain Yes
# Expected: Malaria
# ============================================================

print("\n=== Sample Prediction Test ===")

sample = pd.DataFrame([[
    30,
    le_gender.transform(["Male"])[0],
    le_fever.transform(["Yes"])[0],
    le_cough.transform(["No"])[0],
    le_headache.transform(["Yes"])[0],
    le_body_pain.transform(["Yes"])[0]
]], columns=["Age", "Gender", "Fever", "Cough", "Headache", "Body_Pain"])

prediction   = model.predict(sample)
disease_name = le_disease.inverse_transform(prediction)[0]

print(f"Patient  -> Age: 30, Gender: Male, Fever: Yes, Cough: No, Headache: Yes, Body Pain: Yes")
print(f"Predicted Disease: {disease_name}")
