# import flask, template rendering, 
from flask import Flask, render_template

# create instance of Flask app
app = Flask(__name__)


# make home route and return the template for the "/" url
@app.route("/")
def index():
    return render_template("home.html")


# check if app name is the main script to be executed
if __name__ == "__main__":
    app.run(debug=True)

