#/usr/bin/python

import re

fileImport = open(".tt/radarList.tin")

fileContent = fileImport.readline()
  
for one in fileContent:
  for shipOneVar in fileImport:
    
    regexLine = "(.*)'(.*)'(.*)(.*)"

#    searchObj = re.match(regexLine, fileContent, re.M)
    shipOne = re.match(regexLine, shipOneVar, re.M)

    echoString = "t "
    if shipOne:
      print(echoString + shipOne.group(2))

    echoString = "enemyradarCoords "
    if shipOne:
      print(echoString + shipOne.group(3))
fileImport.close()
