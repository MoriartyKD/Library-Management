import mysql.connector


def createConnection():
    connection = mysql.connector.connect(host='127.0.0.1',
                                         user='root',
                                         passwd='1234',
                                         database='db',
                                         auth_plugin='mysql_native_password')
    print(connection.connection_id)
    return connection

def updateStatusToUnavailable(id):
    connection = createConnection()
    cursor1 = connection.cursor(prepared=True)
    query1 = "update db.books set status=? where id = ? ;"
    cursor1.execute(query1, ("Unavailable", id))
    connection.commit()

def updateStatusToAvailable(id):
    connection = createConnection()
    cursor1 = connection.cursor(prepared=True)
    query1 = "update db.books set status=? where id = ? ;"
    cursor1.execute(query1, ("Available", id))
    connection.commit()

def countDistinct(id):
    connection = createConnection()
    cursor1 = connection.cursor(prepared=True)
    query1 = "Select count(*) from db.issued where roll = '{}' ;".format(id)
    cursor1.execute(query1)
    value1 = cursor1.fetchall()
    if(value1[0][0] < 3):
        return 0
    else:
        return 1
