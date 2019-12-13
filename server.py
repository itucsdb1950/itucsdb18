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
    locations = views.get_locations()
    crns = views.get_crns()

    return render_template("admin_crn.html", locations=locations, crns=crns)


@app.route("/admin/location")
def admin_location_page():
    locations = views.get_locations_for_crn()

    return render_template("admin_location.html", locations=locations)

@app.route("/admin/persons")
def admin_person_page():
    person = views.get_person()

    return render_template("admin_person.html", person=person)

@app.route("/add_person", methods=['POST'])
def add_person():
    stu_name = request.form.get('stu_name')
    stu_num = request.form.get('stu_num')
    usern = request.form.get('usern')
    passw = request.form.get('passw')
    age = request.form.get('age')
    if views.check_person(usern):
        added = views.add_person(stu_name, stu_num, usern, passw, age)
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


@app.route("/add_crn", methods=['POST'])
def add_crn():
    crn = request.form.get('crn')
    code = request.form.get('code')
    loc_sel = request.form.get('loc_sel')
    credits_sel = request.form.get('credits_sel')
    if views.check_crn(crn, code, loc_sel):
        views.add_crn(crn, code, loc_sel, credits_sel)
    return redirect(url_for('admin_crn_page'))


@app.route("/login", methods=['POST'])
def login():
    username = request.form.get('usrn')
    password = request.form.get('pw')
    user = views.check_user(username, password)
    if user:
        return render_template("home.html", record=user)
    return "Your username and password is wrong"

@app.route("/del_person/stu_num", methods=['GET'])
def del_person(stu_num):
    views.del_person(stu_num)
    return redirect(url_for('admin_person_page'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
