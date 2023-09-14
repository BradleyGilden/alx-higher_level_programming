#!/usr/bin/python3

"""
 a script that prints the first State object from the database hbtn_0e_6_usa
Author: Bradley Dillion Gilden
Date: 14-09-2023
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()
    print("{}: {}".format(state.id, state.name))
    session.close()
