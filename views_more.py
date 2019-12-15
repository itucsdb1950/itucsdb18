# def get_student(stu_num):
#     statement = """
#                 SELECT person.name, person.username, student.id, faculty.fac_name, student.gpa, student.comp_credits
#                     FROM student, person, faculty
#                     WHERE ( (person.id = student.id)
#                         AND (student.fac_id = faculty.id) )
#                     WHERE student.id = '{}'
#                 """.format(stu_num)
#
#     with dbapi2.connect(db_url) as connection:
#         with connection.cursor() as cursor:
#             cursor.execute(statement)
#             record = cursor.fetchone()
#             return record
#
#
# def get_courses(stu_num):
#     statement = """
#                 SELECT class.crn AS crn, class.course_code AS course_code, location.day AS day,
#                        location.building AS building, location.class AS class
#                     FROM student, enrollment, class, location
#                     WHERE ( (student.id = enrollment.student_id)
#                         AND (enrollment.crn = class.crn)
#                         AND (class.loc_id = location.id) )
#                     WHERE (student.id = '{}')
#                 """.format(stu_num)
#
#     with dbapi2.connect(db_url) as connection:
#         with connection.cursor() as cursor:
#             cursor.execute(statement)
#             records = cursor.fetchall()
#             return records
#
#
# def get_attendance(stu_num):
#     statement = """
#                 SELECT class.crn AS crn, class.course_code AS course_code,
#                        enrollment.attendance AS attendance
#                     FROM student, enrollment, class
#                     WHERE ( (student.id = enrollment.student_id)
#                         AND (enrollment.crn = class.crn) )
#                     WHERE (student.id = '{}')
#                 """.format(stu_num)
#
#     with dbapi2.connect(db_url) as connection:
#         with connection.cursor() as cursor:
#             cursor.execute(statement)
#             records = cursor.fetchall()
#             return records
#
#
# ~select menu.day, menu.repast, foods.name from MENU, FOODS
    # ~where ( (menu.soup = foods.food_id) or (menu.main = foods.food_id))) 


def get_food_menus(stu_num):
    statement = """
                SELECT menu.dy AS day, menu.repast AS repast,
                       foods.name AS name, foods.calorie AS calories,
                    FROM menu, foods
                    WHERE ( (menu.soup = foods.id)
                        OR (menu.main = foods.id)
                        OR (menu.side = foods.id)
                        OR (menu.extras = foods.id) )
                    ORDER BY menu.dy, menu.repast
                """.format(stu_num)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)
            records = cursor.fetchall()
            return records
