#!/usr/bin/python3

"""
This module defines a City class for cities table

Author: Bradley Dillion Gilden
Date: 14-09-2023
"""

from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base


class City(Base):
    """This class is blueprint for the states table

    __tablename__ (str): the name of the table
    id (sqlalchemy.Integer): The city's id.
    name (sqlalchemy.String): The city's name.
    state_id(sqlalchemy.Integer): Foreign Key reference to state
    """
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(length=128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
