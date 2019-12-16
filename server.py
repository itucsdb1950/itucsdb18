from flask import Flask, render_template, request, redirect, url_for
import views

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("login.html")


@app.route("/login", methods=['POST'])
def login():
    username = request.form.get('usrn')
    password = request.form.get('pw')
    user = views.check_user(username, password)
    if user:
        if user[0]=='000000001':
            return render_template("base.html", record=user)
        else:
            return render_template("base_student.html", stu_num=user[0])
    return "Your username and password is wrong"


@app.route("/error")
def error_page():
    return render_template("error.html")


@app.route("/admin")
def admin_page():
    return render_template("base.html")


@app.route("/admin/crn")
def admin_crn_page():
    locations = views.get_locations_for_crn()
    crns = views.get_lesson()

    return render_template("admin_crn.html", locations=locations, crns=crns)


@app.route("/admin/location")
def admin_location_page():
    locations = views.get_locations()

    return render_template("admin_location.html", locations=locations)


@app.route("/admin/persons")
def admin_person_page():
    person = views.get_person()
    faculty = views.get_department()

    return render_template("admin_person.html", person=person, faculty=faculty)


@app.route("/admin/food")
def admin_food_page():
    food = views.get_food()

    return render_template("admin_food.html", food=food)


@app.route("/admin/meal")
def admin_meal_page():
    meals = views.get_meal()
    food = views.get_food()
    # concat = views.get_concat()

    return render_template("admin_meal.html", meals=meals, food=food)


@app.route("/admin/grades")
def admin_grades_page():
    grades = views.get_grades_admin()
    student = views.get_student_admin()

    return render_template("admin_grades.html", grades=grades, student=student)


@app.route("/admin/department")
def admin_department_page():
    person = views.get_prof()
    department = views.get_department()
    info = views.get_dept_info()
    return render_template("admin_department.html", person=person, department=department, info=info)


@app.route("/add_grades", methods=['POST'])
def add_grades():
    crn = request.form.get('crn')
    stu_id = request.form.get('stu_id')
    taken_from = request.form.get('taken_from')
    percentage = request.form.get('percentage')
    grade = request.form.get('grade')
    if views.check_grades(crn, stu_id, taken_from):
        views.add_grades(crn, stu_id, taken_from, percentage, grade)
    return redirect(url_for('admin_grades_page'))


@app.route("/del_grades/<string:student_id>/<int:crn>/<string:taken_from>", methods=['GET'])
def del_grades(student_id, crn,taken_from):
    views.del_grades(student_id, crn,taken_from)
    return redirect(url_for('admin_grades_page'))


@app.route("/add_crn", methods=['POST'])
def add_crn():
    crn = request.form.get('crn')
    code = request.form.get('code')
    loc_sel = request.form.get('loc_sel')
    credits_sel = request.form.get('credits_sel')
    if views.check_crn(crn, code, loc_sel):
        views.add_crn(crn, code, loc_sel, credits_sel)
    return redirect(url_for('admin_crn_page'))


@app.route("/add_person", methods=['POST'])
def add_person():
    per_name = request.form.get('per_name')
    per_num = request.form.get('per_num')
    usern = request.form.get('usern')
    passw = request.form.get('passw')
    age = request.form.get('age')
    fac = request.form.get('fac')
    if views.check_person(usern):
        added = views.add_person(per_name, per_num, usern, passw, age, fac)
        if added == 1:
            # "User couldn't be added. Make sure all fields are convenient."
            pass
    return redirect(url_for('admin_person_page'))


@app.route("/add_location", methods=['POST'])
def add_location():
    building = request.form.get('building')
    day = request.form.get('day_sel')
    classroom = request.form.get('classroom')
    capacity = request.form.get('capacity')
    if views.check_location(building, day, classroom):
        views.add_location(building, day, classroom, capacity)
    return redirect(url_for('admin_location_page'))


@app.route("/del_location/<int:loc_id>", methods=['GET'])
def del_location(loc_id):
    views.del_location(loc_id)
    return redirect(url_for('admin_location_page'))


@app.route("/add_department", methods=['POST'])
def add_department():
    dept = request.form.get('dept')
    dean = request.form.get('dean')
    delege = request.form.get('delege')
    if views.check_department(dept):
        views.add_department(dept, dean, delege)
    return redirect(url_for('admin_department_page'))


# @app.route("/update_department", methods=['POST'])
# def update_department():
#     dept = request.form.get('dept')
#     dean = request.form.get('dean')
#     delege = request.form.get('delege')
#     # views.update_department(dept, dean, delege)
#
#     return redirect(url_for('admin_department_page'))


@app.route("/update_crn", methods=['POST'])
def update_crn():
    crn = request.form.get('crn')
    code = request.form.get('code')
    loc_sel = request.form.get('loc_sel')
    credits_sel = request.form.get('credits_sel')
    modal_crn = request.form.get('modal_crn')
    modal_code = request.form.get('modal_code')
    modal_loc_sel = request.form.get('modal_loc_sel')
    modal_credits_sel = request.form.get('modal_credits_sel')
    if views.check_crn(modal_crn, modal_code, modal_loc_sel):
        views.update_crn(crn, code, loc_sel, credits_sel, modal_crn, modal_code, modal_loc_sel, modal_credits_sel)
    return redirect(url_for('admin_crn_page'))


