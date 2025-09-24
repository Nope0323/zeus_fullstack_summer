import math

#ex01
def greet():
    print("greet")

#ex02
def greet_by_name(name):
    print(f"Сайн уу,  {name}")

greet_by_name("Болд") 
greet_by_name("Сарнай")

#ex03

def add_and_print(a, b):
# TODO
    c=a+b
    print(a,"+",b,"=",c)
add_and_print(5, 3)
add_and_print(100, 200)

#ex04
def add_and_return(a, b):
# TODO
    hariu=a+b

    return hariu
hariu = add_and_return(10, 20)
print(f"Функцээс буцаасан утга: {hariu}")
print(f"Шууд хэвлэх: {add_and_return(-5, 5)}")

#ex05
def calculate_rectangle_area(length, width):
    """Тэгш өнцөгтийн талбайг тооцоолж буцаана."""
# TODO
    talbai1=length*width

    return talbai1
talbai1 = calculate_rectangle_area(10, 5)
print(f"10x5 хэмжээтэй тэгш өнцөгтийн талбай: {talbai1}")

#ex06
def is_even(number):
    """Тоог тэгш эсэхийг шалгаж True/False буцаана."""
# TODO
    if number%2 == 1:
        return False
    else:
        return True
   
print(f"10 тэгш тоо мөн үү? {is_even(10)}")
print(f"7 тэгш тоо мөн үү? {is_even(7)}")

#ex07
def power(base, exponent):
    """Суурийг зэрэгт дэвшүүлнэ."""
    gf = base**exponent
    return gf
# TODO
print(f"2-ын 3 зэрэг: {power(2, 3)}")
print(f"5-ын 2 зэрэг: {power(5, 2)}")

def get_first_char(word):
    """Үгний эхний үсгийг буцаана."""
    # first=word[0]
    return word[0]
# TODO
print(f"'Python' гэдэг үгний эхний үсэг: {get_first_char('Python')}")

def greet_country(name, country="Монгол"):
    """Хэрэглэгчийн нэр, улсыг авч мэндчилнэ."""
    print(name,country)
# TODO
greet_country("Дорж") # Өгөгдмөл утгыг ашиглах
greet_country("John", "АНУ") # Шинэ утга оруулах

#ex10
def find_max(a, b):
    """Хоёр тооны ихийг олж буцаана."""
    return max(a, b)
# TODO
print(f"100 ба 200-ийн их нь: {find_max(100, 200)}")

#ex11

def find_max_of_three(a, b, c):
    """Гурван тооны ихийг олохдоо find_max функцийг ашиглана."""
    return max(a, b,c)
# TODO
print(f"10, 25, 15-ын хамгийн их нь: {find_max_of_three(10, 25, 15)}")

#ex12
def circle_stats(radius):
    """Тойргийн талбай ба периметрийг зэрэг буцаана."""
    perimetr = (radius*radius)* pi
    talbai = (2*radius*pi)
    return perimetr, talbai
pi = 3.14
# TODO
talbai, perimetr = circle_stats(10)
print(f"10 радиустай тойргийн талбай: {talbai}, периметр: {perimetr}")

#ex13 
def sum_list(numbers):
    """Жагсаалтан дахь тоонуудын нийлбэрийг буцаана."""
    return sum(numbers)
# TODO
my_list = [1, 2, 3, 4, 5]
print(f"{my_list} жагсаалтын нийлбэр: {sum_list(my_list)}")

#ex14
def count_vowels(sentence):
    """Өгүүлбэр дэх эгшгийн тоог буцаана."""
    vowels = "аэиоу"
    # TODO
    return len(vowels)
print(f"'Сайн байна уу' гэдэгт {count_vowels('Сайн байна уу')} эгшиг бий.")

#ex15
def describe_pet(animal_type, pet_name):
    """Амьтны төрөл, нэрийг хэвлэнэ."""
    print(f"Надад {animal_type} байдаг ")
    print(f"Түүний нэрийг {pet_name} гэдэг ")
# TODO
describe_pet(pet_name="Банхар", animal_type="нохой")

#ex16
def celsius_to_fahrenheit(celsius):
    """Цельсийг Фаренгейт рүү хөрвүүлнэ."""
# TODO
    return c*9/5+32
c = 25
f = celsius_to_fahrenheit(c)
print(f"{c}°C нь {f}°F-тэй тэнцүү.")
#ex17
def fizzbuzz_check(number):
    # TODO
    if number%3==0:
        return"fizz"
    elif number%5==0:
        return"buzz"
    elif  number%3==0 and number%5==0 :
        return"fizzbuzz"
    else :
        return number
    

for i in range(1, 21):
    print(fizzbuzz_check(i))

    def countdown(n):
    """n-ээс 1 хүртэл ухраан тоолдог рекурсив функц."""
# TODO
countdown(n - 1) # Өөрийгөө дахин дуудах
countdown(5)