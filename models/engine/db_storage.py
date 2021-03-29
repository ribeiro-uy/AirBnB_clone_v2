#!/usr/bin/python3
"""This module defines new engine DBStorage"""

class DBStorage:
    """Class definition"""

    HBNB_MYSQL_USER = 'hbnb_dev'
    HBNB_MYSQL_PWD = 
    HBNB_MYSQL_HOST = 'localhost'
    HBNB_MYSQL_DB = the database name of your MySQL
    
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

the engine must be linked to the MySQL database and user created before (hbnb_dev and hbnb_dev_db):
# dialect: mysql
# driver: mysqldb
all of the following values must be retrieved via environment variables:
MySQL user: HBNB_MYSQL_USER
MySQL password: HBNB_MYSQL_PWD
MySQL host: HBNB_MYSQL_HOST (here = localhost)
MySQL database: HBNB_MYSQL_DB
don’t forget the option pool_pre_ping=True when you call create_engine
drop all tables if the environment variable HBNB_ENV is equal to test