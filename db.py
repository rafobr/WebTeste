import os
import sqlite3

def query(db, query):

    try:
        sqliteConnection = sqlite3.connect('db/'+str(db)+'.db')
        cursor = sqliteConnection.cursor()
        print("Database created and Successfully Connected to SQLite")
        sqlite_select_Query = query

        cursor.execute(sqlite_select_Query)
        # print(cursor.description)
        record = cursor.fetchall()

        #buscando nome das colunas
        colunas = list(map(lambda x: x[0], cursor.description))
        # print(colunas)
        cursor.close()

        resultado = {
            'colunas': colunas,
            'linhas' : record
        }
        print('resultadoquery:', resultado)
        return resultado

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

def dbs():
    path = 'db'
    listafiles = os.listdir(path)
    listadbs = map(lambda x: x.rsplit('.' , 1)[0], listafiles)
    # print(list(listadbs))
    return listadbs
