import turtle

turtle.speed(0)
turtle.colormode(255)

for square in range(0, 200):
    turtle.color(255, 128, square)
    turtle.goto(square,0)
    turtle.goto(square,200)




turtle.done()