# @app.route("/student/<string:stu_num>")
# def student_page():
#   student = views.get_student(stu_num)
#
#   # name, username, id, fac_name, gpa, comp_credits
#   name = student[1]
#   username = student[2]
#   faculty = student[4]
#   gpa = student[5]
#   compltd_crd = student[6]
#
#   return render_template("student.html", name=name, username=username, stu_num=stu_num,
#                                          faculty=faculty, gpa=gpa, compltd_crd=compltd_crd)
#
#
# @app.route("/student/<string:stu_num>/courses")
# def student_courses_page():
#   courses = views.get_courses(stu_num)
#   return render_template("student_courses.html", courses=courses)
#
#
# @app.route("/student/<string:stu_num>/attendance")
# def student_attendance_page():
#   courses = views.get_attendance(stu_num)
#   return render_template("student_attendance.html", courses=courses)
#
#
# @app.route("/food_menu")
# def food_menus_page():
#     foods = views.get_food_menus()
#
#     # split foods list with respect to day.
#     # note that SQL query in views.get_food_menus() is written in a way that returned table is ordered by day.
#     # therefore, only one iteration is sufficent
#     food_menus = [] # initialize list that will hold food menu which are split with respect to day
#     day = foods[0].day # initilize day with the day of the first food
#     i = 0 # start day from 0
#     for food in foods: # iterate over the entire table
#         if food.day == day: # as long as day remains same, add rows with that day to food_menus[i]
#             # TODO: map table so food elements have the order soup, main, side, extra
#             if food.repast == "lunch":
#                 food_menus[i][0].append(food) # food_menus[0] which corresponds to lunch
#             else: #dinner
#                 food_menus[i][1].append(food) # food_menus[1] which corresponds to dinner
#         else: # if another day is reached
#             day = food.day # update day to the new one
#             i += 1 # so that upcoming course's grades are written to the next index of courses
#
#     return render_template("student_grades.html", menus=food_menus)
#
#
# @app.route("/student/<string:stu_num>/enroll", methods=['GET', 'POST'])
# def student_enrollment_page(stu_num):
#     if request.method == "GET":
#         courses = views.get_crns()
#         return render_template("student_enroll.html", courses=courses)
#
#     crn = request.form['crn'] if request.form['crn'] else return "<h1>Failed! Fill CRN Field!</h1>"
#
#     class = views.get_class(crn)
#     enrolled = views.get_enrolled(crn)
#
#     if class is None:
#         return "<h1>Failed! There is no such CRN!</h1>"
#     if enrolled+1 > class.capacity:
#         return "<h1>Failed! Quota has been reached.</h1>"
#
#     views.add_crn(crn, stu_num)
#     return redirect(url_for("student_enrollment_page"))

@app.route("/update_department/<int:dept_id>", methods=['POST'])
@allow_to()
def update_department(dept_id):
    if request.method == 'GET':
        people = views.get_person()
        return render_template("admin_department_update.html", dept_id=dept_id, people=people)
    else:
        old_id = request.form.get('old_id')
        dept = request.form.get('dept')
        dean = request.form.get('dean')
        delege = request.form.get('delege')
        views.update_department(old_id, dept_id, dean, delege)
        return redirect(url_for('admin_department_page'))
