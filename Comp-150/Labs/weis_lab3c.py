#
# Name: Thomas Weis
# File: weis_lab3c.py
# Date: 02/11/21
#
# Desc: Tells the user which year is a leap year
#
# I Received Help From: None Received
#
# I affirm that my work upholds the highest standards of honesty and
# academic integrity at Wittenberg and that I have neither given nor
# received unauthorized assistance.
#
# Thomas Weis


year = int(input("Enter a year: "))

if (year%4==0):
    if (year % 100 == 0):
        if (year %400 == 0):
            print (year, "is a leap year")
        else :
            print (year, "is not a leap year")
    else:
        print (year, "is a leap year")
else:
    print (year, "is not a leap year")
    
