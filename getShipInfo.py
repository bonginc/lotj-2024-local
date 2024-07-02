#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- Coding by Jon Posey

import sqlite3
import sys

database = sqlite3.connect('.tt/shipDatabase.db')

inputVar = str(sys.argv[1])
inputVar2 = str(sys.argv[2])
searchShip = str(sys.argv[3])

def getShip(database):
    cursorObj = database.cursor()
    cursorObj.execute('SELECT ship, name FROM ships ORDER BY ship')
    rows = cursorObj.fetchall()
    listIt = '\n#showme '
    if inputVar.lower() in ['yes']:
        for row in rows:
            print("\r")
            print(str(row))
    else: 
        for row in rows:
            print(str(listIt) + str(row))

def deleteShip(database,name):
        try:
            cursor = database.cursor()
            print("Connected to SQLite")

            sql_update_query = """DELETE from ships where name = ?"""
            cursor.execute(sql_update_query, (name,))
            database.commit()
            print("Record deleted successfully")
            cursor.close()
        except sqlite3.Error as error:
            print("Failed to delete reocord from a sqlite table", error)
        finally:
            if cursor:
                cursor.close()
                print("sqlite connection is closed")

def getOwner(database):
    cursorObj = database.cursor()
    cursorObj.execute('SELECT name,ship FROM ships ORDER BY name')
    rows = cursorObj.fetchall()
    listIt = '\n#showme '
    if inputVar.lower() in ['yes']:
        for row in rows:
            print("\r")
            print(str(row))
    else: 
        for row in rows:
            print(str(listIt) + str(row))

def getAll(database):
    cursorObj = database.cursor()
    cursorObj.execute('SELECT * FROM ships')
    rows = cursorObj.fetchall()
    listIt = '\n#showme '
    if inputVar.lower() in ['yes']:
        for row in rows:
            print("\r")
            print(str(row))
    else: 
        for row in rows:
            print(str(listIt) + str(row))

if inputVar.lower() in ['yes']:
    if inputVar2.lower() in ['all']:
        print("write")
        print("Name,            Ship,                   Docked,                    Planet")
        print("#send \r")
        getAll(database)
        print("#send \r\r")
        print("/l")
    elif inputVar2.lower() in ['name']:
        print("write")
        print("#send")
        print("Name,            Ship")
        print("#send;#send")
        getOwner(database)
        print("#send;#send")
        print("/l")
    elif inputVar2.lower() in ['delete']:
        deleteShip(database,searchShip)
    elif inputVar2.lower() in ['ship']:
        print("write")
        print("#send")
        print("Ship,                                        Name")
        getShip(database)
        print("#send;#send")
    else:
        print("#showme ERROR!")
else:
    if inputVar2.lower() in ['all']:
        print("#showme Name,            Ship,                       Docked at,                    Planet")
        getAll(database)
        print("#send;#send")
    elif inputVar2.lower() in ['name']:
        print("#showme Name,            Ship")
        print("#send")
        getOwner(database)
        print("#send;#send")
    elif inputVar2.lower() in ['ship']:
        print("#send")
        print("#showme Ship,                                        Name")
        getShip(database)
        print("#send;#send")
    elif inputVar2.lower() in ['delete']:
        deleteShip(database,searchShip)
    else:
        print("#showme ERROR!")

#ships = ()
database.close()
