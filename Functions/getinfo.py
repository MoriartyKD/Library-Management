from datetime import date
import mysql.connector

def createConnection():
    connection = mysql.connector.connect(host='127.0.0.1',
                                         user='root',
                                         passwd='1234',
                                         database='db',
                                         auth_plugin='mysql_native_password')
    print(connection.connection_id)
    return connection


def getStudentInfo(user_id):
    connection = createConnection()
    cursor1 = connection.cursor()
    string = "select name,email,roll,passwd,mob,dob from db.student where roll = '{}'; ".format(user_id)
    cursor1.execute(string)
    value = cursor1.fetchall()
    my_dict = {'name' : value[0][0],'email':value[0][1],'roll':value[0][2],'passwd':value[0][3], 'mob':value[0][4], 'dob':value[0][5]}
    return my_dict


def getAdminInfo(admin_id):
    connection = createConnection()
    cursor1 = connection.cursor()
    string = "select id,name,passwd,email from db.admin_user where id = '{}' ;".format(admin_id)
    cursor1.execute(string)
    value = cursor1.fetchall()
    my_dict = {'id' : value[0][0],'name':value[0][1],'passwd':value[0][2],'email':value[0][3]}
    return my_dict

def getBooksInfo():
    connection = createConnection()
    cursor1 = connection.cursor()
    list1 = []
    string = "select id,title,author,status from db.books ;"
    cursor1.execute(string)
    value = cursor1.fetchall()
    for row in value:
        my_dict = {'id' : row[0],'title':row[1],'author':row[2],'status':row[3]}
        list1.append(my_dict)
    return list1

def getBooksInfoSearch(srch):
    connection = createConnection()
    cursor1 = connection.cursor()
    list1 = []
    string = "select id,title,author,status from db.books where title like '%{}%' OR author like '%{}%' OR id like '%{}%';".format(srch,srch,srch)
    cursor1.execute(string)
    value = cursor1.fetchall()
    for row in value:
        my_dict = {'id' : row[0],'title':row[1],'author':row[2],'status':row[3]}
        list1.append(my_dict)
    return list1

def getIssuedInfo(roll):
    connection = createConnection()
    cursor1 = connection.cursor()
    string = "select id,title,idate,rdate from db.issued where roll = '{}' ;".format(roll)
    cursor1.execute(string)
    value = cursor1.fetchall()
    list1 = []
    for row in value:
        my_dict = {'id': row[0], 'title': row[1], 'idate': row[2], 'rdate': row[3]}
        list1.append(my_dict)
    return list1

def getIssuedInfobyBook(id):
    connection = createConnection()
    cursor1 = connection.cursor()
    string = "select id,title,roll,name,idate,rdate from db.issued where id = '{}' ;".format(id)
    cursor1.execute(string)
    fine = 0
    value = cursor1.fetchall()
    if(value[0][5] < date.today()):
        fine = date.today() - value[0][5]
    my_dict = {'id': value[0][0], 'title': value[0][1], 'roll': value[0][2], 'name': value[0][3], 'idate': value[0][4], 'rdate': value[0][5], 'fine': fine}
    return my_dict

def getAllStudentInfo():
    connection = createConnection()
    cursor1 = connection.cursor()
    list1 = []
    string = "select roll,name,email,mob from db.student ;"
    cursor1.execute(string)
    value = cursor1.fetchall()
    for row in value:
        my_dict = {'roll' : row[0],'name':row[1],'email':row[2],'mob':row[3]}
        list1.append(my_dict)
    return list1

def getAllStudentInfoSearch(srch):
    connection = createConnection()
    cursor1 = connection.cursor()
    list1 = []
    string = "select roll,name,email,mob from db.student where roll like '%{}%' OR name like '%{}%' OR email like '%{}%';".format(srch,srch,srch)
    cursor1.execute(string)
    value = cursor1.fetchall()
    for row in value:
        my_dict = {'roll' : row[0],'name':row[1],'email':row[2],'mob':row[3]}
        list1.append(my_dict)
    return list1

def getAllIssuedInfo():
    connection = createConnection()
    cursor1 = connection.cursor()
    list1 = []
    string = "select roll,name,id,title,idate,rdate from db.issued ;"
    cursor1.execute(string)
    value = cursor1.fetchall()
    for row in value:
        my_dict = {'roll' : row[0],'name' : row[1],'id':row[2],'title':row[3],'idate':row[4],'rdate':row[5]}
        list1.append(my_dict)
    return list1

def getAllIssuedInfoSearch(srch):
    connection = createConnection()
    cursor1 = connection.cursor()
    list1 = []
    string = "select roll,name,id,title,idate,rdate from db.issued where roll like '%{}%' OR id like '%{}%' OR name like '%{}%' OR title like '%{}%' ;".format(srch,srch,srch,srch)
    cursor1.execute(string)
    value = cursor1.fetchall()
    for row in value:
        my_dict = {'roll' : row[0],'name' : row[1],'id':row[2],'title':row[3],'idate':row[4],'rdate':row[5]}
        list1.append(my_dict)
    return list1

def getBook(id):
    connection = createConnection()
    cursor1 = connection.cursor()
    string = "select id,title,author,status from db.books where id = '{}' ;".format(id)
    cursor1.execute(string)
    value = cursor1.fetchall()
    my_dict = {'id' : value[0][0],'title':value[0][1],'author':value[0][2],'status':value[0][3]}
    return my_dict