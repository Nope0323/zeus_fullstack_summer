a= 10
b=5

c=a-b
d= a+b
print(c)

#2
for a in range(11):
    print(a)

number=input("give number:")

number = int(number)

if number%2==0 :
    print("тэгш тоо")
else:
    print("сонгдгой тоо")


fruit = ["алим", "гадил", "жүрж"]
print(fruit)

print(fruit[0])
print(fruit[1])
print(fruit[2])

fruit.append('mango')
print(fruit)
#ex07
numbers = [1, 2, 2, 3, 4, 4, 5]
numbers = {1, 2, 2, 3, 4, 4, 5}
print(numbers)

#ex08
k=10
while k>=0:
    print(k)
    k=k-1

scores = [85, 90, 78, 92]
total = 0
for score in scores:
    total += score
print(total)

#ex08
class Student:    
    def __init__(self, нэр, нас, ):
        self.name = нэр
        self.age = нас

    def introduce(self):
        print(f"Сайн байна уу, миний нэр {self.name}, би {self.age} настай.")

student1 = Student("Бат", 20)

student1.introduce()
#ex09
numbers = [10, 15, 20, 25, 30] 
for nub in numbers: 
    if nub<20:
        print(nub)


#ex10
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result=set1 & set2

print (result)
