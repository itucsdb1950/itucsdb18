from flask import Flask


app = Flask(__name__)


@app.route("/")
def home_page():
    return """Hello, world!
              This is Klasse. 
              Diese ist Klasse.
              This team actually has nothing to do with German. The name "Klasse" is chosen because it's so klasse. :P"""


if __name__ == "__main__":
    app.run()
