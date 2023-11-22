#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from sqlalchemy import (create_engine)
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    connection = engine.connect()
    result = connection.execute('SELECT * FROM states')
    [print(f"{elem[0]}: {elem[1]}") for elem in result]