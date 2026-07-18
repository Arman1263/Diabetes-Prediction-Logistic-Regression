import streamlit as st
import pickle
import numpy as np

st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon="🩺",
    layout="centered"
)

st.title("🩺 Diabetes Prediction App")

st.write(
    "Enter the patient's medical information below to predict whether they are diabetic."
)

with open("model/model.pkl", "rb") as file:
    model = pickle.load(file)

with open("model/scaler.pkl", "rb") as file:
    scaler = pickle.load(file)

st.success("✅ Model Loaded Successfully!")


st.subheader("Patient Information")

col1, col2 = st.columns(2)

with col1:

    pregnancies = st.number_input(
        "Pregnancies",
        min_value=0,
        max_value=20,
        value=0
    )

    glucose = st.number_input(
    "Glucose",
    min_value=1.0,
    value=120.0,
    help="Normal fasting glucose is generally between 70 and 100 mg/dL."
    )

    blood_pressure = st.number_input(
    "Blood Pressure",
    min_value=1.0,
    value=70.0,
    help="Enter the diastolic blood pressure."
    )

    skin_thickness = st.number_input(
    "Skin Thickness",
    min_value=1.0,
    value=20.0
    )


with col2:

    insulin = st.number_input(
    "Insulin",
    min_value=1.0,
    value=79.0
    )

    bmi = st.number_input(
    "BMI",
    min_value=1.0,
    value=32.0
    )

    diabetes_pedigree = st.number_input(
        "Diabetes Pedigree Function",
        min_value=0.000,
        value=0.47,
        format="%.3f"
    )

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=30
    )


predict_button = st.button("🔍 Predict")

if predict_button:

    input_data = np.array([[
        pregnancies,
        glucose,
        blood_pressure,
        skin_thickness,
        insulin,
        bmi,
        diabetes_pedigree,
        age
    ]])

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)

    probability = model.predict_proba(input_scaled)

    diabetes_probability = probability[0][1]
    confidence = np.max(probability)

    st.divider()
    st.subheader("Prediction Result")

    if prediction[0] == 1:
        st.error("⚠️ The model predicts that the patient is Diabetic.")
    else:
        st.success("✅ The model predicts that the patient is Non-Diabetic.")

    st.write(f"**Probability of Diabetes:** {diabetes_probability:.2%}")
    st.write(f"**Confidence:** {confidence:.2%}")



st.sidebar.title("🩺 About")

st.sidebar.info(
    """
    This app predicts the likelihood of diabetes using a Logistic Regression model.

    **Model:** Logistic Regression

    **Dataset:** Pima Indians Diabetes Dataset

    Developed with:
    - Python
    - Scikit-learn
    - Streamlit
    """
)


st.sidebar.subheader("Model Performance")

st.sidebar.write("Accuracy : 75.32%")
st.sidebar.write("Precision : 66.67%")
st.sidebar.write("Recall : 61.82%")
st.sidebar.write("F1 Score : 64.15%")
st.sidebar.write("ROC-AUC : 82.30%")


st.divider()

st.caption(
    "Developed by Arman Shikalgar | Machine Learning Project using Streamlit"
)