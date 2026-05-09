# ============================================================
# GLYCOAID - DIABETES RISK PREDICTION SYSTEM
# File: app.py
# Description: Streamlit web application with professional
#              UI using native Streamlit components only.
#
# Run with: python -m streamlit run app.py
# ============================================================

import joblib
import numpy as np
import pandas as pd
import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="GlycoAID - Diabetes Risk Prediction",
    page_icon="🩺",
    layout="wide"
)


# ============================================================
# LOAD MODEL AND SCALER
# ============================================================

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model    = joblib.load(os.path.join(BASE_DIR, "model.pkl"))
scaler   = joblib.load(os.path.join(BASE_DIR, "scaler.pkl"))

FEATURE_NAMES = [
    "Pregnancies", "Glucose", "BloodPressure",
    "SkinThickness", "Insulin", "BMI",
    "DiabetesPedigreeFunction", "Age"
]


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/stethoscope.png", width=60)
    st.markdown("### About GlycoAID")
    st.write(
        "GlycoAID is an AI-powered early screening system "
        "designed to assist medical staff in identifying "
        "patients at risk of diabetes based on routine "
        "diagnostic test results."
    )
    st.divider()
    st.write("**How to use:**")
    st.write("1. Enter patient details on the right")
    st.write("2. Click Predict Diabetes Risk")
    st.write("3. Review the risk assessment")
    st.divider()
    st.info(
        "**Blood Pressure Note:** Both systolic and diastolic "
        "readings are recorded. The model uses diastolic pressure "
        "for prediction, consistent with the Pima Indians training dataset."
    )
    st.divider()
    st.caption(
        "This tool is intended to assist medical professionals. "
        "It does not replace clinical diagnosis."
    )


# ============================================================
# HEADER
# ============================================================

header_col1, header_col2 = st.columns([3, 1])

with header_col1:
    st.title("🩺 GlycoAID")
    st.subheader("AI-Powered Diabetes Risk Prediction System")
    st.write("Enter the patient's diagnostic information below to receive an instant diabetes risk assessment.")

with header_col2:
    st.metric(label="Dataset", value="768 Records")
    st.metric(label="Features", value="8 Inputs")

st.divider()

# --- Stats Row ---
stat1, stat2, stat3, stat4 = st.columns(4)

with stat1:
    st.metric(label="ML Models Trained", value="2 Models")
with stat2:
    st.metric(label="Model Type", value="Classification")
with stat3:
    st.metric(label="Prediction Speed", value="Real-time")
with stat4:
    st.metric(label="Dataset Source", value="Pima Indians")

st.divider()

# --- Technology Tags ---
st.caption(
    "Technologies: Python  |  Scikit-learn  |  "
    "Logistic Regression  |  Decision Tree  |  "
    "Joblib  |  Streamlit  |  Pandas  |  NumPy"
)

st.divider()


# ============================================================
# PATIENT INPUT FORM
# ============================================================

st.write("### Patient Diagnostic Information")

col1, col2, col3 = st.columns(3)

with col1:
    pregnancies = st.number_input(
        "Pregnancies",
        min_value=0, max_value=20, value=1,
        help="Number of times the patient has been pregnant"
    )
    glucose = st.number_input(
        "Glucose (mg/dL)",
        min_value=0, max_value=300, value=120,
        help="Plasma glucose concentration after 2-hour oral glucose tolerance test"
    )
    st.write("**Blood Pressure (mm Hg)**")
    bp_col1, bp_col2 = st.columns(2)
    with bp_col1:
        systolic_bp = st.number_input(
            "Systolic",
            min_value=0, max_value=300, value=120,
            help="Upper number - pressure when heart beats"
        )
    with bp_col2:
        diastolic_bp = st.number_input(
            "Diastolic",
            min_value=0, max_value=200, value=80,
            help="Lower number - pressure when heart rests"
        )

with col2:
    skin_thickness = st.number_input(
        "Skin Thickness (mm)",
        min_value=0, max_value=100, value=20,
        help="Triceps skin fold thickness"
    )
    insulin = st.number_input(
        "Insulin (mu U/ml)",
        min_value=0, max_value=1000, value=80,
        help="2-Hour serum insulin level"
    )
    bmi = st.number_input(
        "BMI",
        min_value=0.0, max_value=70.0, value=25.0,
        step=0.1,
        help="Body Mass Index"
    )

with col3:
    dpf = st.number_input(
        "Diabetes Pedigree Function",
        min_value=0.0, max_value=3.0, value=0.5,
        step=0.001, format="%.3f",
        help="Genetic risk score from family history"
    )
    age = st.number_input(
        "Age",
        min_value=1, max_value=120, value=30,
        help="Patient age in years"
    )

# --- Live Blood Pressure Classification ---
st.divider()
st.write("**Blood Pressure Assessment**")

bp_col3, bp_col4, bp_col5 = st.columns(3)

with bp_col3:
    st.metric(
        label="Recorded Blood Pressure",
        value=f"{systolic_bp} / {diastolic_bp} mm Hg"
    )

with bp_col4:
    if systolic_bp < 120 and diastolic_bp < 80:
        bp_category = "Normal"
        st.success(f"BP Status: {bp_category}")
    elif systolic_bp < 130 and diastolic_bp < 80:
        bp_category = "Elevated"
        st.warning(f"BP Status: {bp_category}")
    elif systolic_bp < 140 or diastolic_bp < 90:
        bp_category = "High - Stage 1"
        st.warning(f"BP Status: {bp_category}")
    else:
        bp_category = "High - Stage 2"
        st.error(f"BP Status: {bp_category}")

with bp_col5:
    st.caption(
        "Normal: below 120/80\n"
        "Elevated: 120-129 / below 80\n"
        "Stage 1: 130-139 / 80-89\n"
        "Stage 2: 140+ / 90+"
    )

