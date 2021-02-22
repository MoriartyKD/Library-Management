from datetime import date,timedelta

from flask import Flask
from flask import request
from flask import url_for
from flask import redirect
from flask import render_template


from Functions import Log_in
from Functions import register_new
from Functions import getinfo
from Functions import Edit_existing
from Functions import remove
from Functions import transaction

logged_in={'username':"", 'type':"", 'id':""}
editIDfromAdmin = ""
filter_list = []

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if (request.method == 'GET'):
        return render_template('login.html')
    elif (request.method == 'POST'):
        if (request.form['submit_button'] == 'user'):
            roll = request.form['user_name']
            password = request.form['user_password']
            result = Log_in.userlogin(roll, password)

            if len(result) > 0:
                logged_in['username'] = result
                logged_in['type'] = "user"
                logged_in['id'] = roll

                print(result)
                return redirect(url_for('user_dashboard'))
            else:
                return redirect(url_for('login'))

        elif (request.form['submit_button'] == 'admin'):
            id = request.form['user_name']
            password = request.form['admin_password']
            result = Log_in.adminlogin(id, password)

            if len(result) > 0:
                logged_in['username'] = result
                logged_in['type'] = "admin"
                logged_in['id'] = id
                return  redirect(url_for('admin_dashboard'))
            else:
                return redirect(url_for('login'))

@app.route('/register_user' , methods=['GET' , 'POST'])
def register_user():
    if (request.method == 'GET'):
        return render_template('register_user.html')
    elif request.method == 'POST' :
            try:
                student=request.form
                name=student['name']
                email=student['email']
                roll=student['roll']
                passwd=student['password']
                contact=student['contact']
                dob=student['dob']

                register_new.insertTouser(name, email, roll, passwd, contact, dob)
                return redirect(url_for('login'))
            except Exception as e:
                return redirect(url_for('login'))


@app.route('/user_dashboard', methods=['GET', 'POST'])
def user_dashboard():
    if (request.method == 'GET'):

        return render_template('user_dashboard.html', personal_info=getinfo.getStudentInfo(logged_in['id']),
                               issued_info=getinfo.getIssuedInfo(logged_in['id']),
                               books_info=getinfo.getBooksInfo())

    elif (request.method == 'POST'):
        srch = request.form['search']
        return render_template('user_dashboard.html', personal_info=getinfo.getStudentInfo(logged_in['id']),
                               issued_info=getinfo.getIssuedInfo(logged_in['id']),
                               books_info=getinfo.getBooksInfoSearch(srch))


@app.route('/admin_dashboard', methods=['POST', 'GET'])
def admin_dashboard():
    if (request.method == 'GET'):
        return render_template('admin_dashboard.html', personal_info=getinfo.getAdminInfo(logged_in['id']),
                                student_info=getinfo.getAllStudentInfo(), books_info=getinfo.getBooksInfo(),
                                issued_info=getinfo.getAllIssuedInfo())
    elif (request.method == 'POST'):
        if(request.form['sbmt'] == 'book'):
            srch=request.form['search']
            return render_template('admin_dashboard.html', personal_info=getinfo.getAdminInfo(logged_in['id']),
                                   student_info=getinfo.getAllStudentInfo(), books_info=getinfo.getBooksInfoSearch(srch),
                                   issued_info=getinfo.getAllIssuedInfo())

        elif (request.form['sbmt'] == 'student'):
            srch = request.form['search']
            return render_template('admin_dashboard.html', personal_info=getinfo.getAdminInfo(logged_in['id']),
                                   student_info=getinfo.getAllStudentInfoSearch(srch),
                                   books_info=getinfo.getBooksInfo(),
                                   issued_info=getinfo.getAllIssuedInfo())

        elif (request.form['sbmt'] == 'issued'):
            srch = request.form['search']
            return render_template('admin_dashboard.html', personal_info=getinfo.getAdminInfo(logged_in['id']),
                                   student_info=getinfo.getAllStudentInfo(),
                                   books_info=getinfo.getBooksInfo(),
                                   issued_info=getinfo.getAllIssuedInfoSearch(srch))


@app.route('/logout', methods=['GET'])
def logout():
    if(request.method == 'GET'):
        global logged_in
        logged_in['id'] = ""
        logged_in['username'] = ""
        logged_in['type'] = ""
        return redirect(url_for('login'))


@app.route('/register_book',methods=['GET','POST'])
def register_book():
	if(request.method == 'GET'):
		return render_template('register_book.html')
	elif request.method == 'POST' :
           try :
              book_id = request.form['book_id']
              title = request.form['title']
              author = request.form['author']
              status = request.form['status']
              register_new.insertToBook(book_id,title,author,status)
              return redirect(url_for('admin_dashboard'))
           except Exception as e :
              print(e)
              return redirect(url_for('admin_dashboard'))


