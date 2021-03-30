#!/usr/bin/python3
"""
This module defines new engine DBStorage
"""

from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.state import State
from models.city import City
from models.base_model import BaseModel, Base

class DBStorage:
    """
    Class definition
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Constructor
        """

        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                        .format(HBNB_MYSQL_USER,
                                        HBNB_MYSQL_PWD,
                                        HBNB_MYSQL_HOST,
                                        HBNB_MYSQL_DB),
                                        pool_pre_ping=True)

        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

        def all(self, cls=None):
            """
            return a dictionary with all objects depending on class name
            """
            if cls is not None:
                filter_dict = {}
                for objects in self.__session.query(cls): # .filter(cls)
                    key = objects.__class__.__name__ + '.' + objects.id
                    filter_dict[key] = objects
                return filter_dict
            else:
                all_dict = {}
                for objects in self.__session:
                    for key, value in objects.items():
                        all_dict[key] = value
                return all_dict

        def new(self, obj):
            """"add the object to the current database session"""
            self.__session.add(obj)

        def save(self):
            """
            Commit all changes of the current database session
            """
            self.__session.commit()

        def delete(self, obj=None):
            """
            delete from the current database session obj if not None
            """
            if obj is not None:
                self.__session.delete(obj)

        def reload(self):
            """create all tables in the database"""
            # ¿?
            Base.metadata.create_all(self.__engine)
            # call_session is the factory
            call_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
            Session = scoped_session(call_session)
            self.__sesion = Session