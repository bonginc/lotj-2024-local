#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import re

#===============================
# setup 
#===============================

fig = plt.figure(figsize=(10,10))

badGuyRed = "red"
goodGuyGreen = "green"

a1 = fig.add_subplot(1,1,1, projection='3d')

a1.set_title('Lotj')

a1.set_xlabel('X plane')
a1.set_ylabel('Y plane')
a1.set_zlabel('Z plane')
a1.xaxis.labelpad = 10
a1.yaxis.labelpad = 20
a1.zaxis.labelpad = 30
a1.dist = 10

#=============================================================
# Imports from file and strips front and back ascii code
#=============================================================

def strip():

    fileImport = open("~/.tt/radarList.tin")

    for fileContent in fileImport:

        frontStripped1 = re.sub("\x1b\[1;36m", '', fileContent)

        regexMatch = "(.*)'(.*)'(.*)[0-9]"

        backStripped1 = re.sub("\x1b\[",'',frontStripped1)

        searchObj1 = re.match(regexMatch, backStripped1, re.M)

        if searchObj1:

            shipName = str(searchObj1.group(2).strip())
            shipX = searchObj1.group(3).strip()
            splitShip = shipX.split(" ")
#============================================================
# add to np.array([])
#============================================================
            shipName = str(searchObj1.group(2).strip())
            xStrip = splitShip[0]
            yStrip = splitShip[1]
            zStrip = splitShip[2]

            x = np.array([xStrip])
            y = np.array([yStrip])
            z = np.array([zStrip])

            a1.scatter3D(float(x),float(y),float(z),color=badGuyRed)
            a1.text(float(x),float(y),float(z),color="red",s=shipName)

strip()
plt.show()
#plt.savefig('plot.png', bbox_inches='tight')
