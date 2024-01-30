#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.place import Place
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from os import getenv


class City(BaseModel):
    """ The city class, contains state ID and name """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship('Place', cascade='all, delete-orphan', backref='cities')
    else:
        state_id = ""
        name = ""
