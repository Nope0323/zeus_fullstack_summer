import turtle
import random

turtle.speed(0)
turtle.hideturtle()
turtle.colormode(255)

def draw_star(x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()  
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    turtle.pencolor(r, g, b)
    for _ in range(5):
        turtle.forward(size) 
        turtle.right(144)    

    turtle.penup()

for _ in range(50):
    x = random.randint(-600, 600)
    y = random.randint(-600, 600)
    size = random.randint(20, 200)
    draw_star(x, y, size)

turtle.done()