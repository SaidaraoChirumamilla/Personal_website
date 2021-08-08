from flask import Flask, request
from flask import render_template
from Forms import SignupForm
from flask_bootstrap import Bootstrap
from formnew import RegistrationForm
from flask.helpers import flash, url_for
from flask.wrappers import Request
# from signup import Signup
from werkzeug.utils import redirect


app = Flask(__name__)
app.secret_key = 'asrtarstaursdlarsn'
Bootstrap(app)

@app.route('/home')
def index():
    return render_template('home1.html')




@app.route('/signup',methods=["GET", "POST"])
def signup():

    signupform = SignupForm()

    if request.method == "POST" :

        print(request.form.getlist('grade'))

        


        if signupform.validate_on_submit():
            # print(request.form)

            flash(f'Account created for {signupform.username.data}!', 'success')
            return render_template('home1.html')

    print(signupform.errors)
    return render_template('signup.html', signupform = signupform)





if __name__ == "__main__":
    app.run( debug=True, port=5000)