st.divider()


# ============================================================
# PREDICTION BUTTON
# ============================================================

if st.button("Predict Diabetes Risk", use_container_width=True, type="primary"):

    input_data = pd.DataFrame([[
        pregnancies, glucose, diastolic_bp,
        skin_thickness, insulin, bmi, dpf, age
    ]], columns=FEATURE_NAMES)

    input_scaled = scaler.transform(input_data)
    prediction   = model.predict(input_scaled)[0]
    probability  = model.predict_proba(input_scaled)[0]

    risk_percent    = round(probability[1] * 100, 1)
    no_risk_percent = round(probability[0] * 100, 1)

    st.divider()
    st.write("### Prediction Result")

    result_col1, result_col2 = st.columns([2, 1])

    with result_col1:
        if prediction == 1:
            st.error(
                "**High Risk of Diabetes Detected**\n\n"
                "The AI model has identified indicators consistent with diabetes. "
                "Please refer the patient for further clinical evaluation and "
                "laboratory confirmation."
            )
        else:
            st.success(
                "**Low Risk of Diabetes**\n\n"
                "The AI model has not identified significant diabetes risk "
                "indicators at this time. Continue routine monitoring and "
                "healthy lifestyle guidance."
            )

    with result_col2:
        st.metric(label="Diabetes Risk Score", value=f"{risk_percent}%")
        st.metric(label="No Diabetes Score",   value=f"{no_risk_percent}%")

    st.divider()

    # --- Risk Gauge ---
    st.write("### Risk Probability Breakdown")

    gauge_col1, gauge_col2 = st.columns(2)
    with gauge_col1:
        st.write("Diabetes Risk")
        st.progress(int(risk_percent))
        st.caption(f"{risk_percent}% probability of diabetes")
    with gauge_col2:
        st.write("No Diabetes")
        st.progress(int(no_risk_percent))
        st.caption(f"{no_risk_percent}% probability of no diabetes")

    st.divider()

    # --- Patient Summary ---
    st.write("### Patient Data Summary")

    summary_data = {
        "Feature": [
            "Pregnancies", "Glucose",
            "Blood Pressure (Systolic)", "Blood Pressure (Diastolic)",
            "Blood Pressure Category", "Skin Thickness",
            "Insulin", "BMI", "Diabetes Pedigree Function", "Age"
        ],
        "Value": [
            pregnancies, glucose,
            f"{systolic_bp} mm Hg", f"{diastolic_bp} mm Hg",
            bp_category, skin_thickness,
            insulin, bmi, dpf, age
        ]
    }

    st.dataframe(
        pd.DataFrame(summary_data),
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # --- Feature Importance ---
    st.write("### Feature Importance")

    try:
        importance = model.feature_importances_
        importance_df = pd.DataFrame({
            "Feature": FEATURE_NAMES, "Importance": importance
        }).sort_values("Importance", ascending=False)
        st.bar_chart(importance_df.set_index("Feature")["Importance"])
        st.caption("Higher values indicate features with more influence on the prediction.")
    except AttributeError:
        coefficients = np.abs(model.coef_[0])
        importance_df = pd.DataFrame({
            "Feature": FEATURE_NAMES, "Importance": coefficients
        }).sort_values("Importance", ascending=False)
        st.bar_chart(importance_df.set_index("Feature")["Importance"])
        st.caption("Higher coefficient values indicate features with greater influence.")

    st.divider()

    # --- Explainable AI ---
    st.write("### Why Was This Prediction Made?")

    explanations = []

    if glucose > 140:
        explanations.append(f"Glucose level of {glucose} mg/dL is above the high-risk threshold of 140 mg/dL.")
    elif glucose > 100:
        explanations.append(f"Glucose level of {glucose} mg/dL is in the pre-diabetic range.")
    else:
        explanations.append(f"Glucose level of {glucose} mg/dL is within the normal range.")

    if systolic_bp >= 140 or diastolic_bp >= 90:
        explanations.append(f"Blood pressure of {systolic_bp}/{diastolic_bp} mm Hg indicates Stage 2 hypertension, associated with increased diabetes risk.")
    elif systolic_bp >= 130 or diastolic_bp >= 80:
        explanations.append(f"Blood pressure of {systolic_bp}/{diastolic_bp} mm Hg indicates Stage 1 hypertension.")
    else:
        explanations.append(f"Blood pressure of {systolic_bp}/{diastolic_bp} mm Hg is within an acceptable range.")

    if bmi >= 30:
        explanations.append(f"BMI of {bmi} indicates obesity, which is a significant diabetes risk factor.")
    elif bmi >= 25:
        explanations.append(f"BMI of {bmi} indicates overweight, which increases diabetes risk.")
    else:
        explanations.append(f"BMI of {bmi} is within the healthy range.")

    if age >= 45:
        explanations.append(f"Age of {age} years places this patient in a higher-risk age group for diabetes.")
    else:
        explanations.append(f"Age of {age} years is below the higher-risk threshold of 45.")

    if dpf >= 0.5:
        explanations.append(f"Diabetes Pedigree Function of {dpf} suggests notable family history influence.")
    else:
        explanations.append(f"Diabetes Pedigree Function of {dpf} suggests low family history influence.")

    if insulin == 0 or insulin < 16:
        explanations.append(f"Insulin level of {insulin} mu U/ml may indicate insufficient insulin production.")

    for exp in explanations:
        st.write(f"• {exp}")

    st.divider()
    st.caption(
        "GlycoAID AI Prediction System. This assessment is based on statistical patterns "
        "in medical data and is intended to support, not replace, professional medical "
        "judgment. Blood pressure classification follows American Heart Association guidelines."
    )
