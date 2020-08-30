from flask import Flask, redirect, url_for, request, render_template, session
import db


app = Flask(__name__)
app.secret_key = b'_5aa#y2L"F4Q8z\n\xec]/'

@app.route('/')
def inicio():
   return render_template('login.html')

@app.route('/home')
def home():
    if session.get('status') ==  "Logado":
        return render_template('home.html', user=session['usuario'], lista=db.dbs())
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
      if pass1 == '1':
          session['usuario'] = user
          session['status'] = "Logado"
      else:
        if session.get('status') is None:
            return render_template('login.html', status="Falha de Login!")
        # else:
        #     return redirect(url_for('home'))

      # return render_template('home.html', res = user, pass1 = pass1)
      return redirect(url_for('home'))
   else:
       if session.get('status') is None:
           return render_template('login.html', status="Faça o Login para entrar.")
       else:
           return redirect(url_for('home'))

@app.route('/files')
def files():
    return render_template('files.html', lista=db.dbs())


@app.route('/db/<dbname>')
def homedb(dbname):
    if session.get('status') ==  "Logado":
        tabelas = db.query(dbname, 'SELECT name FROM sqlite_master WHERE type="table" ORDER BY name;')
        # print(tabelas)

        if tabelas:
            return render_template('homedb.html',user=session['usuario'], db=dbname, tabelas=tabelas)
        else:
            return render_template('homedb.html',user=session['usuario'], db=dbname)
    else:
        return redirect(url_for('login'))


@app.route('/db/<dbname>/<tabela>',methods = ['POST', 'GET'])
def hometabela(dbname, tabela):
    if request.method == 'GET':
        if session.get('status') ==  "Logado":

            select = db.query(dbname, 'SELECT * FROM ' + tabela + ';')

            if select:
                return render_template('hometabela.html',user=session['usuario'], db=dbname, tabela=tabela, select=select)
            # else:
            #     return render_template('hometabela.html',user=session['usuario'], db=dbname)
        else:
            return redirect(url_for('login'))
    else:
            select = db.query(dbname, 'SELECT * FROM ' + tabela + ';')
            if 'botao_acao' in request.form:
                if request.form['status'] == 'salvar':
                    if request.form['indice_linha'] == request.form['botao_acao']:
                        return f"salvando... dados: {request.form['valor_linha']}   , campo edit = {request.form['indice_linha']}"
                    else:
                        return render_template('hometabela.html',user=session['usuario'], db=dbname, tabela=tabela, select=select , edit=request.form['botao_acao'])

                elif request.form['status'] == 'editar':
                    return render_template('hometabela.html',user=session['usuario'], db=dbname, tabela=tabela, select=select , edit=request.form['botao_acao'])
            elif 'botao_remover' in request.form:
                res = request.form['botao_remover']
                print(res)
                return f"Removendo... dados: {request.form['botao_remover']}   , campo edit = {request.form['botao_remover'][0][0]}"

            else:
                return "q botao ??"



if __name__ == '__main__':
   app.run(debug = True)
