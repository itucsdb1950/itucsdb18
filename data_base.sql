CREATE TABLE PERSON (
	id CHAR(9) PRIMARY KEY,
	name VARCHAR(20),
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
