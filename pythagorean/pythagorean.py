from math import *

# Introducing
print "Welcome to Kevin's pythagorean calculator"
# print the options


def options():
    print "Your Options Are:"
    print "1) If you have the length of A and B"
    print "2) If you have the length of C and A"
    print "3) If you have the length of C and B"
    print "4) Quit this program"
    return input("Choose your option:")


# For this one, we have length of a and b, and we are trying to get length of c
def AnB(a, b):
    print a**2, "+", b**2, "=", a**2 + b**2
    print sqrt(a**2 + b**2)


# For this one, we have length of c and a, and we are trying to get length of b
def CnA(c, a):
    print c**2, "-", a**2, "=", c**2 - a**2
    print sqrt(c**2 - a**2)


# For this one, we have length of c and b, and we are trying to get length of a
def CnB(c, b):
    print c**2, "-", b**2, "=", c**2 - b**2
    print sqrt(c**2 - b**2)


# The beginning of the calculating with code running
loop = 1
choice = 0
while loop == 1:
    choice = options()

    if choice == 1:
        AnB(input("A: "), input("B: "))

    elif choice == 2:
        CnA(input("C: "), input("A: "))

    elif choice == 3:
        CnB(input("C: "), input("B:  "))

    elif choice == 4:
        loop = 0

print "Thank you for using Kevin's calculator"
