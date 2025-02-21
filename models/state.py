#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os

from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column('name', String(128), nullable=False)
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state", cascade="all, delete")

    else:
        @property
        def cities(self):
            """[For FileStorage] Returns the list of City in the State"""
            from models import storage
            # get all cities in the storage
            city_store = storage.all(City)
            # check for cities in this states
            cities = [city for city in city_store if city.state_id == self.id]
            return cities
