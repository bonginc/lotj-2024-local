from datetime import datetime
import sqlite3
import sys

xVar = str(sys.argv[1])
yVar = str(sys.argv[2])
colorVar = str(sys.argv[3])
idVar = "."

def insertCoordIntoTable(x, y, color, id):
    try:

        sqliteConnection = sqlite3.connect('.tt/shipDatabase.db')
            
        cursor = sqliteConnection.cursor()
            
        print("#showme Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO coords
                            (x_coords, y_coords, color, id) 
                            VALUES (?, ?, ?, ?);"""

        data_tuple = (x, y, color, id)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("#showme Successfully into table")

        cursor.close()

    except sqlite3.Error as error:

        print("#showme Failed to insert Python variable into sqlite table", error)
    
    finally:

        if sqliteConnection:
            sqliteConnection.close()
            print("#showme Connection closed")

insertCoordIntoTable(xVar, yVar, colorVar, idVar)
