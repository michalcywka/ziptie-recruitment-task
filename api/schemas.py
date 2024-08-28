from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import date

class CarBase(BaseModel):
    brand: str = Field(..., max_length=20)
    model: str = Field(..., max_length=30)
    production_date: date

class CarCreate(CarBase):
    pass

class CarUpdate(CarBase):
    owner_id: int

class Car(CarBase):
    id: int
    owner_id: Optional[int] = None

    class Config:
        from_attributes = True

class OwnerBase(BaseModel):
    name: str = Field(..., max_length=40)
    last_name: str = Field(..., max_length=60)
    email: EmailStr = Field(..., max_length=120)

class OwnerCreate(OwnerBase):
    cars: Optional[List[CarCreate]] = []

class OwnerUpdate(OwnerBase):
    pass

class Owner(OwnerBase):
    id: int
    cars: Optional[List[Car]] = []

    class Config:
        from_attributes = True