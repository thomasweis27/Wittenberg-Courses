import turtle

def rec (trt1, upLeftCorner, xlength, ylength):
    trt1.penup()
    trt1.setposition(upLeftCorner)
    trt1.setheading(0)
    trt1.pendown()
    trt1.forward(xlength)
    trt1.right(90)
    trt1.forward(ylength)
    trt1.right(90)
    trt1.forward(xlength)
    trt1.right(90)
    trt1.forward(ylength)
    trt1.right(90)


trt1 = turtle.Turtle()
rec(trt1, (-100, -100), 100, 200)
