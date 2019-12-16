from flask import Flask, render_template, request, redirect, url_for
import views

app = Flask(__name__)

@app.route("/error")
def error_page():
    return render_template("error.html")





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
