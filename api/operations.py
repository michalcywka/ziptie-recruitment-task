from sqlalchemy.orm import Session, joinedload
from models import OwnerModel, CarModel
from schemas import CarCreate, CarUpdate, OwnerCreate, OwnerUpdate
from sqlalchemy.exc import NoResultFound

def db_get_owners(db: Session):
    """
    Retrieves all owners from the database.

    Args:
        db (Session): SQLAlchemy database session.

    Returns:
        List[OwnerModel]: A list of all owners in the database.
    """
    return db.query(OwnerModel).all()


def db_create_owner(db: Session, owner: OwnerCreate):
    """
    Creates a new owner in the database with optional associated cars.

    Args:
        db (Session): SQLAlchemy database session.
        owner (OwnerCreate): The owner data to be created.

    Returns:
        OwnerModel: The newly created owner with associated cars if provided.
    """
    db_owner = OwnerModel(name=owner.name, last_name=owner.last_name, email=owner.email)
    db.add(db_owner)
    db.commit()
    db.refresh(db_owner)
    
    if owner.cars:
        for car in owner.cars:
            db_car = CarModel(**car.model_dump(), owner_id=db_owner.id)
            db.add(db_car)
        db.commit()

    return db_owner


def db_get_owner_cars(db: Session, owner_id: int):
    """
    Retrieves all cars associated with a specific owner.

    Args:
        db (Session): SQLAlchemy database session.
        owner_id (int): The ID of the owner whose cars are to be retrieved.

    Raises:
        NoResultFound: If the owner does not exist.

    Returns:
        List[CarModel]: A list of cars associated with the owner.
    """
    owner_exists = db.query(OwnerModel).filter(OwnerModel.id == owner_id).scalar() is not None
    if not owner_exists:
        raise NoResultFound("Owner not found")
    
    return db.query(CarModel).join(OwnerModel).filter(OwnerModel.id == owner_id).options(joinedload(CarModel.owner)).all()


def db_delete_owner(db: Session, owner_id: int):
    """
    Deletes an owner and their associated cars from the database.

    Args:
        db (Session): SQLAlchemy database session.
        owner_id (int): The ID of the owner to be deleted.

    Raises:
        NoResultFound: If the owner does not exist.
    """
    owner = db.query(OwnerModel).filter(OwnerModel.id == owner_id).first()
    if not owner:
        raise NoResultFound("Owner not found")
    
    db.query(CarModel).filter(CarModel.owner_id == owner_id).delete(synchronize_session=False)
    
    db.delete(owner)
    db.commit()


def db_update_owner(db: Session, owner_id: int, owner_update: OwnerUpdate):
    """
    Updates an owner's details in the database.

    Args:
        db (Session): SQLAlchemy database session.
        owner_id (int): The ID of the owner to be updated.
        owner_update (OwnerUpdate): The updated owner data.

    Raises:
        NoResultFound: If the owner does not exist.

    Returns:
        OwnerModel: The updated owner.
    """
    db_owner = db.query(OwnerModel).filter(OwnerModel.id == owner_id).first()
    
    if db_owner is None:
        raise NoResultFound()

    db_owner.name = owner_update.name
    db_owner.last_name = owner_update.last_name
    db_owner.email = owner_update.email

    db.commit()
    db.refresh(db_owner)
    
    return db_owner


def db_get_cars(db: Session):
    """
    Retrieves all cars from the database.

    Args:
        db (Session): SQLAlchemy database session.

    Returns:
        List[CarModel]: A list of all cars in the database.
    """
    return db.query(CarModel).all()


def db_create_car(db: Session, car: CarCreate):
    """
    Creates a new car in the database.

    Args:
        db (Session): SQLAlchemy database session.
        car (CarCreate): The car data to be created.

    Returns:
        CarModel: The newly created car.
    """
    db_car = CarModel(**car.model_dump())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)

    return db_car


def db_delete_car(db: Session, car_id: int):
    """
    Deletes a car from the database.

    Args:
        db (Session): SQLAlchemy database session.
        car_id (int): The ID of the car to be deleted.

    Raises:
        NoResultFound: If the car does not exist.
    """
    car = db.query(CarModel).filter(CarModel.id == car_id).first()
    if not car:
        raise NoResultFound("Car not found")

    db.delete(car)
    db.commit()


def db_update_car(db: Session, car_id: int, car_update: CarUpdate):
    """
    Updates a car's details in the database.

    Args:
        db (Session): SQLAlchemy database session.
        car_id (int): The ID of the car to be updated.
        car_update (CarUpdate): The updated car data.

    Raises:
        NoResultFound: If the car does not exist.

    Returns:
        CarModel: The updated car.
    """
    db_car = db.query(CarModel).filter(CarModel.id == car_id).first()
    
    if db_car is None:
        raise NoResultFound()

    db_car.brand = car_update.brand
    db_car.model = car_update.model
    db_car.production_date = car_update.production_date
    db_car.owner_id = car_update.owner_id

    db.commit()
    db.refresh(db_car)
    
    return db_car