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


print ("Quadratic Formula Solver")

a = int(input("Enter the coefficient a: "))
b = int(input("Enter the coefficient b: "))
c = int(input("Enter the coefficient c: "))


answerOne = (-b + math.sqrt(b*b - 4*a*c))/(2*a)
answerTwo = (-b - math.sqrt(b*b - 4*a*c))/(2*a)

print (answerOne)
print (answerTwo)
print ("The solutions are:", answerOne, answerTwo)
