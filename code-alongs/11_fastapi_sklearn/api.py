from fastapi import FastAPI
import joblib
import pandas as pd 
from constants import DATA_PATH, CLASSIFIER_PATH

df = pd.read_csv(DATA_PATH / "IRIS.csv")

app = FastAPI()

@app.get("/api/data")
async def read_data():
    return df.to_dict(orient="records")
