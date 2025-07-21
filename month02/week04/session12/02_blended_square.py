import turtle

turtle.speed(0)
turtle.colormode(255)  # Fixed color range
turtle.penup()

for x in range(0, 200):
    turtle.goto(x - 100, -100)  # Center the drawing
    turtle.pendown()
    turtle.pencolor(255, 128, x)
    turtle.goto(x - 100, 100)   # Vertical line
    turtle.penup()

turtle.hideturtle()
turtle.done()
