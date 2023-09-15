#!/usr/bin/python3

"""
a script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa

Author: Bradley Dillion Gilden
Date: 14-09-2023
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter_by(name=argv[4]).all()
    if states:
        for state in states:
            print(state.id)
    else:
        print('Not Found')
    session.close()
