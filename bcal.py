#!/usr/bin/python3

import sys

firstInput = str(input("#echo {Enter 1 2 3 4 5 6 7 8}\n"))

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

outerMidguard = str(sys.argv[4])

if firstInput in ['1']:

    print("#echo {----------========== 1 ==========----------}")

    b1x = x + 2000
    b1y = y + 300
    b1z = z + 0

    b2x = x + 2000
    b2y = y + -300
    b2z = z + 0

    b3x = x + 2900
    b3y = y + 0
    b3z = z + 0

elif firstInput in ['2']:

    print("#echo {----------========== 2 ==========----------}")

    # [ L }
    b1x = x + -300
    b1y = y + -2000
    b1z = z + 0

    # [001]
    b2x = x + 300
    b2y = y + -2000
    b2z = z + 0

    # [002]
    b3x = x + 0
    b3y = y + -2900
    b3z = z + 0

elif firstInput in ['3']:

    print("#echo {----------========== 3 ==========----------}")

    # [ L ]
    b1x = x + -300
    b1y = y + 2000
    b1z = z + 0

    # [001]
    b2x = x + 300
    b2y = y + 2000
    b2z = z + 0

    # [002]
    b3x = x + 0
    b3y = y + 2900
    b3z = z + 0

elif firstInput in ['4']:

    print("#echo {----------========== 4 ==========----------}")

    b1x = x + -2000
    b1y = y + 300
    b1z = z + 0

    b2x = x + -2000
    b2y = y + -300
    b2z = z + 0

    b3x = x + -2900
    b3y = y + 0
    b3z = z + 0

elif firstInput in ['5']:

    print("#echo {----------========== 5 ==========----------}")

    b1x = x + 1200
    b1y = y + 1600
    b1z = z + 0

    b2x = x + 1600
    b2y = y + 1200
    b2z = z + 0

    b3x = x + 2050
    b3y = y + 2050
    b3z = z + 0

elif firstInput in ['6']:

    print("#echo {----------========== 6 ==========----------}")

    b1x = x + -1200
    b1y = y + 1600
    b1z = z + 0

    b2x = x + -1600
    b2y = y + 1200
    b2z = z + 0

    b3x = x + -2050
    b3y = y + 2050
    b3z = z + 0

elif firstInput in ['7']:

    print("#echo {----------========== 7 ==========----------}")

    b1x = x + 1600
    b1y = y + -1200
    b1z = z + 0

    b2x = x + 1200
    b2y = y + -1600
    b2z = z + 0

    b3x = x + 2050
    b3y = y + -2050
    b3z = z + 0

elif firstInput in ['8']:

    print("#echo {----------========== 8 ==========----------}")

    b1x = x + -1200
    b1y = y + 1600
    b1z = z + 0

    b2x = x + -1600
    b2y = y + 1200
    b2z = z + 0

    b3x = x + -2050
    b3y = y + 2050
    b3z = z + 0

shipOne = str(b1x) + " " + str(b1y) + " " + str(b1z)
shipTwo = str(b2x) + " " + str(b2y) + " " + str(b2z)
shipThree = str(b3x) + " " + str(b3y) + " " + str(b3z)

# Trade this with that #

# Center Midguard up front Outer in back #
if outerMidguard == "Midguard":
    print("#echo {Center Midguard up front}")
    print("battle nav $battleTwo calculate local " + shipThree)
    print("battle nav $battleOne calculate local " + shipTwo)
    print("calculate local " + shipOne)
elif outerMidguard == "Outer":
    print("#echo {Center Midguard up front}")
    print("battle nav $battleOne calculate local " + shipThree)
    print("battle nav $battleTwo calculate local " + shipTwo)
    print("calculate local " + shipOne)
