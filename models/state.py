#!/usr/bin/python3
""" State Module for HBNB project """
import shlex
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City
import models


class State(BaseModel):
    """ State class to represents new state"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",
                          cascade='all, delete, delete-orphan',
                          backref="state")
    @property
    def cities(self):
        "Getter method for city calss"
        cities = models.storage.all()
        cities_dict = []
        result = []
        for key in cities:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'city'):
                cities_dict.append(cities[key])
        for key in cities_dict:
            if (key.state_id == self.id):
                result.append(key)
        return result
