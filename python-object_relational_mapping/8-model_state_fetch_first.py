#!/usr/bin/python3
"""Module 8-model_state_fetch_first"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    """Print the first State object from database hbtn_0e_6_usa"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{database}"
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).order_by(State.id).first()
    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")
    session.close()
