Parts Implemented by Enes Furkan Örnek
======================================

Person
^^^^^^
.. figure:: ../ss/admin-person.png
  :scale: 50 %
  :alt: map to buried treasure

  http://itucsdb1950.herokuapp.com/admin/persons

* In this page admin user can add person to table and read, delete a person from table.
* Person has attributes of name, person id, username, password, age and the faculty to identify the person is a student or not.
* Name section takes person's name and surname information.
* Person id is a key variable to identify persons and it is generally 9-digit number but it may differ.
* Username and password are given person to enter the website.
* Age info is important to check the person is at university age and it must be at least 18.
* In department section is optional. If the department is selected, then the person becomes student otherwise person creates as professor automatically.

Forbidden Pages
^^^^^^^^^^^^^^^

*In case of trying to enter a page which is not your authority let to or entering wrong username and password, this page welcomes you.*

.. figure:: ../ss/Gandalf.png
  :scale: 50 %
  :alt: map to buried treasure

  http://itucsdb1950.herokuapp.com/403_forbidden

Not Found Pages
^^^^^^^^^^^^^^^

*If user tries to enter a nonexistent page, this page encounters you.*

.. figure:: ../ss/notFound.png
  :scale: 50 %
  :alt: map to buried treasure

  http://itucsdb1950.herokuapp.com/something