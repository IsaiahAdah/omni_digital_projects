# ============================================================
# AI DOCTOR - SAVE THE TRAINED MODEL
# File: ai_doctor_save_model.py
# Description: Trains the model and saves it to disk so the
#              Streamlit app can load and use it.
#
# Run this file ONCE before running the Streamlit app.
# ============================================================

import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# --- Load the dataset ---
user_data = pd.read_csv("ai_doctor_users.csv")

# --- Encode the data ---
le_gender    = LabelEncoder()
le_age_group = LabelEncoder()
le_diet      = LabelEncoder()

user_data["Gender"]    = le_gender.fit_transform(user_data["Gender"])
user_data["Age_Group"] = le_age_group.fit_transform(user_data["Age_Group"])
user_data["Diet"]      = le_diet.fit_transform(user_data["Diet"])

# --- Set input and output ---
X = user_data[["Age", "Gender", "Age_Group"]]
y = user_data["Diet"]

# --- Train the model ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# --- Save the model and encoders to disk ---
with open("ai_doctor_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("le_gender.pkl", "wb") as f:
    pickle.dump(le_gender, f)

with open("le_age_group.pkl", "wb") as f:
    pickle.dump(le_age_group, f)

with open("le_diet.pkl", "wb") as f:
    pickle.dump(le_diet, f)

print("Model and encoders saved successfully!")
print("Files created:")
print("  - ai_doctor_model.pkl")
print("  - le_gender.pkl")
print("  - le_age_group.pkl")
print("  - le_diet.pkl")
