# ============================================================
# AI DOCTOR - STREAMLIT WEB APP
# File: ai_doctor_app.py
# Description: A simple web app that loads the trained model
#              and recommends a diet based on user input.
#
# Run with: python -m streamlit run ai_doctor_app.py
# ============================================================

import pickle
import pandas as pd
import streamlit as st


# --- Load the saved model and encoders ---
with open("ai_doctor_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("le_gender.pkl", "rb") as f:
    le_gender = pickle.load(f)

with open("le_age_group.pkl", "rb") as f:
    le_age_group = pickle.load(f)

with open("le_diet.pkl", "rb") as f:
    le_diet = pickle.load(f)


# --- Helper function to determine age group ---
def get_age_group(age):
    if age <= 12:
        return "Child"
    elif age <= 19:
        return "Teen"
    elif age <= 59:
        return "Adult"
    else:
        return "Senior"


# ============================================================
# APP LAYOUT
# ============================================================

st.title("AI Doctor")
st.subheader("Personalised Diet Recommendation App")
st.write("Fill in your details below and get an instant diet recommendation.")

st.divider()

# --- User Inputs ---
age    = st.number_input("Enter your age", min_value=1, max_value=100, value=25)
gender = st.selectbox("Select your gender", ["Female", "Male"])

st.divider()

# --- Predict Button ---
if st.button("Get My Diet Recommendation"):

    # Determine age group from age
    age_group = get_age_group(age)

    # Encode the inputs
    encoded_gender    = le_gender.transform([gender])[0]
    encoded_age_group = le_age_group.transform([age_group])[0]

    # Prepare input for the model
    sample_input = pd.DataFrame(
        [[age, encoded_gender, encoded_age_group]],
        columns=["Age", "Gender", "Age_Group"]
    )

    # Make prediction
    prediction       = model.predict(sample_input)
    recommended_diet = le_diet.inverse_transform(prediction)[0]

    # --- Display the result ---
    st.success(f"Recommended Diet: {recommended_diet}")

    st.write("---")
    st.write("**Your Profile Summary:**")
    st.write(f"Age       : {age}")
    st.write(f"Gender    : {gender}")
    st.write(f"Age Group : {age_group}")
    st.write(f"Diet Plan : {recommended_diet}")

    # Show diet description
    diet_info = {
        "Growth Diet":       "Focuses on nutrients that support healthy growth and development in children.",
        "High Energy Diet":  "Provides high calories and nutrients to support the active lifestyle of teenagers.",
        "Balanced Diet":     "A well-rounded mix of proteins, carbohydrates, and healthy fats for adult females.",
        "High Protein Diet": "Rich in protein to support muscle maintenance and energy for adult males.",
        "Low Sodium Diet":   "Reduces sodium intake to support heart health and blood pressure in seniors."
    }

    if recommended_diet in diet_info:
        st.info(diet_info[recommended_diet])
