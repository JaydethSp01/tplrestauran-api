from fastapi import APIRouter, HTTPException
from typing import List

router = APIRouter()

fake_tables_db = [
    {"id": 1, "number": 1, "capacity": 4},
    {"id": 2, "number": 2, "capacity": 2}
]

@router.get("/mesas", response_model=List[dict])
async def get_tables():
    return fake_tables_db

@router.post("/mesas", status_code=201)
async def create_table(table: dict):
    new_id = max(table["id"] for table in fake_tables_db) + 1
    table["id"] = new_id
    fake_tables_db.append(table)
    return table

@router.put("/mesas/{table_id}")
async def update_table(table_id: int, table: dict):
    for idx, existing_table in enumerate(fake_tables_db):
        if existing_table["id"] == table_id:
            fake_tables_db[idx] = {**existing_table, **table}
            return fake_tables_db[idx]
    raise HTTPException(status_code=404, detail="Table not found")

@router.delete("/mesas/{table_id}", status_code=204)
async def delete_table(table_id: int):
    global fake_tables_db
    fake_tables_db = [table for table in fake_tables_db if table["id"] != table_id]
