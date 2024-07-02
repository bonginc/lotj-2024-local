#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- Coding by Jon Posey

import sqlite3

conn = sqlite3.connect('.tt/shipDatabase.db')

curr = conn.cursor()

table = ''' 
CREATE TABLE ships (
    NAME TEXT (20),
    SHIP TEXT (20),
    DOCK TEXT (20),
    PLANET TEXT (20),
    DATE TEXT (20),
    CHARACTER TEXT (20)
)
'''
coords = '''
CREATE TABLE coords (
    id INTEGER (20),
    X_COORDS INTEGER (20),
    Y_COORDS INTEGER (20),
    COLOR TEXT (20)
)
'''
planets = '''
CREATE TABLE planets (
    planet TEXT (20),
    X_PLANET INTEGER (20),
    Y_PLANET INTEGER (20),
    COLOR TEXT (20)
)
'''

try:
    curr.execute(planets)
    curr.execute(table)
    curr.execute(coords)
    print("#showme {table made}")
except:
    print('error in table')
conn.close()
