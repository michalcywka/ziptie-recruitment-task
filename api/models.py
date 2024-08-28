from sqlalchemy import Column, String, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from database import Base

class OwnerModel(Base):
    """
    Represents an owner of cars.

    Attributes:
        id (int): The unique identifier for the owner.
        name (str): The first name of the owner.
        last_name (str): The last name of the owner.
        email (str, optional): The email address of the owner.
        cars (relationship): A relationship to the `CarModel` class, representing the cars owned by this owner.
    """
    __tablename__ = "owners"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(40), nullable=False)
    last_name = Column(String(60), nullable=False)
    email = Column(String(120))

    cars = relationship("CarModel", back_populates="owner")

class CarModel(Base):
    """
    Represents a car owned by an owner.

    Attributes:
        id (int): The unique identifier for the car.
        brand (str): The brand of the car.
        model (str): The model of the car.
        production_date (date, optional): The production date of the car.
        owner_id (int, optional): The foreign key linking to the `OwnerModel` representing the owner of the car.
        owner (relationship): A relationship to the `OwnerModel` class, representing the owner of this car.
    """
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String(20), nullable=False)
    model = Column(String(30), nullable=False)
    production_date = Column(Date)
    owner_id = Column(Integer, ForeignKey('owners.id'), nullable=True)

    owner = relationship("OwnerModel", back_populates="cars")

