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

Some example functions of server.py and views.py are given below
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Views
^^^^^^

**Delete Location**

.. code-block::

    def del_location(id):
        statement = "DELETE FROM location WHERE id = '{}'".format(id)

        with dbapi2.connect(db_url) as connection:
            with connection.cursor() as cursor:
                cursor.execute(statement)


* This function allow the admin user to delete location tuples from DB.

**Get Location**

.. code-block::

    def get_locations(limit=100):
        statement = "SELECT * FROM location LIMIT {}".format(limit)

        with dbapi2.connect(db_url) as connection:
            with connection.cursor() as cursor:
                cursor.execute(statement)
                records = cursor.fetchall()
                return records

* This function takes the location information from DB and send the server.py.

**Update Location**

.. code-block::

    def update_location(old_id, building, day, classroom, capacity):
        statement = """
                    UPDATE location
                        SET classroom='{}',building='{}',dy='{}',capacity='{}'
                        WHERE (id='{}')
                        """.format(classroom, building, day, capacity, old_id)

* With this function admin user can update the location tuples in DB.


Server
^^^^^^

.. code-block::

    @app.route("/admin/location")
    @allow_to()
    def admin_location_page():
        locations = views.get_locations()

        return render_template("admin_location.html", locations=locations)

* Given above function let the http://itucsdb1950.herokuapp.com/admin/location page run and takes related tables informations and show them in the website.

.. code-block::

    @app.route("/add_location", methods=['POST'])
    @allow_to()
    def add_location():
        building = request.form.get('building')
        day = request.form.get('day_sel')
        classroom = request.form.get('classroom')
        capacity = request.form.get('capacity')
        if views.check_location(building, day, classroom):
            views.add_location(building, day, classroom, capacity)
        return redirect(url_for('admin_location_page'))

* With this function admin user can add some locations to DB. Also this function too takes the data from get functions of views.py.