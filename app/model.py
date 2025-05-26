# app/model.py
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import os

# Dummy sales data
df = pd.read_csv(os.path.join("data", "sales_data.csv"))


X = df[["advertising"]]
y = df["sales"]

model = LinearRegression()
model.fit(X, y)

# Save model
with open("app/model.pkl", "wb") as f:
    pickle.dump(model, f)
