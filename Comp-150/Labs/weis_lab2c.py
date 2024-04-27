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
import math

print("Compinations Program")

n = int(input("Enter number of items: "))
k = int(input("Enter number to chose: "))

solution = (math.factorial(n))//(math.factorial(k)*math.factorial(n-k))

print (n, "choose", k, "is", solution)

