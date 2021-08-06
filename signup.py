import psycopg2



def Signup(form):
    connection = psycopg2.connect(user="teja",
                                  password="Saidarao3!",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="iamstem")


   # Create a cursor to perform database operations
    cursor = connection.cursor()

    
    fname = form['firstName']
    sname = form['lastName']
    password = form['password']
    email = form['email']
    roles = form['roles']

    print(type(form['firstName']))

    user_insert_query = """INSERT INTO users (firstname, lastname, email,pass,rol,phone,grade) \
    VALUES (%s,%s,%s,%s,%s,%s,%s)"""


    cursor.execute(user_insert_query,(fname,sname,email,password,roles,fname,fname))
    connection.commit()


