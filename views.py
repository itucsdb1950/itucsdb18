import os
import sys

import psycopg2 as dbapi2
from configs import db_url

DSN = {'user': "postgres",
       'password': "123",
       'host': "127.0.0.1",
       'port': "5432",
       'database': "scholar"}


def check_user(username, password):
    statement = "SELECT * FROM PERSON WHERE username = '{}' AND password = '{}'".format(username, password)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)
            record = cursor.fetchone()
            return record


def add_location(building, day, classroom, capacity):
    statement = "INSERT INTO LOCATION(classroom, building, dy, capacity) VALUES('{}', '{}', '{}', '{}')".format(building, day, classroom, capacity)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)


def get_locations(limit=100):
    statement = "SELECT * FROM location LIMIT {}".format(limit)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)
            records = cursor.fetchall()
            return records


def get_locations_for_crn(limit=100):
    statement = "SELECT * FROM location WHERE  NOT EXISTS (SELECT 3  FROM   class   WHERE  class.loc_id = location.id) LIMIT {}".format(limit)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)
            records = cursor.fetchall()
            return records


def check_location(building, day, classroom):
    statement = "SELECT * FROM location WHERE building = '{}' AND dy = '{}' AND classroom = '{}'".format(building, day, classroom)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)
            record = cursor.fetchone()
            return record is None


def del_location(id):
    statement = "DELETE FROM location WHERE id = '{}'".format(id)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)


def get_crns(limit=100):
    statement = "SELECT * FROM CLASS LIMIT {}".format(limit)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)
            records = cursor.fetchall()
            return records


def check_crn(crn, code, loc_sel):
    statement = "SELECT * FROM class WHERE crn = '{}' AND course_code = '{}' AND loc_id = '{}'".format(crn, code, loc_sel)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)
            record = cursor.fetchone()
            return record is None


def add_crn(crn, code, loc_sel, credits_sel):
    statement = "INSERT INTO CLASS(crn, course_code, loc_id, credit) VALUES('{}', '{}', '{}', '{}')".format(crn, code, loc_sel, credits_sel)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)


def del_crn(id):
    statement = "DELETE FROM class WHERE crn = '{}'".format(id)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)


def get_lesson(limit=500):
    statement = "SELECT * FROM class LEFT JOIN location ON class.loc_id = location.id"

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)
            records = cursor.fetchall()
            return records


def get_person(limit=500):
    statement = "SELECT * FROM person LEFT JOIN student ON person.id = student.id WHERE person.name <> 'ADMINISTRATOR'"

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)
            records = cursor.fetchall()
            return records


def add_person(per_name, per_num, usern, passw, age, fac):
    # ~statement="SELECT * FROM person WHERE username = '{}' ".format(usern)
    #TODO: If exists, don't add

    if int(age) < 18:
        return 1

    if fac:
        statement = """INSERT INTO person(id, name, age, username, password) VALUES('{}', '{}', '{}', '{}', '{}');
                        INSERT INTO STUDENT(id, fac_id) VALUES('{}','{}')""".format(per_num, per_name, age, usern, passw, per_num, fac)

    else:
        statement = "INSERT INTO person(id, name, age, username, password) VALUES('{}', '{}', '{}', '{}', '{}')".format(
            per_num, per_name, age, usern, passw)
    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)


def check_person(usern):
    statement = "SELECT * FROM person WHERE username = '{}' ".format(usern)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)
            record = cursor.fetchone()
            return record is None


def del_person(id):
    statement = "DELETE FROM person WHERE id = '{}'".format(id)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)


def check_grades(crn, stu_id, taken_from):
    statement = "SELECT * FROM grades WHERE crn = '{}' and student_id = '{}' and taken_from = '{}'".format(crn, stu_id, taken_from)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)
            record = cursor.fetchone()
            return record is None


def add_grades(crn, stu_id, taken_from, percentage, grade):
    statement = "INSERT INTO GRADES VALUES('{}', '{}', '{}', '{}', '{}')".format(stu_id, crn, taken_from, percentage, grade)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)


def get_grades_admin():
    statement = """
                SELECT class.crn AS crn, class.course_code AS course_code, 
                       grades.taken_from AS taken_from, grades.grade AS grade,
                       grades.percentage AS percent, class.credit AS credits
                    FROM student, grades, class
                    WHERE ( (student.id = grades.student_id)
                        AND (grades.crn = class.crn) )
                    ORDER BY class.crn
                """

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)
            records = cursor.fetchall()
            return records


def del_grades(student_id, crn,taken_from):
    statement = "DELETE FROM GRADES WHERE student_id = '{}' and crn = '{}' and taken_from = '{}'".format(student_id, crn,taken_from)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)


def get_department(limit=100):
    statement = "SELECT * FROM faculty LIMIT {}".format(limit)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)
            records = cursor.fetchall()
            return records


def add_department(dept, dean, delege):
    statement = "INSERT INTO FACULTY(fac_name, dean_id, stu_delegate) VALUES('{}', '{}', '{}')".format(dept, dean, delege)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)


def check_department(dept):
    statement = "SELECT * FROM faculty WHERE fac_name = '{}' ".format(dept)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)
            record = cursor.fetchone()
            return record is None


