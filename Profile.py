from flask import Flask
from flask import render_template
from flask.wrappers import Request

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

@app.route('/projects')
def projects():
    return render_template('AboutMe.html')

@app.route('/experince')
def experince():
    return render_template('AboutMe.html')

@app.route('/techicalskills')
def techicalskills():
    return render_template('TechnicalSkills.html')


@app.route('/Contact')
def Contact():
    return render_template('AboutMe.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
