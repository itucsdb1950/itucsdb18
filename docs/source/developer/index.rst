Developer Guide
===============

Database Design
---------------

Explanations
^^^^^^^^^^^^
* Our database has 9 main tables. Their names are foods, menu, person, student, enrollment, grades, class, faculty and location.
* In foods table we have different types of eatables of a repast. A repast has mainly four types of foods: soup, main, side and extras. Also there is calorie value of each food.
* Menu tables keeps the repast menu of a day, which has mainly four types of foods from foods table and every day has two different repast as lunch and dinner.
* Person table has information about a student or a lecturer. These persons created and took id, username and password by admin users . In addition to them, person have name and age information too.
* When adding a person if the faculty information of person is entered, then that person becomes a student otherwise person added to system as a lecturer.
* Student table exists students' id, which is primary key, gpa numbers in d.dd format, completed credits number and faculty id which foreign key which refers to id in faculty.
* I faculty table there are faculty names, deans' id and student delegate information as in primary key of id.
* There is grades table which keeps to students' grades and which grades taken from which examination how many percentage is effective, and end grade information.
* Also enrollment table keeps how many attendance is there each student in each crn.
* In location table there exist classroom, building, day and capacity. That gives knowledge of the lesson's location ,time and how many people can enroll that lesson.
* Finally, class table keeps the crn numbers, location info referenced from location table, course code which need for student to enroll the classes, and credits of lessons.

**Database E/R diagram**

.. figure:: ../ss/diagram.png
  :scale: 75 %
  :align: center
  :alt: map to buried treasure


Code
----

**We have mainly 'views.py' as a header file which keeps database operations functions and 'server.py' to run and manage the website pages.**

VIEWS
^^^^^
* There are 48 functions in views.py which making operations about data management.
* Get functions read the necessary part of DB send them to server.py.
* Del functions delete the selected parts from DB.
* Add functions adds the intended sections of tables to DB.
* Update functions change the selected parts of DB.
* Check functions looks the some conditions to check whether the condition certain or not. This is important while deleting or updating some referenced keys.

SERVER
^^^^^^
* The main aim of server.py is running the server and coordinate the relations of pages.
* Almost all functions in this file correspond with a page of the website.
* Some pages run with get, some of them with post and some of them run with both get and post method. This is determined according to the data will send or receive.
* @app.route functools gives the address of the page to url.
* @allow_to functools decide the pages are able to entered with unauthorised users or not.


.. toctree::

   member1
   member2
   member3
