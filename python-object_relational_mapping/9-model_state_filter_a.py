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

    engine = create_engine(db_api.format(usr, pswd, db), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State).filter(State.name.like('%a%'))
    idx = "{}:"

    for states in results:
        if states is not None:
            print(idx.format(states.id), states.name)
        else:
            print("Nothing")
