import os
import sys

import psycopg2 as dbapi2

DSN = {'user' : "postgres",
	  'password' : "123",
	  'host' : "127.0.0.1",
	  'port' : "5432",
	  'database' : "scholar"}

def check_user(username, password):
	statement = "SELECT * FROM PERSON WHERE username = '{}' AND password = '{}'".format(username, password)

	with dbapi2.connect(**DSN) as connection:
		with connection.cursor() as cursor:
			cursor.execute(statement)
			record = cursor.fetchone()
			return record
			
if __name__ == '__main__':
	check_user("kkarakamis", "1234")
