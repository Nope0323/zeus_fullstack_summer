import turtle
import random

def drawBranch (x,y,size, degree):
    turtle.pu()
    turtle.goto(x,y)
    turtle.setheading(degree)
    turtle.pd()
    turtle.color('brown')
    turtle.width(size*0.08)
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
    else :
        turtle.colormode(255)
        turtle.color(0,random.randint(50,200),0)
        turtle.dot(4)

for a in range(6): #x tenhlegiin bair soligdoj bga 
    x=200 *a - 400
    drawBranch(x,-100,100,90)
turtle.done()