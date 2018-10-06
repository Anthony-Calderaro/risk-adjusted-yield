# import flask, template rendering, as well as data files
from flask import Flask, render_template
from data import Companies

# create instance of Flask app
app = Flask(__name__)

# create a variable equal to the data array from data.py
Companies = Companies()

# make routes
@app.route("/")
def index():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/companies")
def companies():
    return render_template("companies.html", companies = Companies)

@app.route("/companies/<string:id>/")
def company(id):
    return render_template("company.html", id = id)

# check if app name is the main script to be executed
if __name__ == "__main__":
    app.run(debug=True)

