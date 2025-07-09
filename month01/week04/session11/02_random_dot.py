import random
import turtle

# a= input("loop number:")
# limit_number = int(a)
a = random.randint(24,30)
for n in range(10):
    x= random.randint(0,100)
    y= random.randint(0,100)
    
    paint = ["red","blue","pink", "purple"]
    turtle.color(random.choice(paint))
    turtle.dot(a)
    turtle.goto(x,y)
    print(x,y)
turtle.done()