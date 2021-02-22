import mysql.connector


def createConnection():
    connection = mysql.connector.connect(host='127.0.0.1',
                                         user='root',
                                         passwd='1234',
                                         database='db',
                                         auth_plugin='mysql_native_password')
    print(connection.connection_id)
    return connection

def removeFromStudents(user_id):
    connection = createConnection()
    cursor1 = connection.cursor()
    string1 = "DELETE from db.student where roll= '{}' ;".format(user_id)
    cursor1.execute(string1)
    connection.commit()


def removeFromBooks(book_id):
    connection = createConnection()
    cursor1 = connection.cursor(prepared=True)
    string1 = "DELETE from db.books where id= '{}' ;".format(book_id)
    cursor1.execute(string1)
    connection.commit()

def removeIssued(book_id):
    connection = createConnection()
    cursor1 = connection.cursor(prepared=True)
    string1 = "DELETE from db.issued where id= '{}' ;".format(book_id)
    cursor1.execute(string1)
    connection.commit()


