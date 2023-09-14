#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
sys.path.append('/home/nightlock/workspace/Python/alx-higher_level_programming/0x0F-python-object_relational_mapping')
from sqlalchemy import (create_engine)
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
