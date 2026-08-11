import streamlit as st
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.title("🔮 Predict Performance")

hours = st.slider("Study Hours", 0, 10)
attendance = st.slider("Attendance", 0, 100)
prev_marks = st.slider("Previous Marks", 0, 100)
sleep = st.slider("Sleep Hours", 0, 10)

if st.button("Predict"):
    result = model.predict([[hours, attendance, prev_marks, sleep]])[0]

    st.success(f"📊 Predicted Marks: {int(result)}")

    # Risk Detection
    if result < 50:
        st.error("🔴 High Risk")
    elif result < 70:
        st.warning("🟡 Medium Risk")
    else:
        st.success("🟢 Safe")

    # Grade
    if result >= 80:
        st.info("Grade: A")
    elif result >= 60:
        st.info("Grade: B")
    else:
        st.info("Grade: C")

    # Suggestions
    st.subheader("💡 Suggestions")
    if hours < 3:
        st.write("👉 Increase study hours")
    if attendance < 75:
        st.write("👉 Improve attendance")
    if sleep < 6:
        st.write("👉 Get proper sleep")