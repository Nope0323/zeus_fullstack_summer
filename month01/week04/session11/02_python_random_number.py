#random number
import turtle
import random

a = random.randint(80,90)

paint = ["red","blue","pink", "purple"]
turtle.color(random.choice(paint))
turtle.dot(a)

print(a)

turtle.done()