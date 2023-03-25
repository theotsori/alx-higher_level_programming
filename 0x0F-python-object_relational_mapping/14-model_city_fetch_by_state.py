#!/usr/bin/python3
"""Lists all City objects from the database hbtn_0e_14_usa"""

from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City


if __name__ == '__main__':
    # Connect to the database
    user = argv[1]
    password = argv[2]
    dbname = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, password, dbname))

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query all cities and print them by state
    for state, city in session.query(State, City) \
            .filter(State.id == City.state_id).order_by(City.id):
        print('{}: ({}) {}'.format(state.name, city.id, city.name))

    # Close the session
    session.close()
