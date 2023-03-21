#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_101_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == '__main__':
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine and session
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{db_name}',
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects and access corresponding State object using the relationship
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print(f'{city.id}: {city.name} -> {city.state.name}')
