#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()