#!/usr/bin/python3

import re

fileImport = open(".tt/radarList.tin")

global x,y,z,shipName

def strip():

#=============================================================
# Imports from file and strips front and back ascii code
#=============================================================

  for fileContent in fileImport:
    global x,y,z,shipName

    frontStripped1 = re.sub("\x1b\[1;36m", '', fileContent)

    regexMatch = "(.*)'(.*)'(.*)[0-9]"

    backStripped1 = re.sub("\x1b\[",'',frontStripped1)

    searchObj1 = re.match(regexMatch, backStripped1, re.M)

    if searchObj1:
      shipName = str(searchObj1.group(2).strip())
      shipX = searchObj1.group(3).strip()
      splitShip = shipX.split(" ")
      x = splitShip[0]
      y = splitShip[1]
      z = splitShip[2]
      print(shipName)
      print(x)
      print(y)
      print(z)
      return x,y,z
