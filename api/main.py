from fastapi import FastAPI, Depends, HTTPException
from database import get_db_session
from sqlalchemy.orm import Session
from operations import db_create_car, db_create_owner, db_delete_car, db_delete_owner, db_get_cars, db_get_owners, db_get_owners, db_get_owner_cars, db_update_car, db_update_owner
from schemas import CarCreate, CarUpdate, Owner, Car, OwnerCreate, OwnerUpdate
from sqlalchemy.exc import NoResultFound

app = FastAPI()

@app.get("/owners", response_model=list[Owner])
async def get_owners(db: Session = Depends(get_db_session)):
    return db_get_owners(db)

@app.get("/owners/{owner_id}/cars/", response_model=list[Car])
async def get_owner_cars(owner_id: int, db: Session = Depends(get_db_session)):
    try:
        cars = db_get_owner_cars(db, owner_id)
        return cars
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Owner not found")

@app.post("/owners", response_model=Owner)
async def post_owner(owner: OwnerCreate, db: Session = Depends(get_db_session)):
    return db_create_owner(db, owner)

@app.delete("/owners/{owner_id}", status_code=204)
async def delete_owner(owner_id: int, db: Session = Depends(get_db_session)):
    try:
        db_delete_owner(db, owner_id)
        return None
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Owner not found")

@app.put("/owners/{owner_id}", response_model=Owner)
async def update_owner(owner_id: int, owner_update: OwnerUpdate, db: Session = Depends(get_db_session)):
    try:
        owner = db_update_owner(db, owner_id, owner_update)
        return owner
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Owner not found")

@app.get("/cars", response_model=list[Car])
async def get_cars(db: Session = Depends(get_db_session)):
    return db_get_cars(db)

@app.post("/cars", response_model=Car)
async def post_car(car: CarCreate, db: Session = Depends(get_db_session)):
    return db_create_car(db, car)

@app.put("/cars/{car_id}", response_model=Car)
async def update_car(car_id: int, car_update: CarUpdate, db: Session = Depends(get_db_session)):
    try:
        car = db_update_car(db, car_id, car_update)
        return car
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Car not found")

@app.delete("/cars/{car_id}", status_code=204)
async def delete_car(car_id: int, db: Session = Depends(get_db_session)):
    try:
        db_delete_car(db, car_id)
        return None
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Car not found")