from flask import Flask, render_template, request
from views import *

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
    return render_template("admin_location.html")

@app.route("/login", methods=['POST'])
def login():
    username = request.form.get('usrn')
    password = request.form.get('pw')
    user = check_user(username, password)
    if user:
        return render_template("home.html", record=user)
    return "Your username and password is wrong"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
