CREATE TABLE PERSON (
	id CHAR(9) PRIMARY KEY,
	name VARCHAR(20),
	age INTEGER,
	username VARCHAR(10),
	password VARCHAR(15)
);
CREATE INDEX person_name ON person(name);

CREATE TABLE QUIZ (
	quiz_numb INTEGER NOT NULL,
	ques_numb INTEGER NOT NULL,
	ques_text VARCHAR(250) NOT NULL,
	right_ans VARCHAR(25) NOT NULL,
	wrong_ans1 VARCHAR(25) NOT NULL,
	wrong_ans2 VARCHAR(25),
	wrong_ans3 VARCHAR(25),
	PRIMARY KEY(quiz_numb,ques_numb)
);


CREATE TABLE ANSWERS (
	quiz_numb INTEGER NOT NULL,
	ques_numb INTEGER NOT NULL,
	id CHAR(9),
	given_ans VARCHAR(25)NOT NULL,
	PRIMARY KEY (quiz_numb,ques_numb,id),
	FOREIGN KEY (id) REFERENCES person(id)
);

ALTER TABLE PERSON
ADD CHECK (age>=18); 


CREATE TABLE CLASS (
	crn INT(5),
	course_code VARCHAR(7),
	loc_id INT(5) FOREIGN KEY REFERENCES LOCATION(loc_id),
	credit INT(1),

);


CREATE TABLE LOCATION (
	class VARCHAR(10),
	building CHAR(3),
	day CHAR(3),
	start_time TIME(),
	end_time TIME(),
	year YEAR,
	loc_id INT(5) PRIMARY KEY
);

CREATE TABLE LOCATION (
	dep_id INT(4),
	dep_name VARCHAR(30),
	fac_name VARCHAR(30),
	dean_id INT FOREIGN KEY REFERENCES PERSON(id),
	stu_delegate INT FOREIGN KEY REFERENCES PERSON(id)
	
);

