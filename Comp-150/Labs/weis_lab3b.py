#
# Name: Thomas Weis
# File: weis_lab3b.py
# Date: 02/11/21
#
# Desc: Computes wether numbers are prime or composite
#
# I Received Help From: None Received
#
# I affirm that my work upholds the highest standards of honesty and
# academic integrity at Wittenberg and that I have neither given nor
# received unauthorized assistance.
#
# Thomas Weis


num = int(input("Enter a number: "))
numOfDiv = 0

#tests to see the number of divisors
for i in range (1, num):
    if num%i == 0:
        numOfDiv = numOfDiv + 1

        

#finds if the number of divisors is > 1 and if so the ## is prime
if numOfDiv > 1:
    print(num, "is composite, with", numOfDiv, "divisors.")
else:
    print(num, "is prime, with", numOfDiv, "divisors.")
