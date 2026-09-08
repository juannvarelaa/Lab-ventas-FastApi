from pydantic import BaseModel

class ProductCreate(BaseModel):
    name:str
    price:float

class SaleCreate(BaseModel):
    fecha:str
    hora:str
    id_producto:int
    cantidad:int