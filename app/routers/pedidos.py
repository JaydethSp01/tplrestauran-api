from fastapi import APIRouter, HTTPException
from typing import List

router = APIRouter()

fake_orders_db = [
    {"id": 1, "table_number": 1, "total": 29.99},
    {"id": 2, "table_number": 2, "total": 15.50}
]

@router.get("/pedidos", response_model=List[dict])
async def get_orders():
    return fake_orders_db

@router.post("/pedidos", status_code=201)
async def create_order(order: dict):
    new_id = max(order["id"] for order in fake_orders_db) + 1
    order["id"] = new_id
    fake_orders_db.append(order)
    return order

@router.put("/pedidos/{order_id}")
async def update_order(order_id: int, order: dict):
    for idx, existing_order in enumerate(fake_orders_db):
        if existing_order["id"] == order_id:
            fake_orders_db[idx] = {**existing_order, **order}
            return fake_orders_db[idx]
    raise HTTPException(status_code=404, detail="Order not found")

@router.delete("/pedidos/{order_id}", status_code=204)
async def delete_order(order_id: int):
    global fake_orders_db
    fake_orders_db = [order for order in fake_orders_db if order["id"] != order_id]
