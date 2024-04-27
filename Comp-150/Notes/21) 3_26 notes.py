import turtle

t1 = turtle.Turtle()

t1.turtlesize(3, 3)
t1.forward(100)

t1.setheading(180)

t1.backward(100)
t1.forward(100)
for i in range (3):
    t1.left(120)
    t1.forward(100)

t1.setheading(180)

t1.sety(-200)
t1.xcor()
#tells user the coordnate
t1.setx(-200)

t1.goto(-300, 300)

t1.clear()

t2 = turtle.Turtle()
t2.turtlesize(1, 2)
t2. color("red")

t2.hideturtle()

t2.penup()
t2.goto(300, -300)
t2.pendown()

for i in range (3):
    t2.left(120)
    t2.forward(100)
#t2.isvisable()
#shows if turtle is visable

t2.penup()
t2.goto(0, 0)
t2.pendown()

t1.setheading(0)
t1.setheading(90)
t1.setheading(180)
t1.circle(100)


for i in range(0, 360, 10):
    t2.setheading(i)
    t2.circle(100)


