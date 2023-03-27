#!/usr/bin/python3
"""Script that creates the State California with the City San Francisco"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys


if __name__ == '__main__':
    USER = sys.argv[1]
    PASSWORD = sys.argv[2]
    DATABASE = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(USER, PASSWORD, DATABASE),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name='California')
    san_francisco = City(name='San Francisco')

    california.cities.append(san_francisco)

    session.add(california)
    session.add(san_francisco)

    session.commit()
    session.close()
