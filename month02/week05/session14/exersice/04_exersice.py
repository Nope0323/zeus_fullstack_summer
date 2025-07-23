import turtle

def square(x, y,size , color):
    turtle.speed(0)
    turtle.color(color)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    for a in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()
square(-500,400,800, 'black')
square(-500,400,400,'red')
square(-45,400,300,'yellow')
square(-500,400,50,'blue')
square(-500,-40,50,'blue')
square(-500,-60,50,'blue')







turtle.done()