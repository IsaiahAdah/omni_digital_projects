# ============================================================
# MEDCARE - AI DISEASE PREDICTION SYSTEM
# File: app.py
# Description: Streamlit web application that loads the trained
#              model and predicts disease based on patient
#              symptoms entered by hospital staff.
#
# Run with: python -m streamlit run app.py
# Queens Hospital Akure - AI Engineering Team
# ============================================================

import joblib
import pandas as pd
import streamlit as st


# ============================================================
# LOAD THE SAVED MODEL AND ENCODERS
# ============================================================

model        = joblib.load("disease_model.pkl")
le_gender    = joblib.load("le_gender.pkl")
le_fever     = joblib.load("le_fever.pkl")
le_cough     = joblib.load("le_cough.pkl")
le_headache  = joblib.load("le_headache.pkl")
le_body_pain = joblib.load("le_body_pain.pkl")
le_disease   = joblib.load("le_disease.pkl")


# ============================================================
# DISEASE INFORMATION
# Provides context about each predicted disease
# ============================================================

disease_info = {
    "Malaria": {
        "description": "A mosquito-borne infectious disease caused by Plasmodium parasites.",
        "advice": "Recommend antimalarial medication and blood test confirmation. Avoid mosquito exposure."
    },
    "Typhoid": {
        "description": "A bacterial infection caused by Salmonella typhi, spread through contaminated food and water.",
        "advice": "Recommend antibiotics and stool/blood culture test. Ensure proper hydration."
    },
    "Flu": {
        "description": "A contagious respiratory illness caused by influenza viruses.",
        "advice": "Recommend rest, hydration, and antiviral medication if severe. Monitor for complications."
    },
    "Common Cold": {
        "description": "A mild viral infection of the upper respiratory tract.",
        "advice": "Recommend rest, fluids, and over-the-counter cold medication. Usually resolves in 7-10 days."
    }
}


# ============================================================
# APP LAYOUT
# ============================================================

st.title("MedCare")
st.subheader("AI Disease Prediction System")
st.write("Queens Hospital Akure - AI Healthcare Assistant")
st.divider()

st.write("Enter the patient's information below to receive an AI-powered disease prediction.")
st.divider()

# --- Patient Information ---
st.write("**Patient Information**")

col1, col2 = st.columns(2)

with col1:
    age    = st.number_input("Age", min_value=1, max_value=100, value=30)
    fever  = st.selectbox("Fever", ["Yes", "No"])
    cough  = st.selectbox("Cough", ["Yes", "No"])

with col2:
    gender     = st.selectbox("Gender", ["Male", "Female"])
    headache   = st.selectbox("Headache", ["Yes", "No"])
    body_pain  = st.selectbox("Body Pain", ["Yes", "No"])

st.divider()

# ============================================================
# PREDICTION BUTTON
# ============================================================

if st.button("Predict Disease"):

    # Encode the inputs using the saved encoders
    encoded_gender    = le_gender.transform([gender])[0]
    encoded_fever     = le_fever.transform([fever])[0]
    encoded_cough     = le_cough.transform([cough])[0]
    encoded_headache  = le_headache.transform([headache])[0]
    encoded_body_pain = le_body_pain.transform([body_pain])[0]

    # Prepare the input DataFrame
    sample_input = pd.DataFrame([[
        age,
        encoded_gender,
        encoded_fever,
        encoded_cough,
        encoded_headache,
        encoded_body_pain
    ]], columns=["Age", "Gender", "Fever", "Cough", "Headache", "Body_Pain"])

    # Make the prediction
    prediction    = model.predict(sample_input)
    disease_name  = le_disease.inverse_transform(prediction)[0]

    # --- Display the Result ---
    st.success(f"Predicted Disease: {disease_name}")

    st.divider()

    # --- Patient Summary ---
    st.write("**Patient Summary**")

    col3, col4 = st.columns(2)

    with col3:
        st.write(f"Age        : {age}")
        st.write(f"Gender     : {gender}")
        st.write(f"Fever      : {fever}")

    with col4:
        st.write(f"Cough      : {cough}")
        st.write(f"Headache   : {headache}")
        st.write(f"Body Pain  : {body_pain}")

    st.divider()

    # --- Disease Information ---
    if disease_name in disease_info:
        st.write("**About This Disease**")
        st.info(disease_info[disease_name]["description"])

        st.write("**Medical Advice**")
        st.warning(disease_info[disease_name]["advice"])

    st.divider()
    st.caption("This AI prediction is intended to assist medical staff and does not replace professional medical diagnosis.")
