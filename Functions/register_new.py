import mysql.connector


def createConnection():
    connection = mysql.connector.connect(host='127.0.0.1',
                                         user='root',
                                         passwd='1234',
                                         database='db',
                                         auth_plugin='mysql_native_password')
    print(connection.connection_id)
    return connection

def insertTouser(name,email,roll,password,contact,dob):
    connection = createConnection()
    cursor1 = connection.cursor()
    string = "insert into db.student (name,email,roll,passwd,mob,dob) values ('{}','{}','{}','{}','{}','{}');".format(name,email,roll,password,contact,dob)
    cursor1.execute(string)
    connection.commit()
    cursor1.close()


def insertToBook(book_id,title,author,status):
    connection1 = createConnection()
    cursor1 = connection1.cursor()
    string = "insert into db.books (id,title,author,status) values ('{}','{}','{}','{}');".format(book_id,title,author,status)
    cursor1.execute(string)
    connection1.commit()
    cursor1.close()

def insertToIssued(id,title,roll,name,idate,rdate):
    connection1 = createConnection()
    cursor1 = connection1.cursor()
    string = "insert into db.issued (id,title,roll,name,idate,rdate) values ('{}','{}','{}','{}','{}','{}');".format(id,title,roll,name,idate,rdate)
    cursor1.execute(string)
    connection1.commit()
    cursor1.close()

