import streamlit as st
import pickle
import numpy as np

# Load the model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# App title
st.title("🔮 Salary Predictor")
st.write("Enter years of experience to predict the salary.")

# Input box for the user
input_value = st.number_input(
    "Enter Years of Experience:",
    min_value=0.0
)

# Predict button
if st.button("Predict"):
    prediction = model.predict([[input_value]])
    st.success(f"✅ Predicted Salary: **{prediction[0]:.2f}**")
