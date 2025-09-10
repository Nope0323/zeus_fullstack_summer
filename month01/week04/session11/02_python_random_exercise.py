import random 
import turtle

range_number= input("range number:")
range_limit = int(range_number)

a = random.randint(24,30)

for n in range(range_limit):
    x= random.randint(0,100)
    y= random.randint(0,100)
    turtle.width(random.randint(1, 26))
    paint = ["green", "blue", "pink", "purple", "yellow"]
    turtle.color(random.choice(paint))
    turtle.dot(a)
    turtle.goto(x,y)
    print(x,y)

turtle.done()


turtle.done()