@app.route("/del_crn/<string:crn_num>", methods=['GET'])
def del_crn(crn_num):
    views.del_crn(crn_num)
    return redirect(url_for('admin_crn_page'))



@app.route("/del_person/<string:per_num>", methods=['GET'])
def del_person(per_num):
    views.del_person(per_num)
    return redirect(url_for('admin_person_page'))


@app.route("/del_department/<string:id>", methods=['GET'])
def del_department(id):
    views.del_department(id)
    return redirect(url_for('admin_department_page'))


@app.route("/add_food", methods=['POST'])
def add_food():
    dish_type = request.form.get('dish_type')
    food_name = request.form.get('food_name')
    food_cal = request.form.get('food_cal')
    if views.check_food(dish_type, food_name):
        views.add_food(dish_type, food_name, food_cal)
    return redirect(url_for('admin_food_page'))


@app.route("/del_food/<string:id>", methods=['GET'])
def del_food(id):
    views.del_food(id)
    return redirect(url_for('admin_food_page'))


@app.route("/student/<string:stu_num>")
def student_page(stu_num):
    student = views.get_student(stu_num)
    
    if not student:
        return "No Student Found"
    
    # name, username, id, fac_name, gpa, comp_credits
    name = student[0]
    username = student[1]
    faculty = student[3]
    gpa = student[4]
    compltd_crd = student[5]

    return render_template("student.html", name=name, username=username, stu_num=stu_num,
                           faculty=faculty, gpa=gpa, compltd_crd=compltd_crd)


@app.route("/student/<string:stu_num>/courses")
def student_courses_page(stu_num):
    courses = views.get_courses(stu_num)
    return render_template("student_courses.html", stu_num=stu_num, courses=courses)


@app.route("/student/<string:stu_num>/attendance")
def student_attendance_page(stu_num):
    courses = views.get_attendance(stu_num)
    return render_template("student_attendance.html", stu_num=stu_num, courses=courses)


@app.route("/student/<string:stu_num>/grades")
def student_grades_page(stu_num):
    grades = views.get_grades(stu_num)
    if not grades:
        return "<h1>No Grades Found</h1>"

    # split courses list with respect to crn.
    # note that SQL query in views.get_grades() is written in a way that returned table is ordered by crn.
    # therefore, only one iteration is sufficient
    courses = [[]]  # initialize list that will hold grades which are split by course
    crn = grades[0][0]  # initialize crn with the first course's crn
    i = 0
    for grade in grades:  # iterate over the entire table
        if grade[0] == crn:  # as long as crn remains same, add rows with that crn to courses[i]
            courses[i].append(crn)
        else:  # if another crn is reached
            crn = grade[0]  # update crn to the new one
            i += 1  # so that upcoming course's grades are written to the next index of courses

    return render_template("student_grades.html", stu_num=stu_num, courses=courses)



@app.route("/add_meal", methods=['POST'])
def add_meal():
    day = request.form.get('day_sel')
    repast = request.form.get('repast')
    soup = request.form.get('soup')
    main = request.form.get('main')
    side = request.form.get('side')
    extras = request.form.get('extras')

    # if views.check_meal(building, day, classroom):
    views.add_meal(day, repast, soup, main, side, extras)
    return redirect(url_for('admin_meal_page'))


@app.route("/del_meal/<string:dy>/<string:repast>", methods=['GET'])
def del_meal(dy,repast):
    views.del_meal(dy,repast)
    return redirect(url_for('admin_meal_page'))


@app.route("/food_menu")
def food_menus_page():
    foods = views.get_food_menus()

    # split foods list with respect to day.
    # note that SQL query in views.get_food_menus() is written in a way that returned table is ordered by day.
    # therefore, only one iteration is sufficent
    food_menus = []  # initialize list that will hold food menu which are split with respect to day
    day = foods[0].day  # initilize day with the day of the first food
    i = 0  # start day from 0
    for food in foods:  # iterate over the entire table
        if food.day == day:  # as long as day remains same, add rows with that day to food_menus[i]
            # TODO: map table so food elements have the order soup, main, side, extra
            if food.repast == "lunch":
                food_menus[i][0].append(food)  # food_menus[0] which corresponds to lunch
            else:  # dinner
                food_menus[i][1].append(food)  # food_menus[1] which corresponds to dinner
        else:  # if another day is reached
            day = food.day  # update day to the new one
            i += 1  # so that upcoming course's grades are written to the next index of courses

    return render_template("student_grades.html", menus=food_menus)


@app.route("/student/<string:stu_num>/enroll", methods=['GET', 'POST'])
def student_enrollment_page(stu_num):
    if request.method == "GET":
        courses = views.get_crns()
        return render_template("student_enroll.html", stu_num=stu_num, courses=courses)

    if request.form['crn']:
        crn = request.form['crn']
    else:
        return "<h1>Failed! Fill CRN Field!</h1>"

    klasse = views.get_class(crn)

    enrolled = views.get_enrolled(crn)

    if klasse is None:
        return "<h1>Failed! There is no such CRN!</h1>"
    if enrolled[0] + 1 > klasse[8]:
        return "<h1>Failed! Quota has been reached.</h1>"

    views.add_enrollment(crn, stu_num)
    return redirect(url_for("student_enrollment_page", stu_num=stu_num))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
