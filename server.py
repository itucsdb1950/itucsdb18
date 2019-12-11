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
    return render_template("admin_crn.html")


@app.route("/admin/location")
def admin_location_page():
    locations = views.get_locations()

    return render_template("admin_location.html", locations=locations)


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


@app.route("/login", methods=['POST'])
def login():
    username = request.form.get('usrn')
    password = request.form.get('pw')
    user = views.check_user(username, password)
    if user:
        return render_template("home.html", record=user)
    return "Your username and password is wrong"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
