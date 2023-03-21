#!/usr/bin/python3
"""Module for State class"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """Class representing the states table"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    def __str__(self):
        """Return a string representation of the State instance"""
        cities_list = [city.__str__() for city in self.cities]
        if len(cities_list) > 0:
            return "{}: {}".format(self.id, self.name) + "\n\t" + "\n\t".join(cities_list)
        else:
            return "{}: {}".format(self.id, self.name) + "\n\t" + "No cities"
