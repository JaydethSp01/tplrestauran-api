from fastapi import APIRouter, HTTPException
from typing import List

router = APIRouter()

fake_kitchen_orders_db = [
    {"id": 1, "table_number": 1, "status": "Preparando"},
    {"id": 2, "table_number": 2, "status": "Listo"}
]

@router.get("/cocina", response_model=List[dict])
async def get_kitchen_orders():
    return fake_kitchen_orders_db

@router.post("/cocina", status_code=201)
async def create_kitchen_order(order: dict):
    new_id = max(order["id"] for order in fake_kitchen_orders_db) + 1
    order["id"] = new_id
    fake_kitchen_orders_db.append(order)
    return order

@router.put("/cocina/{order_id}")
async def update_kitchen_order(order_id: int, order: dict):
    for idx, existing_order in enumerate(fake_kitchen_orders_db):
        if existing_order["id"] == order_id:
            fake_kitchen_orders_db[idx] = {**existing_order, **order}
            return fake_kitchen_orders_db[idx]
    raise HTTPException(status_code=404, detail="Kitchen order not found")

@router.delete("/cocina/{order_id}", status_code=204)
async def delete_kitchen_order(order_id: int):
    global fake_kitchen_orders_db
    fake_kitchen_orders_db = [order for order in fake_kitchen_orders_db if order["id"] != order_id]
