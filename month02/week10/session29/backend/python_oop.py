#object oreiented programing in python
#python class- keyword
#atteribute of class
#body - integer
#height - float
#name-str
#skin_color- str
#spirit- integer
#is_single- boolen
class Human:
    body= 1
    eyes= 2
    name="human"
    skin_color = "biege"
    spirit = 1
    is_single= True
boldoo = Human() #boldoo
print(boldoo)
print(boldoo.name)#name
boldoo.name= 'Boldoo'
khangai= Human()
print(khangai)
print(khangai.name)#name
khangai.name ='Khangai'
print(khangai.name)
#init mentod
#class mentod - function

class Cat :
    species ="Felis catus"
    def __init__(self):
        age = 1
egyptian_cat = Cat()
bohomian_cat = Cat()

egyptian_cat.age = 3
bohomian_cat.age = 10
print (bohomian_cat)
print (egyptian_cat)
class Dog:
    species= "Canis familiaris"
    def __init__(self, name, age):
        #self n tuhain classaas obj uusgehed hergelne
        self.name = name
        self.age = age

bulldog = Dog('Bulldog', 2)

banhar = Dog('Mongol banhar', 4)
print(bulldog)
bulldog.age = 3
print(banhar)
class Car :
    def __init__(self,brand,style,engine,mirror,door,tire):
        self.brand = brand
        self.style= "SUV"
        self.engine =3.4
        self.mirror= 2
        self.door =4
        self.tire= 4

mercedes = Car()
print(f'The car brand is {mercedes.brand} and has the style of {mercedes.style}')

audi= Car()
print(f'The car brand is {audi.brand} and has the style of {audi.style}')

mercedes.brand ='Mercedes Benz'
mercedes. engine =2.5
mercedes. tire_number = 4
mercedes.style ='Sport'    
print(f'The car brand is {mercedes.brand} and has the style of {mercedes.style}')

mercedes.brand ='Audi Benz'
mercedes. engine =3.5
mercedes. tire_number = 4
mercedes.style ='Sedan'    
print(f'The car brand is {audi.brand} and has the style of {audi.style}')

class Animal :
    species ="Animalus catus"
    is_mammal = False

    def __init__(self,age, eats_plant,legs):
        self.age = age 
        self.eat_plant = eats_plant
        self.legs = legs
    
trapped_wolf = Animal(4,False,3)
trapped_wolf.is_mammal = True

# elepant = Animal(3, True,4)
# elepant.is_mammal = True
#     def __str__(self):
#         return f"""
#             The Animal is mammal {self.is_mammal}, {self.age}
#             years old. It eats plant {self.eats_plant} and has (self.legs)
#         """
        
# print (wolf)
# print (elepant)

class Book:
    def __init__(self, title , autor, page):
        self.title = title
        self.autor = autor
        self.page = page
    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.page} pages"
        
my_book = Book ("The Hobbit", "J.R.R. Tolkien",310)

book_best = Book("Strange Man", "Albert Camus", 140)

class Student:
    def __init__(self, name , grade):
        self.title = name
        self.autor = grade
    def __str__(self):
        return f"'{self.name}' by {self.grade}"

student1 = Student("Alice", "10th")
student2 = Student("Alice", "11th")
student3 = Student("Alice", "09th")