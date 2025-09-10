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
square(-50,400,310,'yellow')
square(-50,60,150,'blue')
square(80,60,150,'blue')
square(150,60,150,'blue')
square(-50,-135,265,'red')
square(35,-135,265,'red')

square(-500,-30,60,'blue')
square(-500,-60,60,'blue')
square(-500,-90,60,'blue')
square(-500,-120,60,'blue')
square(-500,-160,60,'blue')
square(-500,-190,60,'blue')
square(-500,-220,60,'blue')
square(-500,-240,60,'blue')
square(-500,-260,60,'blue')
square(-500,-290,60,'blue')
square(-500,-310,60,'blue')

square(-420,-30,340,'yellow')








turtle.done()