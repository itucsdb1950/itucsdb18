from flask import Flask, render_template, request, redirect, url_for
import views

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("login.html")


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

    return render_template("admin_person.html", person=person)


@app.route("/admin/department")
def admin_department_page():
    person = views.get_person()
    department = views.get_department()
    return render_template("admin_department.html", person=person, department=department)


@app.route("/add_crn", methods=['POST'])
def add_crn():
    dept = request.form.get('dept')
    dean = request.form.get('dean')
    delege = request.form.get('delege')
    if views.check_crn(dept):
        views.add_crn(dept, dean, delege)
    return redirect(url_for('admin_crn_page'))


@app.route("/add_person", methods=['POST'])
def add_person():
    per_name = request.form.get('per_name')
    per_num = request.form.get('per_num')
    usern = request.form.get('usern')
    passw = request.form.get('passw')
    age = request.form.get('age')
    type = request.form.get('type')
    if views.check_person(usern):
        added = views.add_person(per_name, per_num, usern, passw, age, type)
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


@app.route("/login", methods=['POST'])
def login():
    username = request.form.get('usrn')
    password = request.form.get('pw')
    user = views.check_user(username, password)
    if user:
        return render_template("home.html", record=user)
    return "Your username and password is wrong"


@app.route("/del_person/<string:per_num>", methods=['GET'])
def del_person(per_num):
    views.del_person(per_num)
    return redirect(url_for('admin_person_page'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
