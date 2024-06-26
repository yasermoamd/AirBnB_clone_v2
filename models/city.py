#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.place import Place

class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    state_id = Column(String(128), nullable=False)
    name = Column(String(60), ForeignKey('state.id'),
                  nullable=False)
    places = relationship("Place",
                          cascade='all, delete, delete-orphan',
                          backref="cities")
