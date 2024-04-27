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

print("Exponential Decay Program")

amountInitial = float(input("Enter the amount of material in grams: "))
decayConstant = float(input("Enter the decay constant: "))
timePassed = float(input("Enter the amount of time in years: "))

solution = amountInitial * math.exp(-decayConstant*timePassed)

print("The amount of material left after", int(timePassed), "years is", solution, "grams.")
