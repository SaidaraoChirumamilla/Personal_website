import psycopg2



def signup():
    connection = psycopg2.connect(user="teja",
                                  password="Saidarao3!",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="iamstem")

   # Create a cursor to perform database operations
    cursor = connection.cursor()
    cursor.execute("select * from users;")
    record = cursor.fetchall()
    for item in record:
       print("ids =",item[0])

signup()
