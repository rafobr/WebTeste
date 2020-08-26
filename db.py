import os
import sqlite3

def query(db, query):

    try:
        sqliteConnection = sqlite3.connect('db/'+str(db)+'.db')
        cursor = sqliteConnection.cursor()
        print("Database created and Successfully Connected to SQLite")
        sqlite_select_Query = query
        
        cursor.execute(sqlite_select_Query)
        record = cursor.fetchall()
        cursor.close()
        return record

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
    return listadbs
