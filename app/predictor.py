# app/predictor.py
import pickle
import numpy as np

# Load model
with open("app/model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_sales(advertising_budget: float) -> float:
    prediction = model.predict(np.array([[advertising_budget]]))
    return prediction[0]
