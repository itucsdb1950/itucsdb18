Parts Implemented by Mehmet Fatih Yıldırım
==========================================

Tables
------

There are three main tables as in the Figure, these tables keeps location,
enrollment and grades information.

.. figure:: ../ss/fatih.jpg
  :scale: 70 %
  :alt: map to buried treasure

Tables and their sql codes are like given below:

LOCATION
^^^^^^^^
.. code-block:: sql

  CREATE TABLE IF NOT EXISTS LOCATION (
    id SERIAL PRIMARY KEY NOT NULL,
    classroom VARCHAR(255),
    building VARCHAR(255),
    dy VARCHAR(255),
    capacity INT DEFAULT 80
  );

.. figure:: ../ss/location.png
  :scale: 100 %
  :align: center
  :alt: map to buried treasure

GRADES
^^^^^^
.. code-block:: sql

  CREATE TABLE IF NOT EXISTS GRADES (
    STUDENT_ID CHAR(9) REFERENCES STUDENT(ID) NOT NULL,
    CRN INTEGER REFERENCES CLASS ON DELETE CASCADE NOT NULL,
    TAKEN_FROM VARCHAR(15) NOT NULL,
    PERCENTAGE INT NOT NULL,
    GRADE INT NOT NULL,
    CHECK (PERCENTAGE >= 0),
    CHECK (PERCENTAGE <= 100),
    CHECK (GRADE >= 0),
    CHECK (GRADE <= 100),
    PRIMARY KEY (STUDENT_ID, CRN, TAKEN_FROM)
  );

.. figure:: ../ss/grades.png
  :scale: 100 %
  :align: center
  :alt: map to buried treasure

ENROLLMENT
^^^^^^^^^^

.. code-block:: sql

  CREATE TABLE IF NOT EXISTS ENROLLMENT (
    STUDENT_ID CHAR(9) REFERENCES STUDENT(ID) NOT NULL,
    CRN INTEGER REFERENCES CLASS ON DELETE CASCADE NOT NULL,
    ATTENDANCE INT DEFAULT 0,
    CHECK (ATTENDANCE >= 0),
    PRIMARY KEY (STUDENT_ID, CRN)
  );

.. figure:: ../ss/enrollment.png
  :scale: 100 %
  :align: center
  :alt: map to buried treasure

Python
^^^^^^

**Add Enrollment**

.. code-block::

    def add_enrollment(crn, stu_num):
        statement = """
                INSERT INTO enrollment
                    (crn, student_id)
                    VALUES ('{}', '{}')
                """.format(crn, stu_num)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)

* This function allow the students enroll a class which exist in DB.

**Get Enrollment**

.. code-block::

    def get_enrolled(crn):
        statement = """
                    SELECT COUNT(student.id) FROM class, student, enrollment
                        WHERE ( (class.crn = enrollment.crn)
                            AND (student.id = enrollment.student_id)
                            AND (class.crn = '{}') )
                    """.format(crn)

        with dbapi2.connect(db_url) as connection:
            with connection.cursor() as cursor:
                cursor.execute(statement)
                record = cursor.fetchone()
                return record

* This function let the students see enrolled classes.

**Update Location**

.. code-block::

    def update_location(old_id, building, day, classroom, capacity):
    statement = """
                UPDATE location
                    SET classroom='{}',building='{}',dy='{}',capacity='{}a
                    WHERE (id='{}')
                    """.format(classroom, building, day, capacity, old_id)

* With this function admin user can update the location tuples in DB.