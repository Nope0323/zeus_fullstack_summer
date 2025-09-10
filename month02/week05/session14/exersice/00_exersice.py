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
square(40,240, 240, 'red')
square(-80, 150, 100,'green')
square(-170,150,70, 'blue')
square(-30,45,50, 'purple')
square(-170,45,120, 'yellow')
square(-30,-10,200, 'orange')
square(180,-10,50, 'purple')
square(180,-70,50, 'purple')
square(180,-130,50, 'purple')


turtle.done()
