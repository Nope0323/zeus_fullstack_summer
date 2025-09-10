import turtle
import random

turtle.speed(0)
turtle.colormode(255)
turtle.width(1)

for n in range(0, 225):
    # Generate a random RGB color
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    turtle.pencolor(r, g, b)
    turtle.forward(n * 2)
    turtle.right(90)

turtle.done()
