#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
import models
from os import getenv
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """

    if models.typestorage == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        # If State object is deleted, all linked City objects must be automatically deleted.
        cities = relationship("City", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if models.typestorage != "db":
        @property
        def cities(self):
            """
            Getter attribute to list City instaces
            """
            new_list = []
            all_cities = models.storage.__objects.all(City)
            for city in all_cities:
                if city.state_id == self.id:
                    new_list.append(city)
            return new_list
