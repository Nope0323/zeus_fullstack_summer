import turtle
import random

def drawBranch (x,y,size, degree):
    turtle.pu()
    turtle.goto(x,y)
    turtle.setheading(degree)
    turtle.pd()
    turtle.fd(size)
    x1 = turtle.xcor()
    y1 = turtle.ycor()

    if size>5:
        ang1 = degree - random.randint(15,25)
        ang2 = degree + random.randint(15,25)
        size1 = size * random.uniform(0.4,0.8)
        size2 = size * random.uniform(0.4,0.8)
        drawBranch(x1,y1,size1,ang1)
        drawBranch(x1,y1,size2, ang2)

turtle.speed(0)
drawBranch(0,0,100,90)
turtle.done()