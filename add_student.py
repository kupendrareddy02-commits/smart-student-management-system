import streamlit as st
import pickle
from database import add_student

model = pickle.load(open("model.pkl", "rb"))

st.title("➕ Add Student")

name = st.text_input("Student Name")
hours = st.slider("Study Hours", 0, 10)
attendance = st.slider("Attendance (%)", 0, 100)
prev_marks = st.slider("Previous Marks", 0, 100)
sleep = st.slider("Sleep Hours", 0, 10)

if st.button("Add & Predict"):
    pred = model.predict([[hours, attendance, prev_marks, sleep]])[0]
    
    add_student(name, hours, attendance, prev_marks, sleep, pred)

    st.success(f"Predicted Marks: {int(pred)}")