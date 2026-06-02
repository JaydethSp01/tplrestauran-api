from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import menu, mesas, pedidos, cocina
import os
app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=os.environ.get("CORS_ORIGINS","*").split(","), allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.include_router(menu.router)
app.include_router(mesas.router)
app.include_router(pedidos.router)
app.include_router(cocina.router)
@app.get("/health")
async def health():
    return {"status": "ok"}
