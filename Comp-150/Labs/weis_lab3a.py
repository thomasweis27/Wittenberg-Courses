#
# Name: Thomas Weis
# File: weis_lab3a.py
# Date: 02/11/21
#
# Desc: Computing weekly wages of a workers pay
#
# I Received Help From: None Received
#
# I affirm that my work upholds the highest standards of honesty and
# academic integrity at Wittenberg and that I have neither given nor
# received unauthorized assistance.
#
# Thomas Weis

hours = int(input("Enter hours worked: "))
rate  = int(input("Enter hourly rate: "))
grossPay = 0

if hours > 40:
    hours = hours -40
    grossPay = 40 * rate + hours * rate * 1.5
    print("Gross Pay = $ {:.2f}".format(grossPay))
else:
    grossPay = 40 * rate
    print ("Gross Pay = $ {:.2f}".format(grossPay))
