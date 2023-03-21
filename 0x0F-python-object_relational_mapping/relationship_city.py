#!/usr/bin/python3
"""Module for City class"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    """Class representing the cities table"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)

    def __str__(self):
        """Return a string representation of the City instance"""
        return "{}: ({}) {}".format(self.state.name, self.id, self.name)
