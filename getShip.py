from datetime import datetime
import sqlite3
import sys

nameVar = str(sys.argv[1])
shipVar = str(sys.argv[2])
dockVar = str(sys.argv[3])
planetVar = str(sys.argv[4])
dateVar = datetime.now()
characterVar = str(sys.argv[5])


def insertVariableIntoTable(name, ship, dock, planet, date, character):
    try:

        sqliteConnection = sqlite3.connect('.tt/shipDatabase.db')
            
        cursor = sqliteConnection.cursor()
            
        print("#showme Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO ships
                            (name, ship, dock, planet, date, character) 
                            VALUES (?, ?, ?, ?, ?, ?);"""

        data_tuple = (name, ship, dock, planet, date, character)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("#showme Python Variables inserted successfully into SqliteDb_developers table")

        cursor.close()

    except sqlite3.Error as error:

        print("#showme Failed to insert Python variable into sqlite table", error)
    
    finally:

        if sqliteConnection:
            sqliteConnection.close()
            print("#showme The SQLite connection is closed")

insertVariableIntoTable(nameVar, shipVar, dockVar, planetVar, dateVar, characterVar)
