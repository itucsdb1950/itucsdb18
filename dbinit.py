import os
import sys

import psycopg2 as dbapi2


INIT_STATEMENTS = [
	# KUTAY KARAKAMIŞ
	# "CREATE TABLE IF NOT EXISTS DUMMY (NUM INTEGER)",
	# "INSERT INTO DUMMY VALUES (42)",
	# "CREATE TABLE PERSON (id CHAR(9) PRIMARY KEY, name VARCHAR(20), age INTEGER, username VARCHAR(10), password VARCHAR(15))",
	# "CREATE INDEX person_name ON person(name)",
	# "CREATE TABLE QUIZ ( quiz_numb INTEGER NOT NULL, ques_numb INTEGER NOT NULL, ques_text VARCHAR(250) NOT NULL, right_ans VARCHAR(25) NOT NULL, wrong_ans1 VARCHAR(25) NOT NULL, wrong_ans2 VARCHAR(25), wrong_ans3 VARCHAR(25), PRIMARY KEY(quiz_numb,ques_numb));",
	# "CREATE TABLE ANSWERS (quiz_numb INTEGER NOT NULL, ques_numb INTEGER NOT NULL, id CHAR(9), given_ans VARCHAR(25)NOT NULL, PRIMARY KEY (quiz_numb,ques_numb,id), FOREIGN KEY (id) REFERENCES person(id));",
	# "ALTER TABLE PERSON ADD CHECK (age>=18);" ,
	
	# ENES FURKAN ÖRNEK
	"CREATE TABLE LOCATION (class VARCHAR(10) PRIMARY KEY, building CHAR(3), day CHAR(3), start_time TIME, end_time TIME, year NUMERIC(4), loc_id NUMERIC(5) PRIMARY KEY);",
	"CREATE TABLE CLASS (crn CHAR(5) PRIMARY KEY, course_code VARCHAR(7), loc_id NUMERIC(5) REFERENCES LOCATION(loc_id), credit NUMERIC(1));",
	"CREATE TABLE DEPARTMENT (dep_id CHAR(4), dep_name VARCHAR(30), fac_name VARCHAR(30), dean_id CHAR(9) REFERENCES PERSON(id), stu_delegate CHAR(9) REFERENCES PERSON(id));",
	
	# MEHMET FATİH YILDIRIM
	"""
	CREATE TABLE STUDENT (
		ID CHAR(9) PRIMARY KEY REFERENCES PERSON,
		GPA NUMERIC(3, 2),
		COMP_CREDITS INT NOT NULL DEFAULT 0,
		DEP_ID NUMERIC(4) REFERENCES DEPARTMENT NOT NULL,
		CHECK (COMP_CREDITS >= 0),
		CHECK (GPA >= 0) AND (GPA <= 4)
	)
	""",
	"""
	CREATE TABLE ENROLLMENT (
		ID CHAR(9) REFERENCES PERSON NOT NULL,
		CRN CHAR(5) REFERENCES CLASS NOT NULL,
		ATTENDANCE INT,
		CHECK (ATTENDANCE >= 0),
		PRIMARY KEY (ID, CRN)
	)
	""",
	"""
	CREATE TABLE GRADES (
		ID CHAR(9) REFERENCES PERSON NOT NULL,
		CRN CHAR(5) REFERENCES CLASS NOT NULL,
		TAKEN_FROM VARCHAR(15) NOT NULL,
		PERCENTAGE INT NOT NULL,
		GRADE INT NOT NULL,
		CHECK (PERCENTAGE >= 0) AND (PERCENTAGE <= 100),
		CHECK (GRADE >= 0) AND (GRADE <= 100),
		PRIMARY KEY (ID, CRN, TAKEN_FROM)
	)
	"""
]


def initialize(url):
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        for statement in INIT_STATEMENTS:
            cursor.execute(statement)
        cursor.close()


if __name__ == "__main__":
    url = os.getenv("DATABASE_URL")
    if url is None:
        print("Usage: DATABASE_URL=url python dbinit.py", file=sys.stderr)
        sys.exit(1)
    initialize(url)
