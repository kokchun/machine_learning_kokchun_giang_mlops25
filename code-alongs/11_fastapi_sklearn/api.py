from fastapi import FastAPI
import joblib
import pandas as pd 
from constants import DATA_PATH, CLASSIFIER_PATH
from data_models import IrisInput, PredictionOutput

df = pd.read_csv(DATA_PATH / "IRIS.csv")

app = FastAPI()

# read
@app.get("/api/data")
async def read_data():
    return df.to_dict(orient="records")

# create
@app.post("/api/predict")
async def predict_flower(payload: IrisInput):
    pass