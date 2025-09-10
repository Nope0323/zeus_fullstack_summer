import turtle

turtle.colormode(255)
turtle.speed(0)
# turtle.bgcolor("black")  

paint1 = ["orange", "green", "red", "blue", "purple"]

for i, a in enumerate(range(250, 0, -10)):  # Add loop index i
    turtle.color(paint1[i % len(paint1)])  # Cycle through colors in order
    turtle.dot(a)

turtle.done()

