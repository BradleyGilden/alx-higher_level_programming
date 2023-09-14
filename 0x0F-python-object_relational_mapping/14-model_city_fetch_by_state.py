#!/usr/bin/python3

"""
a script 14-model_city_fetch_by_state.py that prints all City objects from
the database hbtn_0e_14_usa

Author: Bradley Dillion Gilden
Date: 14-09-2023
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    table = (
        session.query(State, City)
        .join(City, State.id == City.state_id)
        .order_by(City.id.asc())
    )

    for row in table:
        print("{}: ({}) {}".format(row[0].name, row[1].id, row[1].name))
    session.commit()
    session.close()
