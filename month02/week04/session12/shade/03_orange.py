import turtle

turtle.colormode(255)
turtle.speed(0)
turtle.bgcolor("black")
paint1 = ["black",  "red"]
for a in range(250,0,-3):
    turtle.color(255,a,0)
    turtle.dot(a)

turtle.done()