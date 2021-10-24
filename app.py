from flask import Flask, request, render_template, session

from Python_templates import Forms,Data_Ingestion,DataValidations

from flask.helpers import flash

from werkzeug.utils import redirect



app = Flask(__name__)



@app.route('/')
def home():

    return render_template('home.html')











if __name__ == "__main__":
    app.run( debug=True, port=5000)
