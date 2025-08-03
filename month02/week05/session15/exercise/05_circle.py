import turtle
import random

turtle.speed(0)
turtle.hideturtle()
turtle.penup()
turtle.colormode(255)  

def circle(x, y, w):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    
    turtle.goto(x, y)
    turtle.dot(w, color)
    
    if w > 40:
        circle(x, y, w - 10)

circle(0, 0, 400)

turtle.done()
