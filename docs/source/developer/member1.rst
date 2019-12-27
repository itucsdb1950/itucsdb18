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



Some example functions of server.py and views.py are given below
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Views
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


**Add Menus**

.. code-block::

    def add_meal(day, repast, soup, main, side, extras):
        statement = "INSERT INTO MENU(dy, repast, soup, main, side, extras) VALUES('{}', '{}', '{}', '{}', '{}', '{}')".format(day, repast, soup, main, side, extras)

        with dbapi2.connect(db_url) as connection:
            with connection.cursor() as cursor:
                cursor.execute(statement)

* With this function admin user are able to add food menus to menu tables in DB.

**Update Menu**

.. code-block::

    def update_meal(day, repast, soup, main, side, extras, m_day, m_repast, m_soup, m_main, m_side, m_extras):
        statement = """UPDATE menu
                        SET dy='{}',repast='{}',soup='{}', main='{}',dise='{}',extras='{}'
                        WHERE dy='{}' and repast='{}' and soup='{}' and main='{}' and dise='{}' and extras='{}'
                        """.format(m_day, m_repast, m_soup, m_main, m_side, m_extras, day, repast, soup, main, side, extras)

        with dbapi2.connect(db_url) as connection:
            with connection.cursor() as cursor:
                cursor.execute(statement)

* This function allow the admin to change the menus in DB.

Server
^^^^^^

**Admin Meal Page**

.. code-block::

    @app.route("/admin/meal")
    @allow_to()
    def admin_meal_page():
        meals = views.get_meal()
        food = views.get_food()
        menu = views.get_food_menus()

        return render_template("admin_meal.html", meals=meals, food=food, menus=menu)

* With given function http://itucsdb1950.herokuapp.com/admin/meal page shows the meal menus with getting their data from views.get functions.

**Delete Menu**

.. code-block::

    @app.route("/del_meal/<string:dy>/<string:repast>", methods=['GET'])
    @allow_to()
    def del_meal(dy, repast):
        views.del_meal(dy, repast)
        return redirect(url_for('admin_meal_page'))

* With this function admin users are able to delete some meal menu tuples from DB.