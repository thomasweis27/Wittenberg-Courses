#
# Name: Thomas Weis
# File: weis_lab1d.py
# Date: 01/28/2021
#
# Desc: Program calculating quotent and remainder of devision of two numbers.
#
# I Received Help From: None Received
#
# I affirm that my work upholds the highest standards of honesty and
# academic integrity at Wittenberg and that I have neither given nor
# received unauthorized assistance.
#
# Thomas Weis
#

print("Making Change Program")

cents = int(input("Enter an amound of cents: "))

print(cents, "cents is: ")
quarters = cents//25
cents = cents%25
dimes = cents//10
cents = cents%10
nickles = cents//5
cents = cents%5
pennies = cents//1

print (quarters, "quarters")
print (dimes, "dimes")
print (nickles, "nickles")
print (pennies, "pennies")





