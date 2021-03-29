#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from models.engine.db_storage import DBStorage
from os import getenv
from sqlalchemy.orm import relationship
from models.city import City
from models import storage
HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ State class """

    if HBNB_TYPE_STORAGE == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        # If State object is deleted, all linked City objects must be automatically deleted.
        cities = relationship("City", backref="state")
    else:
        name = ""

    if HBNB_TYPE_STORAGE != "db":
        @property
        def cities(self):
            """
            Getter attribute to list City instaces
            """
            new_list = []
            all_cities = storage.__objects.all(City):
            for city in all_cities:
                if city.state_id == self.id:
                    new_list.append(city)
            return new_list
