#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_101_usa.
Usage: ./102-relationship_cities_states_list.py <mysql username> /
                                                <mysql password> /
                                                <database name>
"""
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv


if __name__ == "__main__":
    eng = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    rows = session.query(City).all()
    for city in rows:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    session.close()
