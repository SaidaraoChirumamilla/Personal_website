# import psycopg2
# # from wtforms import validators,StringField



# def Signup(form):
#     connection = psycopg2.connect(user="teja",
#                                   password="Saidarao3!",
#                                   host="127.0.0.1",
#                                   port="5432",
#                                   database="iamstem")


#    # Create a cursor to perform database operations
#     cursor = connection.cursor()

#     if len(form['firstName'])>4 and len(form['lastName'])>4 and validators.email(form['email']):

#         fname = form['firstName']
#         sname = form['lastName']
#         password = form['password']
#         email = form['email']
#         roles = form['roles']
#         user_insert_query = """INSERT INTO users (firstname, lastname, email,pass,rol,phone,grade) \
#               VALUES (%s,%s,%s,%s,%s,%s,%s)"""
#         cursor.execute(user_insert_query,(fname,sname,email,password,roles,fname,fname))
#         connection.commit()
#     else:
#         return 0

# # class SignupForm():

# #     username = StringField('Username',
# #                            validators=[DataRequired(), Length(min=2, max=20)])
# #     email = StringField('Email',
# #                         validators=[DataRequired(), Email()])
# #     password = PasswordField('Password', validators=[DataRequired()])
# #     confirm_password = PasswordField('Confirm Password',
# #                                      validators=[DataRequired(), EqualTo('password')])
# #     submit = SubmitField('Sign Up')

