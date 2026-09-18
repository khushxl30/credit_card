
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import pickle
import os


# --------------------------------------------------
# CREATE APP
# --------------------------------------------------

app = FastAPI(
    title="Credit Card Fraud Detection API",
    description="Machine Learning API for detecting fraudulent transactions",
    version="1.0"
)


# --------------------------------------------------
# CORS
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "fraud_model.pkl"
)

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)


# --------------------------------------------------
# INPUT MODEL
# --------------------------------------------------

class Transaction(BaseModel):

    Time: float
    Amount: float

    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float


# --------------------------------------------------
# HOME
# --------------------------------------------------

@app.get("/")
def home():

    return {
        "status": "success",
        "message": "Credit Card Fraud Detection API is running"
    }


# --------------------------------------------------
# HEALTH CHECK
# --------------------------------------------------

@app.get("/health")
def health():

    return {
        "status": "healthy",
        "model": "loaded"
    }


# --------------------------------------------------
# PREDICTION
# --------------------------------------------------

@app.post("/predict")
def predict(transaction: Transaction):

    # Convert input to dictionary
    transaction_data = transaction.model_dump()

    # Convert to DataFrame
    input_data = pd.DataFrame([transaction_data])

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Convert result
    if prediction == 1:

        result = "Fraudulent Transaction"
        message = "The transaction has been identified as potentially fraudulent."

    else:

        result = "Genuine Transaction"
        message = "The transaction appears to be legitimate."

    return {
        "prediction": int(prediction),
        "result": result,
        "message": message
    }

