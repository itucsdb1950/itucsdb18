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
        return render_template("base.html", record=user)
    return "Your username and password is wrong"


@app.route("/admin")
def admin_page():
    return render_template("base.html")


@app.route("/admin/crn")
def admin_crn_page():
    locations = views.get_locations_for_crn()
    crns = views.get_crns()

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
    grades = views.get_grades()
    student = views.get_student()

    return render_template("admin_grades.html", grades=grades, student=student)


@app.route("/admin/department")
def admin_department_page():
    person = views.get_person()
    department = views.get_department()
    info = views.get_dept_info()
    return render_template("admin_department.html", person=person, department=department, info=info)


@app.route("/add_grades", methods=['POST'])
def add_crn():
    crn = request.form.get('crn')
    stu_id = request.form.get('stu_id')
    taken_from = request.form.get('taken_from')
    percentage = request.form.get('percentage')
    grade = request.form.get('grades')
    if views.check_grades(crn, stu_id, taken_from):
        views.add_grades(crn, stu_id, taken_from, percentage, grade)
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
    return render_template("student_courses.html", courses=courses)


@app.route("/student/<string:stu_num>/attendance")
def student_attendance_page(stu_num):
    courses = views.get_attendance(stu_num)
    return render_template("student_attendance.html", courses=courses)


@app.route("/student/<string:stu_num>/grades")
def student_grades_page(stu_num):
    grades = views.get_grades(stu_num)

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

    return render_template("student_grades.html", courses=courses)



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


@app.route("/del_meal/<string:id>", methods=['GET'])
def del_meal(id):
    views.del_meal(id)
    return redirect(url_for('admin_meal_page'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
