#!/usr/bin/python3

"""
Lists all City objects from the database hbtn_0e_101_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City


def main():
    """
    Lists all City objects from the database hbtn_0e_101_usa.

    This script lists all the City objects from the database hbtn_0e_101_usa,
    along with their corresponding State objects.

    Args:
        None.

    Returns:
        None.
    """
    # Get the username, password, and database name from the command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create an SQLAlchemy engine and session
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{db_name}',
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects and print their details
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print(f'{city.id}: {city.name} -> {city.state.name}')


if __name__ == '__main__':
    main()
