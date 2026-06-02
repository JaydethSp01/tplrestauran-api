from pydantic import BaseModel
class MenuItem(BaseModel):
    id: int
    name: str
    price: float
class Mesa(BaseModel):
    id: int
    number: int
    status: str
class Pedido(BaseModel):
    id: int
    mesa_id: int
    items: list
    status: str
