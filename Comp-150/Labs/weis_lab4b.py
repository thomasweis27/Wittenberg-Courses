#
# Name: Thomas Weis
# File: weis_lab4b.py
# Date: 03/04/21
#
# Desc: Determines the if a year is a leap year
#
# I Received Help From: None Received
#
# I affirm that my work upholds the highest standards of honesty and
# academic integrity at Wittenberg and that I have neither given nor
# received unauthorized assistance.
#
# Thomas Weis


def isLeapYear(yr):
    #math to determines if the year is a leap year
    if yr % 4 == 0 and yr % 100 != 0 or yr % 400 == 0:
        return True 
    else:
        return False

def main():
    #asks for year and prints the correct output
    yr = eval(input("\nEnter a year: "))
    print()
    if isLeapYear(yr):
        print(yr,"is a leap year\n")
    else:
        print(yr,"is not a leap year\n")


main ()
