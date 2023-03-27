#!/usr/bin/python3
"""
Lists all State objects and corresponding City objects contained in the
database specified by the command-line arguments.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City


if __name__ == '__main__':
    username, password, db_name = sys.argv[1:]
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}',
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")

    session.close()
    engine.dispose()
