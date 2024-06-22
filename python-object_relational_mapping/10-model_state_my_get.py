#!/usr/bin/python3
"""Start link class to table in database"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    db_api = 'mysql+mysqldb://{}:{}@localhost/{}'
    usr = sys.argv[1]
    pswd = sys.argv[2]
    db = sys.argv[3]
    state = sys.argv[4]

    engine = create_engine(db_api.format(usr, pswd, db), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.like(state)).scalar()
    if states is not None:
        print(states.id)
    else:
        print("Not found")
