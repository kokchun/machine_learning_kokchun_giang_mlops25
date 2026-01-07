from fastapi import FastAPI
from data_processing import library_data

books = library_data("library.json").books

app = FastAPI()

@app.get("/books")
async def read_books():
    return books