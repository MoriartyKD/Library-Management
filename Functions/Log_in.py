import mysql.connector
def createConnection():
    
    connection=mysql.connector.connect(host='127.0.0.1',
                                user='root',
                                passwd='1234',
                                database='db',
                                auth_plugin='mysql_native_password')
    print(connection.connection_id)
    return connection


def userlogin(roll, password):
    connection = createConnection()
    query = "select passwd,name from db.student where roll = '{}';".format(roll)
    cursor1 = connection.cursor()
    cursor1.execute(query)
    value = cursor1.fetchall()
    if len(value) > 0:
        if password == value[0][0]:
            return value[0][1]
        else:
            return ""
    else:
        return ""


def adminlogin(id, password):
    connection = createConnection()
    query = "select passwd,name from db.admin_user where id = '{}';".format(id)
    cursor1 = connection.cursor()
    cursor1.execute(query)
    value = cursor1.fetchall()
    if len(value) > 0:
        if password == value[0][0]:
            return value[0][1]
        else:
            return ""
    else:
        return ""
