import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load data
data = pd.read_csv("data.csv")

# ✅ Use 4 features
X = data[['hours', 'attendance', 'prev_marks', 'sleep']]
y = data['result']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained successfully!")