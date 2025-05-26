# app/main.py

from fastapi import FastAPI
from pydantic import BaseModel
from app.predictor import predict_sales

# Initialize FastAPI app
app = FastAPI(
    title="📈 Sales Predictor API",
    description="Predicts sales based on advertising budget using a trained ML model.",
    version="1.0.0"
)

# Request schema
class SalesInput(BaseModel):
    advertising: float

# POST endpoint for prediction
@app.post("/predict", summary="Predict Sales", response_description="Predicted sales value")
def get_prediction(input: SalesInput):
    """
    Predicts sales based on advertising budget.

    - **advertising**: advertising spend in dollars
    """
    prediction = predict_sales(input.advertising)
    return {
        "advertising_budget": input.advertising,
        "predicted_sales": round(prediction, 2)
    }
