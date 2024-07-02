import sys

true = str(sys.argv[1])
one = int(sys.argv[2])
two = int(sys.argv[3])
three = int(sys.argv[4])

if true == "yes":
    print("calculate local " + str(one) + " " + str(two) + " " + str(three))
else:
    inputOne = one + 625
    inputTwo = two + 525
    print("calculate local " + str(inputOne) + " " + str(inputTwo) + " " + str(three))
