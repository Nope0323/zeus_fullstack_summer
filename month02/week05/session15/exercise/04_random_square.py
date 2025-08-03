import turtle
import random

turtle.speed(0)
turtle.penup()
turtle.hideturtle()
turtle.colormode(255)
    
def square(x, y, w):
    turtle.goto(x, y)

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    turtle.fillcolor(random_color)
    turtle.begin_fill()

    for n in range (4):
        turtle.penup()
        turtle.fd(w)
        turtle.rt(90)
        turtle.penup()

       
    turtle.end_fill()

   


for l in range(0,50):
    x= random.randint(-600,600)
    y= random.randint(-600,600)
    size = random.randint(20, 200)
    square(x, y, size )

turtle.done()