Parts Implemented by Kutay Karakamış
====================================

Tables
------

There are three main tables as in the Figure, these tables keeps foods,
meal menus and class information.

.. figure:: ../ss/kutay.jpg
  :scale: 70 %
  :alt: map to buried treasure

Tables and their sql codes are like given below:

CLASS
^^^^^
.. code-block:: sql

  CREATE TABLE IF NOT EXISTS CLASS (
    crn INTEGER PRIMARY KEY NOT NULL ,
    course_code VARCHAR(7),
    loc_id INTEGER REFERENCES LOCATION(id) ON DELETE SET NULL,
    credit NUMERIC(1)
  );

.. figure:: ../ss/class.png
  :scale: 100 %
  :align: center
  :alt: map to buried treasure

FOODS
^^^^^
.. code-block:: sql

  CREATE TABLE IF NOT EXISTS FOODS (
    id SERIAL PRIMARY KEY NOT NULL,
    food_type VARCHAR(15),
    food_name VARCHAR(255),
    calorie INT
  );

.. figure:: ../ss/foods.png
  :scale: 100 %
  :align: center
  :alt: map to buried treasure

MENU
^^^^

.. code-block:: sql

  CREATE TABLE IF NOT EXISTS MENU (
    dy VARCHAR(15),
    repast VARCHAR(20),
    soup INTEGER,
    main INTEGER,
    side INTEGER,
    extras INTEGER,
    PRIMARY KEY(dy, repast),
    FOREIGN KEY(soup) REFERENCES FOODS(id),
    FOREIGN KEY(main) REFERENCES FOODS(id),
    FOREIGN KEY(side) REFERENCES FOODS(id),
    FOREIGN KEY(extras) REFERENCES FOODS(id)
  );

.. figure:: ../ss/menu.png
  :scale: 100 %
  :align: center
  :alt: map to buried treasure

Python
^^^^^^

**Get Food Menus**

.. code-block::

    def get_food_menus():
    statement = """
                SELECT menu.dy AS day, menu.repast AS repast,
                       foods.food_name AS name, foods.calorie AS calories, foods.food_type
                    FROM menu, foods
                    WHERE ( (menu.soup = foods.id)
                        OR (menu.main = foods.id)
                        OR (menu.side = foods.id)
                        OR (menu.extras = foods.id) )
                    ORDER BY menu.dy, menu.repast
                """

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)
            records = cursor.fetchall()
            return records

* This function shows the food menus both in admin and students food_menu pages.

**Delete Menus**

.. code-block::

    def del_meal(day, repast):
    statement = "DELETE FROM MENU WHERE ((dy = '{}') and( repast = '{}'))".format(day, repast)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)

* With this function admin user are able to delete food menus from DB.