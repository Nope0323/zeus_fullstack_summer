import turtle

def square(x, y,size , color):
    turtle.color(color)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    for a in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()
square(40,200, 240, 'red')
square(-100, 240, 160,'purple')
square(-260,100,260, 'yellow')

turtle.done