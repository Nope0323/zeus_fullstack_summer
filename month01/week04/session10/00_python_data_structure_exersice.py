#Variables
message = "Hello, world!"
 
print(message)

a=7
b=3

product = a+b 
total = a*b

print(product, total)

your_name = "Bold_Erdene"
parent_name ="Enkhtsetseg"

full_name = your_name+parent_name

print(full_name)

x=5
y=10
temp=x
x=y
y=temp

print("x=",x)
print("y=",y)

text = '123'
num= int(text)

print(num)
print(type(num))

#dictionary

student={'John':'20'}
#Major = {"name": "John", "age": 20,}
student["major"] = "Physics"
print(student)

fruit_prices = {'apple': 1.5, 'banana': 0.75}

fruit_prices ['apple']=2,0

#favorit_sport[" Ralf Williams"] = "Ice Hokey"
print (fruit_prices)

fruit_prices['orange']=1.25
del fruit_prices["banana"]

print(student)

students_grades = {
    'Alice':{'math': 70, 'science': 86},
    'Bob':{'math': 79, 'science': 96},
    'Samira':{'math': 90, 'science': 86}
    
    }

print(students_grades)

colors = ['red', 'green', 'blue']

print(colors)

colors.append('orange')

colors.insert(1,'yellow')

print(colors)
print(colors[0:3])
print(colors[-1])
print(colors[0])

colors.remove('green')

find = colors.find('blue')
print(find)