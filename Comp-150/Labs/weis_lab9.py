# Name: Thomas Weis
# File: weis_lab8.py
# Date: 04/17/21
#
# Student Gpa Calculator
#
# I Received Help From: None Received
#
# I affirm that my work upholds the highest standards of honesty and
# academic integrity at Wittenberg and that I have neither given nor
# received unauthorized assistance.
#
# Thomas Weis


import turtle

def draw_shell():
    #move the pen to the starting location
    t.penup()
    t.setpos(100, 0)
    t.setheading(45+90)
    t.pendown()
    #this is the size of the oval
    size = 200
    for i in range(2):
        t.circle(size,90)
        t.left(135)
        t.forward(283)
        t.backward(283)
        t.right(90)
        t.forward(140)
        t.backward(140)
        t.right(45)
        t.circle(size//2,90)
        

def shell_lines():
    #vert lines
    t.circle(200,23)
    t.left(112)
    t.forward(230)
    t.backward(230)
    t.right(112)
    t.circle(200,22)
    t.left(90)
    t.forward(260)
    t.backward(260)
    t.right(90)
    t.circle(200,22)
    t.left(68)
    t.forward(230)
    t.backward(230)
    t.right(68)
    t.circle(200,23)

    #horr lines
    t.circle(100,45)
    t.left(90)
    t.forward(341)
    t.left(90)
    t.circle(100,15)


def head():
    t.right(180)
    t.circle(30,60)
    t.circle(60,50)


    #now its a happy turtle because it has a face and can see! Its also smiling!
    
    #mouth
    t.right(40)
    t.circle(15,-90)
    t.circle(15,90)
    t.left(40)
    
    t.circle(60,40)
    t.circle(30,90)
    t.circle(60,100)

    #eye
    t.penup()
    t.setpos(185, -5)
    t.pendown()
    t.setheading(0)
    t.circle(5)

    #nose
    t.penup()
    t.setpos(210, -20)
    t.pendown()
    t.setheading(0)
    t.circle(1)
    

def legs():
    t.penup()
    t.setpos(75, -162)
    t.pendown()
    t.setheading(270)
    t.forward(90)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(65)

    t.penup()
    t.setpos(-100, -190)
    t.pendown()
    t.setheading(270)
    t.forward(60)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(90)





t = turtle.Turtle()
draw_shell()
shell_lines()
head()
legs()


