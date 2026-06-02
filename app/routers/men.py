from fastapi import APIRouter, HTTPException
from typing import List

router = APIRouter()

fake_menu_db = [
    {"id": 1, "name": "Pizza Margherita", "description": "Classic pizza with tomatoes and mozzarella", "price": 8.5},
    {"id": 2, "name": "Spaghetti Carbonara", "description": "Pasta with eggs, cheese, pancetta, and pepper", "price": 10.0}
]

@router.get("/men", response_model=List[dict])
async def get_menu_items():
    return fake_menu_db

@router.post("/men", status_code=201)
async def create_menu_item(item: dict):
    new_id = max(item["id"] for item in fake_menu_db) + 1
    item["id"] = new_id
    fake_menu_db.append(item)
    return item

@router.put("/men/{item_id}")
async def update_menu_item(item_id: int, item: dict):
    for idx, existing_item in enumerate(fake_menu_db):
        if existing_item["id"] == item_id:
            fake_menu_db[idx] = {**existing_item, **item}
            return fake_menu_db[idx]
    raise HTTPException(status_code=404, detail="Menu item not found")

@router.delete("/men/{item_id}", status_code=204)
async def delete_menu_item(item_id: int):
    global fake_menu_db
    fake_menu_db = [item for item in fake_menu_db if item["id"] != item_id]
