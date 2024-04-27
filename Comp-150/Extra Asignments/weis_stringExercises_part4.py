#
# Name: Thomas Weis
# File: weis_stringExercises_part4.py
# Date: 03/10/2021
#
# Desc: switches the beginnings 2 letters of two given strings
#
# I Received Help From: None Received
#
# I affirm that my work upholds the highest standards of honesty and
# academic integrity at Wittenberg and that I have neither given nor
# received unauthorized assistance.
#
# Thomas Weis

def main():
    one = input("Please enter string one: ")
    two = input("Please enter string two: ")

    #switches the beginnings
    newOne = two[:2] + one[2:]
    newTwo = one[:2] + two[2:]

    #combines and prints
    both = newOne + " " + newTwo
    print (both)

main()
