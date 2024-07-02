#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- Coding by Jon Posey

import sqlite3

database = sqlite3.connect('shipStats.db')


def sql_fetch(database):
    cursorObj = database.cursor()

    cursorObj.execute('SELECT * FROM ships ORDER BY proximity ASC')
    rows = cursorObj.fetchall()

    for row in rows:
        print(row)


sql_fetch(database)
database.close()
