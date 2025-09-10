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
square(0,0, 500, 'red')
square(50,-50,400, 'orange')
square(100,-100,300, 'yellow')
square(150, -150,200,'green')
square(200,-200,100, 'blue')
square(225,-230,50, 'purple')




turtle.done()
