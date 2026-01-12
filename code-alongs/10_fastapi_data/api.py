from fastapi import FastAPI
from data_processing import DataExplorer

app = FastAPI()

@app.get("/sales")
async def read_sales():
    data_explorer = DataExplorer(limit=5)
    return data_explorer.json_response()
