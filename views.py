import os
import sys

import psycopg2 as dbapi2
from configs import db_url

DSN = {'user': "postgres",
       'password': "123",
       'host': "127.0.0.1",
       'port': "5432",
       'database': "scholar"}


def check_user(username, password):
    statement = "SELECT * FROM PERSON WHERE username = '{}' AND password = '{}'".format(username, password)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)
            record = cursor.fetchone()
            return record


def add_location(building, day, classroom, capacity):
    statement = "INSERT INTO LOCATION(class, building, day, capacity) VALUES('{}', '{}', '{}', '{}')".format(building, day, classroom, capacity)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)


def get_locations(limit=100):
    statement = "SELECT * FROM location LIMIT {}".format(limit)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)
            records = cursor.fetchall()
            return records


def check_location(building, day, classroom):
    statement = "SELECT * FROM location WHERE building = '{}' AND day = '{}' AND class = '{}'".format(building, day, classroom)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)
            record = cursor.fetchone()
            return record is None


def del_location(id):
    statement = "DELETE FROM location WHERE id = '{}'".format(id)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)


if __name__ == '__main__':
    check_user("kkarakamis", "1234")
