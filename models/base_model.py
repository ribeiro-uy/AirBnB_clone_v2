#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
import models

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), unique=True, primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    # created_at = Column(datetime.utcnow()), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if args:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        elif kwargs:  # A dictionary given at creation will be in a tuple.
            for dictionary in kwargs:
                for key, value in dictionary.items():
                    if key != '__class__':
                        if key == "created_at" or key == "updated_at":
                            setattr(self, key, datetime.
                                    strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                        else:
                            setattr(self, key, value)
        else:  # No arguments at the time of creation.
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        # Move the models.storage.new(self)
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        # agregar lo mismo que delete
        to_delete = "_sa_instance_state"
        # ¿Estás son las keys?  
        for element in dictionary.key():
            print(element)
        for key, value in dictionary.items():
            if to_delete == key:
                del dictionary[key]
        # if to_delete in dictonary:
            # del dictonary[to_delete]
        return dictionary

    def delete(self):
        """delete the current instance from the storage"""
        storage.delete(self)