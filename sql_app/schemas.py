from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    description: str


class Product(ProductBase):
    id: int


    class Config:
        orm_mode = True
