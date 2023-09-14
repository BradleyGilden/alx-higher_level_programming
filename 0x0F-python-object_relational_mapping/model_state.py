#!/usr/bin/python3

"""
This module defines a State class for states table

Author: Bradley Dillion Gilden
Date: 14-09-2023
"""

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """This class is blueprint for the states table

    __tablename__ (str): the name of the table
    id (sqlalchemy.Integer): The state's id.
    name (sqlalchemy.String): The state's name.
    """
    __tablename__ = "states"

    id = Column('id', Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column('name', String(length=128), nullable=False)
