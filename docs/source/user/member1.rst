Parts Implemented by Kutay Karakamış
====================================

There are various sections to make some CRUD operations in DB.

CRN
^^^
.. figure:: ../ss/admin-crn.png
  :scale: 50 %
  :alt: map to buried treasure

  http://itucsdb1950.herokuapp.com/admin/location

* In this page admin user can add CRN to table and read, delete a CRN from table.
* CRN has attributes of CRN, course code, location which referenced from location table and credits.
* CRN attribute is identifier of class which has no same features and it is 5-digit number.
* Course code gives the information of lesson's related department, it is generally abbreviation of departments i.e.: BLG, ELK, EHB etc.
* Location referenced from location table and contain its attributes. Therefore to create a CRN at least one tuple must be in the location table.
* Credits take number from 1 to 5.



Department
^^^^^^^^^^
.. figure:: ../ss/admin-department.png
  :scale: 50 %
  :alt: map to buried treasure

  http://itucsdb1950.herokuapp.com/admin/department

* In this page admin user can add department to table and update, read, delete a department from table.
* Department has attributes of department name, dean which is professor person from person table, and student delegate with optional.
* With update button admin user can make some change at table.

Food
^^^^
.. figure:: ../ss/admin-food.png
  :scale: 50 %
  :alt: map to buried treasure

  http://itucsdb1950.herokuapp.com/admin/food

* In this page admin user can add food to table and read, delete a person from table.
* Food has attributes of food type, food name and calorie.
* Food type has four different option which are soup, main, side and extras.

Menu
^^^^
.. figure:: ../ss/admin-menu.png
  :scale: 50 %
  :alt: map to buried treasure

  http://itucsdb1950.herokuapp.com/admin/meal

* In this page admin user can add meal to table and read, delete a meal from table.
* Meal has attributes of day, repast, soup, main, side and extras.
* Every repast of days are unique and has mainly four types of foods.
* Day and repast sections form selection feature which keeps days of weeks and lunch and dinner as repast.
* Foods are reference the foods from table, with selecting them admin user can make different menus.

Grades
^^^^^^
.. figure:: ../ss/admin-grades.png
  :scale: 50 %
  :alt: map to buried treasure

  http://itucsdb1950.herokuapp.com/admin/grades

* In this page admin user can add grades to table and read, delete a grade from table.
* Grades have attributes of CRN which referenced from CRN table, student id which referenced from student table, taken-from, percentage, grade.
* Taken from is name of the examination.
* Percentage is the number of percentage the examination affects the all grade.