@app.route('/edit_admin',methods=['GET','POST'])
def edit_admin():
    if(request.method == 'GET'):
        return render_template('edit_admin.html',personal_info=getinfo.getAdminInfo(logged_in['id']))
    elif(request.method == 'POST'):
        name = request.form['username']
        email = request.form['email']
        password = request.form['password']
        Edit_existing.editAdmin(logged_in['id'],name,email,password)
        return redirect(url_for('admin_dashboard'))

@app.route('/edit_user',methods=['GET','POST'])
def edit_user():
    if(request.method == 'GET'):
        return render_template('edit_user.html',personal_info=getinfo.getStudentInfo(logged_in['id']))
    elif(request.method == 'POST'):
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        mob = request.form['mob']
        dob = request.form['dob']
        Edit_existing.editUser(logged_in['id'],name,email,password,mob,dob)
        return redirect(url_for('user_dashboard'))

@app.route('/edit_book',methods=['GET','POST'])
def edit_book():
    if(request.method == 'GET'):
        if(logged_in['type'] == "admin"):
            global book_id_to_be_edited
            book_id_to_be_edited = request.args.get('id')
            return render_template('edit_book.html',book_info = getinfo.getBook(book_id_to_be_edited))
    elif(request.method == 'POST'):
        title = request.form['title']
        author = request.form['author']
        status = request.form['status']
        if(logged_in['type'] == "admin"):
           Edit_existing.editBook(book_id_to_be_edited ,title, author, status)
           return redirect(url_for('admin_dashboard'))

@app.route('/removeBook',methods=['GET','POST'])
def removeBook():
    if (request.method == 'GET'):
        if (logged_in['type'] == "admin"):
            global book_id_to_be_removed
            book_id_to_be_removed = request.args.get('id')
            return render_template('remove_book.html', book_info=getinfo.getBook(book_id_to_be_removed))
    elif (request.method == 'POST'):
        if (logged_in['type'] == "admin"):
            remove.removeFromBooks(book_id_to_be_removed)
            return redirect(url_for('admin_dashboard'))


@app.route('/removeUser', methods=['GET','POST'])
def removeUser():
    if (request.method == 'GET'):
        if (logged_in['type'] == "admin"):
            global user_id_to_be_removed
            user_id_to_be_removed = request.args.get('id')
            return render_template('remove_user.html', personal_info=getinfo.getStudentInfo(user_id_to_be_removed))
    elif (request.method == 'POST'):
        if (logged_in['type'] == "admin"):
            remove.removeFromStudents(user_id_to_be_removed)
            return redirect(url_for('admin_dashboard'))

@app.route('/issueBook',methods=['GET','POST'])
def issueBook():
    if(request.method == 'GET'):
        if (logged_in['type'] == "user"):
            global book_issued
            book_issued = request.args.get('id')
            return render_template('issue_book.html', book_info=getinfo.getBook(book_issued))
    elif request.method == 'POST':
        try :
            book_info=getinfo.getBook(book_issued)
            idate = date.today()
            rdate = idate + timedelta(days=7)
            count = transaction.countDistinct(logged_in['id'])
            if(count == 0):
                register_new.insertToIssued(book_info['id'],book_info['title'],logged_in['id'],logged_in['username'],idate,rdate)
                transaction.updateStatusToUnavailable(book_info['id'])
            return redirect(url_for('user_dashboard'))
        except Exception as e :
            print(e)
            return redirect(url_for('user_dashboard'))

@app.route('/returnBook',methods=['GET','POST'])
def returnBook():
    if(request.method == 'GET'):
        if (logged_in['type'] == "user"):
            global book_return
            book_return = request.args.get('id')
            return render_template('return_book.html', info=getinfo.getIssuedInfobyBook(book_return))
    elif request.method == 'POST':
        try :
            remove.removeIssued(book_return)
            transaction.updateStatusToAvailable(book_return)
            return redirect(url_for('user_dashboard'))
        except Exception as e :
            print(e)
            return redirect(url_for('user_dashboard'))

@app.route('/removeIssued',methods=['GET','POST'])
def removeIssued():
    if (request.method == 'GET'):
        if (logged_in['type'] == "admin"):
            global issued_id_to_be_removed
            issued_id_to_be_removed = request.args.get('id')
            return render_template('remove_issued.html', info=getinfo.getIssuedInfobyBook(issued_id_to_be_removed))
    elif (request.method == 'POST'):
        if (logged_in['type'] == "admin"):
            remove.removeIssued(issued_id_to_be_removed)
            return redirect(url_for('admin_dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
