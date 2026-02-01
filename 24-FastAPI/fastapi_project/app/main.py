# app/main_basics.py
from fastapi import FastAPI, HTTPException

app = FastAPI(title="FastAPI Basics – Learning Mode",
description = 'API for learning FastAPI',
version = '1.0.0'
)


@app.get("/")
def root():
    return {"message": "Welcome to FastAPI basics"}

@app.get("/items/{item_id}", tags=['Items'], summary='Get an item by its ID')
def get_item(item_id: int):
    return {
        "item_id": item_id,
        "description": "This endpoint demonstrates path parameters"
    }

@app.get("/search", tags=['Items'], summary='Search items with query parameters')
def search_items(q: str | None = None, limit: int = 10):
    return {
        "query": q,
        "limit": limit
    }

@app.post("/items", status_code=201, tags=['Items'], summary='Create a new item')
def create_item(payload: dict):
    if "name" not in payload:
        raise HTTPException(status_code=400, detail="name is required")
    return {
        "message": "Item created",
        "item": payload
    }

@app.delete("/items/{item_id}", status_code=204, tags=['Items'], summary='Delete an item by its ID')
def delete_item(item_id: int):
    return None

@app.get('/health', tags=['Health'], summary='Health check test function')
def health():
    return {'status': 'ok'}