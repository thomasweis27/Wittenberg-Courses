# Name: Thomas Weis
# File: weis_assignment6.py
# Date: 5/10/21
#
# Desc: recursive spiral turtle function
#
# I Received Help From: None Received
#
# I affirm that my work upholds the highest standards of honesty and
# academic integrity at Wittenberg and that I have neither given nor
# received unauthorized assistance.
#
# Thomas Weis

import turtle

def spiral(t, size):
    #finds the radius for the size of the circle
    radius = (size*4)/(2*3.14159)
    #print(radius)

    #bass case for when size is less than one
    if radius < 1:
        return False

    #if its bigger than the bass case then it makes the quarter circle
    t.circle(radius,90)
    size = size*.90
    spiral(t, size)


def main():
    #makes turtle and puts it in right spot
    t = turtle.Turtle()
    t.forward(300)
    t.setheading(90)
    t.hideturtle()
    t.clear()
    size = 300
    spiral(t, size)

main()


"""
The reason the spiral does not look like the expected output is the 
   expected output in the pdf has a RADIUS of 300, not have the quarter
   circle have the length of 300 as required by the asignment guidelines.
   
"""
