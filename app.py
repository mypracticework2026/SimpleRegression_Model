import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title="Salary Predictor", page_icon="📈", layout="centered")

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("📈 Salary Predictor")
st.caption("ML-powered estimation based on years of experience")

st.divider()

col1, col2, col3 = st.columns(3)

col1.markdown("""
<div style="background:#534AB7; padding:1rem; border-radius:10px;">
  <p style="color:#AFA9EC; font-size:12px; margin:0;">MODEL</p>
  <p style="color:#EEEDFE; font-size:16px; font-weight:600; margin:0;">Linear Regression</p>
</div>
""", unsafe_allow_html=True)

col2.markdown("""
<div style="background:#0F6E56; padding:1rem; border-radius:10px;">
  <p style="color:#5DCAA5; font-size:12px; margin:0;">FEATURE</p>
  <p style="color:#E1F5EE; font-size:16px; font-weight:600; margin:0;">Years of Experience</p>
</div>
""", unsafe_allow_html=True)

col3.markdown("""
<div style="background:#993C1D; padding:1rem; border-radius:10px;">
  <p style="color:#F0997B; font-size:12px; margin:0;">OUTPUT</p>
  <p style="color:#FAECE7; font-size:16px; font-weight:600; margin:0;">Predicted Salary</p>
</div>
""", unsafe_allow_html=True)

st.divider()

years = st.number_input("Enter years of experience:", min_value=0.0, max_value=40.0, step=0.5)

if st.button("Predict Salary", use_container_width=True):
    prediction = model.predict([[years]])
    salary = round(prediction[0], 2)
    st.markdown(f"""
    <div style="background:#0F6E56; padding:1.2rem; border-radius:10px; margin-top:1rem;">
      <p style="color:#5DCAA5; font-size:13px; margin:0;">Estimated Annual Salary</p>
      <p style="color:#E1F5EE; font-size:28px; font-weight:700; margin:4px 0;">${salary:,.2f}</p>
      <p style="color:#9FE1CB; font-size:12px; margin:0;">Based on {years} years of experience</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()
st.caption("⚠️ Predictions are estimates based on training data. Actual salaries may vary.")
