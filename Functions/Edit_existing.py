import mysql.connector


def createConnection():
    connection = mysql.connector.connect(host='127.0.0.1',
                                         user='root',
                                         passwd='1234',
                                         database='db',
                                         auth_plugin='mysql_native_password')
    print(connection.connection_id)
    return connection


def editUser(id,name,email,password,mob,dob):
    connection = createConnection()
    cursor1 = connection.cursor(prepared=True)
    query1 = "update db.student set  name=? ,email=?,  passwd = ? ,mob=? ,dob=? where roll = ? ;"
    cursor1.execute(query1,(name,email,password,mob,dob,id))
    connection.commit()

def editAdmin(id,name,email,password):
    connection = createConnection()
    cursor1 = connection.cursor(prepared=True)
    query1 = "update admin_user set name=? , email=? , passwd = ? where id = ? ;"
    cursor1.execute(query1,(name,email,password,id))
    connection.commit()

def editBook(id,title,author,status):
    connection = createConnection()
    cursor1 = connection.cursor(prepared=True)
    query1 = "update db.books set title=? , author=? , status= ? where id = ? ;"
    cursor1.execute(query1,(title,author,status,id))
    connection.commit()
