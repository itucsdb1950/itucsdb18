def get_student(stu_num):
    statement = """ SELECT person.name, person.username, student.id, faculty.fac_name, student.gpa, student.comp_credits, 
                      FROM student, person, faculty
                        WHERE ( (person.id = student.id)
                            AND (student.fac_id = faculty.id) ) 
                        WHERE student.id = '{}' """.format(stu_num)

    with dbapi2.connect(db_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)
            record = cursor.fetchone()
            return record
