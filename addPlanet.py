from datetime import datetime
import sqlite3
import sys

planetVar = str(sys.argv[1])
xVar = str(sys.argv[2])
yVar = str(sys.argv[3])
colorVar = str(sys.argv[4])

def insertPlanetIntoTable(planet, x, y, color):
    try:

        sqliteConnection = sqlite3.connect('.tt/shipDatabase.db')
            
        cursor = sqliteConnection.cursor()
            
        print("#showme Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO planets
                            (planet, x_planet, y_planet, color)
                            VALUES (?, ?, ?, ?);"""

        data_tuple = (planet, x, y, color)
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

insertPlanetIntoTable(planetVar, xVar, yVar, colorVar)
