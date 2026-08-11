import streamlit as st
import joblib
import numpy as np

st.title("🧪 Test Student Performance")

st.write("Enter student details:")

# Inputs
hours = st.number_input("Study Hours", 0, 24)
attendance = st.number_input("Attendance (%)", 0, 100)
prev_marks = st.number_input("Previous Marks", 0, 100)
sleep = st.number_input("Sleep Hours", 0, 12)

# Load model safely
try:
    model = joblib.load("model.pkl")
except:
    st.error("❌ Model not found! Run model.py first.")
    st.stop()

# Prediction
if st.button("Predict"):
    data = np.array([[hours, attendance, prev_marks, sleep]])
    prediction = model.predict(data)

    st.success(f"🎯 Predicted Score: {prediction[0]:.2f}")