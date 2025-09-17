import math
#ex01
class Car():
    # TODO
    # Классыг ашиглах
    def __init__(self, brand, model ):
        self.brand = brand
        self.model = model
    def show_info(self):
        print(f"Машины марк: {self.brand}, Загвар: {self.model}")

my_car = Car("Toyota", "Prius")
my_car1 = Car("Mercedes","Benz")

my_car.show_info()
my_car1.show_info()

#ex02
class Student():
    def __init__(self,name,age):
        self.name= name
        self.age= age
        
    def is_adult(self):
        return self.age >= 18
    
student1 = Student("Болд", 20)
student2 = Student("Дорж", 17)
print(f"{student1.name} насанд хүрсэн үү? {student1.is_adult()}")
print(f"{student2.name} насанд хүрсэн үү? {student2.is_adult()}")

#ex03
class Circle():
    def __init__(self,input_raduis,input_p_number):
        self.raduis= input_raduis
        self.p_number=input_p_number
    def calculate_area(self):
        return  (self.raduis*self.raduis)* self.p_number
    
    def calculate_circumference(self):
        return 2*self.raduis* self.p_number

circle = Circle(5,3.14)
print(math.pi)
print(f"5 радиустай тойргийн талбай: {circle.calculate_area():.2f}")
print(f"5 радиустай тойргийн урт:{circle.calculate_circumference():.2f}")

#ex04
class BankAccount:

    def __init__(self,owner_name,balance=0):
        self.owner_name=owner_name
        self.balance= balance
    
    def deposit(self, deposit):
        # self.balance += deposit
        self.balance = self.balance + deposit
        print(f"{deposit}төгрөг нэмэгдлээ.Одоогийн үлдэгдэл:{self.balance}")
    def withdraw(self,withdraw):
        
        if self.balance>=withdraw:
            self.balance = self.balance-withdraw
            print(f"{withdraw}төгрөг нэмэгдлээ.Одоогийн үлдэгдэл:{self.balance}")
        else :
            print("Гүйлгээ амжилтгүй. Таны үлдэгдэл хүрэлцэхгүй байна.")
    
    def __str__(self):
        return f"Данс эзэмшигч: {self.owner_name}, Үлдэгдэл: {self.balance}төгрөг"
            
acc = BankAccount("Цэцэг", 50000)
acc.deposit(20000)
acc.withdraw(60000)
acc.withdraw(20000)

#ex05
print(acc)

#ex06
class Book:
    def __init__(self,title,author):
        self.title=title
        self.author= author
        
class Library :
    def __init__(self):
        self.books = []
    def add_book(self,book):
        self.books.append(book)
        print(f"{book.title} by {book.author} номыг санд нэмлээ.")

    def list_books(self):
        for book in self.books:
            print(f"{book.author}by {book.title}")

book1 = Book("Тунгалаг тамир", "Ч.Лодойдамба")
book2 = Book("Leaders Eat Last", "Simon Sinek")
library = Library()
library.add_book(book1)
library.add_book(book2)
library.list_books()


#ex07

class ShopItem:
    tax_rate = 0.1 # Бүх бараанд адилхан үйлчилнэ
    def __init__(self, name, price):
    # TODO
        self.name=name
        self.price= price
    def get_total_price(self):
        # TODO
        # Классыг ашиглах
        return self.price+(self.price * self.tax_rate)
item1 = ShopItem("Талх", 2000)
item2 = ShopItem("Сүү", 3500)
print(f"{item1.name}-ийн нийт үнэ: {item1.get_total_price()}")
print(f"{item2.name}-ийн нийт үнэ: {item2.get_total_price()}")

class Animal:
    # TODO
    def speak():
        print("hh")
class Dog(Animal):
    # TODO
    def dog_speak():
        print("Hav Hav!")
class Cat(Animal):
    # TODO
    def cat_speak():
        print("Miyav!")

    # Классыг ашиглах
my_dog = Dog()
my_cat = Cat()
my_dog.speak()
my_cat.speak()