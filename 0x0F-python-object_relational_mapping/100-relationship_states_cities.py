#!/usr/bin/python3
# Adds the State "California" with the City "San Francisco"
# to the database hbtn_0e_100_usa using SQLAlchemy and
# the cities relationship for all State objects.


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    # Create an engine to the database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Create a new State and City objects
    new_state = State(name="California")
    new_city = City(name="San Francisco")

    # Add the new City to the new State's cities relationship
    new_state.cities.append(new_city)

    # Add the new State to the session and commit changes
    session.add(new_state)
    session.commit()

    # Close the session
    session.close()
