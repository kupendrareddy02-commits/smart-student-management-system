import streamlit as st
import pandas as pd
from database import get_students
import matplotlib.pyplot as plt

st.title("📊 Dashboard")

data = get_students()

df = pd.DataFrame(data, columns=[
    "ID","Name","Hours","Attendance","Previous Marks","Sleep","Predicted Marks"
])

st.dataframe(df)

# Graph
st.subheader("📈 Performance Chart")

fig, ax = plt.subplots()
ax.bar(df["Name"], df["Predicted Marks"])
plt.xticks(rotation=45)

st.pyplot(fig)