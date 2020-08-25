from flask import Flask, redirect, url_for, request, render_template, session
import os


app = Flask(__name__)
app.secret_key = b'_5aa#y2L"F4Q8z\n\xec]/'

@app.route('/')
def inicio():
   return render_template('login.html')

@app.route('/home')
def home():
    if session.get('status') ==  "Logado":
        return render_template('home.html', user=session['usuario'], lista=dbs())
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      pass1 = request.form['pass1']
      if pass1 == 'rafa':
          session['usuario'] = user
          session['status'] = "Logado"
      else:
        if session.get('status') is None:
            return render_template('login.html', status="Falha de Login!")
        else:
            return redirect(url_for('home'))

      # return render_template('home.html', res = user, pass1 = pass1)
      return redirect(url_for('home'))
   else:
       if session.get('status') is None:
           return render_template('login.html', status="Faça o Login para entrar.")
       else:
           return render_template('login.html', status="Logado")

@app.route('/files')
def files():
    return render_template('files.html', lista=dbs())
def dbs():
    path = 'db'
    listadbs = os.listdir(path)
    return listadbs

@app.route('/db/<dbname>')
def homedb(dbname):
    if session.get('status') ==  "Logado":
        return render_template('homedb.html', db=dbname)
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
   app.run(debug = True)



# try:
#     sqliteConnection = sqlite3.connect('SQLite_Python.db')
#     cursor = sqliteConnection.cursor()
#     print("Database created and Successfully Connected to SQLite")
#
#     sqlite_select_Query = "select * from usuario3;"
#     cursor.execute(sqlite_select_Query)
#     record = cursor.fetchall()
#     print("SQLite Database Version is: ", record)
#     cursor.close()
#
# except sqlite3.Error as error:
#     print("Error while connecting to sqlite", error)
# finally:
#     if (sqliteConnection):
#         sqliteConnection.close()
#         print("The SQLite connection is closed")
