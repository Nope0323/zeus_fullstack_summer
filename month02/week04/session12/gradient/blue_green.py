import turtle

turtle.speed(0)
turtle.colormode(255)

for square in range(0, 400):
    turtle.color(54, 93+square, 199-square)
    turtle.goto(square,0)
    turtle.goto(square,200)






turtle.done()