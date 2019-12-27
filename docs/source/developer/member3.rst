Parts Implemented by Enes Furkan Örnek
======================================

Tables
------

There are three main tables as in the Figure, these tables keeps person,
student and location information.

.. figure:: ../ss/efo.jpg
  :scale: 70 %
  :alt: map to buried treasure

Tables and their sql codes are like given below:

PERSON
^^^^^^
.. code-block:: sql

  CREATE TABLE IF NOT EXISTS PERSON (
    id CHAR(9) PRIMARY KEY,
    name VARCHAR(20),
    age INTEGER,
    username VARCHAR(10),
    password VARCHAR(15)
  );

.. figure:: ../ss/person.png
  :scale: 100 %
  :align: center
  :alt: map to buried treasure

STUDENT
^^^^^^^
.. code-block:: sql

  CREATE TABLE IF NOT EXISTS STUDENT (
    ID CHAR(9) PRIMARY KEY NOT NULL REFERENCES PERSON(id) ON DELETE CASCADE,
    GPA NUMERIC(3, 2) DEFAULT NULL,
    COMP_CREDITS INT NOT NULL DEFAULT 0,
    FAC_ID INTEGER REFERENCES FACULTY(id) ON DELETE CASCADE NOT NULL,
    CHECK (COMP_CREDITS >= 0),
    CHECK (GPA >= 0),
    CHECK (GPA <= 4)
  );

.. figure:: ../ss/student.png
  :scale: 100 %
  :align: center
  :alt: map to buried treasure

LOCATION
^^^^^^^^^^

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