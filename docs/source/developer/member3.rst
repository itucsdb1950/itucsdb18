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


ADMIN LOGIN
^^^^^^^^^^^

With this function users who is not login as a correct username and password are not able to enter the pages requiring permission.
All these page functions in 'server.py' has starts with that @allow_to functool. If the user enter the wrong username or password this function direct them to 'forbidden_page' page.

.. code-block::

  def allow_to():
      def decorator_let_to(view_func):
          @functools.wraps(view_func)
          def wrapper_view_func(*args, **kwargs):
              user = views.check_user(tabe['username'] , tabe['password'])
              if user:
                  returned_value = view_func(*args, **kwargs)
              else:
                  return redirect(url_for(forbidden_403.__name__))
          return returned_value
      return wrapper_view_func
  return decorator_let_to
