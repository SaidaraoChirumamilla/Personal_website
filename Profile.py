from flask import Flask, request
from flask import render_template
from flask.helpers import url_for
from flask.wrappers import Request
# from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/home', methods=["GET", "POST"])
def home():
    ButtonPressed = "success"
    if Request.method == "POST":
        return render_template("home.html", ButtonPressed )
    return render_template('home.html')

@app.route('/aboutme')
def aboutme():
    return render_template('AboutMe.html')

@app.route('/courses')
def Courses():
    return render_template('Courses.html')

@app.route("/projects", methods=["GET", "POST"])
def projects():
    if request.method == 'POST' :

        Email = request.form['email']
        firstName = request.form['fname']
        secondname = request.form['sname']
        msg = request.form['msg']

        print(Email,firstName,secondname,msg)

        return render_template('Projects.html',firstName  = firstName, secondname = secondname, Email = Email, msg = msg)

        # redirect('/projects', firstName  = firstName, secondname = secondname, Email = Email, msg = msg)


    else :
        return render_template('Projects.html')

	

	

@app.route('/experince')
def experince():
    return render_template('Experince.html')

@app.route('/techicalskills')
def techicalskills():
    return render_template('TechnicalSkills.html')


@app.route('/Contact')
def Contact():
    return render_template('AboutMe.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