def del_department(id):
    statement = """
                DELETE FROM person
                    WHERE (id = ANY (
                        SELECT person.id FROM person, student
                            WHERE ((person.id = student.id)
                                AND (student.fac_id = {}))
                    ));
                
                DELETE FROM faculty WHERE id = {}
                """.format(id,id)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)


def get_food(limit=1000):
    statement = "SELECT * FROM FOODS LIMIT {}".format(limit)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)
            records = cursor.fetchall()
            return records


def add_food(type, name, calorie):
    statement = "INSERT INTO FOODS(food_type, food_name, calorie) VALUES('{}', '{}', '{}')".format(type, name, calorie)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)


def check_food(type,name):
    statement = "SELECT * FROM FOODS WHERE food_name = '{}' and food_type = '{}' ".format(name, type)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)
            record = cursor.fetchone()
            return record is None


def del_food(id):
    statement = "DELETE FROM FOODS WHERE id = '{}'".format(id)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)


def get_student_admin():
    statement = """
                SELECT person.name, person.username, student.id, faculty.fac_name, student.gpa, student.comp_credits
                    FROM student, person, faculty
                    WHERE ( (person.id = student.id)
                        AND (student.fac_id = faculty.id) )
                """

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)
            record = cursor.fetchone()
            return record


def get_dept_info():
    statement = """
                SELECT faculty.fac_name, faculty.dean_id AS dean_id, person.name
                    FROM faculty, person
                    WHERE ( (person.id = dean_id) or (dean_id is NULL) )
                """

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)
            records = cursor.fetchall()
            return records


def get_student(stu_num):
    statement = """
                SELECT person.name, person.username, student.id, faculty.fac_name, student.gpa, student.comp_credits
                    FROM student, person, faculty
                    WHERE ( (person.id = student.id)
                        AND (student.fac_id = faculty.id)
                        AND (student.id = '{}') )
                """.format(stu_num)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)
            record = cursor.fetchone()
            return record


def get_courses(stu_num):
    statement = """
                SELECT class.crn AS crn, class.course_code AS course_code, location.dy AS dy,
                       location.building AS building, location.classroom AS classroom, credits
                    FROM student, enrollment, class, location
                    WHERE ( (student.id = enrollment.student_id)
                        AND (enrollment.crn = class.crn)
                        AND (class.loc_id = location.id)
                        AND (student.id = '{}') )
                """.format(stu_num)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)
            records = cursor.fetchall()
            return records


def get_attendance(stu_num):
    statement = """
                SELECT class.crn AS crn, class.course_code AS course_code,
                       enrollment.attendance AS attendance
                    FROM student, enrollment, class
                    WHERE ( (student.id = enrollment.student_id)
                        AND (enrollment.crn = class.crn)
                        AND (student.id = '{}') )
                """.format(stu_num)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)
            records = cursor.fetchall()
            return records


def get_grades(stu_num):
    statement = """
                SELECT class.crn AS crn, class.course_code AS course_code, 
                       grades.taken_from AS taken_from, grades.grade AS grade,
                       grades.percentage AS percent, class.credit AS credits
                    FROM student, grades, class
                    WHERE ( (student.id = grades.student_id)
                        AND (grades.crn = class.crn)
                        AND (student.id = '{}') )
                    ORDER BY class.crn
                """.format(stu_num)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)
            records = cursor.fetchall()
            return records


def add_meal(day, repast, soup, main, side, extras):
    statement = "INSERT INTO MENU(dy, repast, soup, main, side, extras) VALUES('{}', '{}', '{}', '{}', '{}', '{}')".format(day, repast, soup, main, side, extras)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)

def del_meal(day, repast):
    statement = "DELETE FROM MENU WHERE dy = '{}', repast = '{}'".format(day, repast)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)

def get_meal(limit=100):
    statement = "SELECT * FROM MENU LIMIT {}".format(limit)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)
            records = cursor.fetchall()
            return records


def get_food_menus():
    statement = """
                SELECT menu.dy AS day, menu.repast AS repast,
                       foods.name AS name, foods.calorie AS calories, foods.food_type
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


# ~def add_location(building, day, classroom, capacity):
# ~statement = "INSERT INTO LOCATION(classroom, building, dy, capacity) VALUES('{}', '{}', '{}', '{}')".format(building, day, classroom, capacity)

# ~with dbapi2.connect(db_url) as connection:
# ~with connection.cursor() as cursor:
# ~cursor.execute(statemen

def get_class(crn):
    statement = """
                SELECT * FROM class, location
                    WHERE ( (class.loc_id = location.id)
                        AND (crn = '{}') )
                """.format(crn)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)
            record = cursor.fetchone()
            return record


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


def add_enrollment(crn, stu_num):
    statement = """
                INSERT INTO enrollment 
                    (crn, student_id)
                    VALUES ('{}', '{}')
                """.format(crn, stu_num)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)



# def get_concat():
#     statement = "SELECT FOODS.id AS id, MENU.dy as dy, MENU.repast as repast,  "
#
#     with dbapi2.connect(db_url) as connection:
#         with connection.cursor() as cursor:
#             cursor.execute(statement)
#             records = cursor.fetchall()
#             return records


if __name__ == '__main__':
    check_user("kkarakamis", "1234")
