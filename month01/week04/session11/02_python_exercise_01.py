import turtle
import random


t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("white")
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "black"]

# Draw burst pattern with random line lengths
for _ in range(100):
    t.color(random.choice(colors))
    t.width(5)
    line_length = random.randint(50, 150)  # <-- Random line length
    t.forward(line_length)
    t.backward(line_length)
    t.right(random.randint(3, 10))  # Randomized angle

t.hideturtle()
turtle.done()