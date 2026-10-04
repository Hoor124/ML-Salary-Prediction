
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("model/salary_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Salary Prediction App",
    page_icon="💰",
    layout="centered"
)

# Title
st.title("💰 Salary Prediction App")

st.write(
    "This machine learning application predicts salary "
    "based on years of professional experience."
)

st.divider()

# User input
experience = st.number_input(
    "Experience Years",
    min_value=0.0,
    max_value=50.0,
    value=1.0,
    step=0.1
)

# Prediction button
if st.button("Predict Salary"):

    input_data = pd.DataFrame({
        "Experience Years": [experience]
    })

    prediction = model.predict(input_data)[0]

    st.success(
        f"Predicted Salary: ${prediction:,.2f}"
    )

st.divider()

st.subheader("About the Model")

st.write(
    "The model was trained using a salary dataset containing "
    "experience years and salary information. "
    "The data was divided into training and testing sets, "
    "and regression models were evaluated using MSE, RMSE, "
    "MAE, and R²."
)
