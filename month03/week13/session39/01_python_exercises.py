#ex01
print("Сайн уу, Python!")
#ex02
class Name():
    def __init__(self,name ):
            self.name = name
    def show_info(self): 
            print(f"Сайн уу, {self.name}")

name =Name ("Тэмүүлэн!")
#ex03
name.show_info()

class Date():
    def __init__(self,ognoo,sar,jil ):
            self.ognoo = ognoo
            self.sar = sar
            self.jil = jil
    def show_info(self): 
            print(f"{self.jil}оны {self.sar}-р сарын{self.ognoo}")

jil = Date (19,9,2025)
jil.show_info()

#ex04
class Ishlel():
    def __init__(self,durtаi_ishlel):
              self.durtаi_ishlel= durtаi_ishlel
        
    def show_info(self):
              print(f"{self.durtаi_ishlel}")

durtаi_ishlel = Ishlel("Humans are creatures, who their lifes trying to convince themselves, that existence is not absurd _Alber Camus_")
durtаi_ishlel.show_info()

#ex05
class Full_name():
    def __init__(self,first_name, last_name):
              self.first_name= first_name
              self.last_name = last_name  
    def show_info(self):
              print(f"{self.first_name} {self.last_name}")
            
first_name = Full_name("Enkhtsetseg", "Bold-Erdene")
first_name.show_info()

#ex06
class Full_name():

    def __init__(self,first_name, last_name):
              self.first_name= first_name
              self.last_name = last_name
            
                    
    def show_info(self):
              print(f"{self.first_name} {self.last_name}")
            
first_name = Full_name("Enkhtsetseg", "Bold-Erdene")
first_name.show_info()


#ex07
input_name = input("Таны нэр хэн бэ? ")
print(f"Сайн уу, {input_name}!")
#ex08
input_color = input("Таны дуртай өнгө юу вэ? ")
print(f"Таны дуртай өнгө бол {input_color} юм байна.")
#ex09
input_city = input("Та аль хотод төрсөн бэ? ")
print(f"Та {input_city} хотод төрсөн юм байна.")
#ex10
input_first_name= input("Таны овог хэн бэ?")
input_last_name = input("Таны нэр хэн бэ?") 
print(f"Таны бүтэн нэр {input_first_name} {input_first_name}")
#ex11
input_book = input("Таны дуртай ном юу вэ?")
print(f"Надад ч гэсэн {input_book} ном таалагддаг.")
#ex12
input_pet =input("Таны гэрийн тэжээвэр амьтны нэр юу вэ?")
print(f"Сайн уу, {input_pet} Чи сайн амьтан шүү.")
#ex13
input_dream =input("Таны мөрөөдлийн ажил юу вэ?")
print(f"Та ирээдүйд мундаг {input_dream} болох болно!")
#ex14
input_food = input('Таны дуртай хоол юу вэ?')
print(f"Тантай адилхан, надад ч гэсэн {input_food} таалагддаг.")
#ex15
input_country = input('Улсын нэр оруулна уу:')
input_capitral = input('улсын нийслэлийн нэрийг оруулна уу:')
print(f"{input_country}-ын нийслэл бол {input_capitral}.")
#ex16
input_film = input('Таны дуртай киноны нэр юу вэ?')
print(f"Зүрхний хилэн бол {input_film}")
#ex17
input_number = input('Таны тоо:')
input_number= int(input_number)
input_number =input_number*2
print(f"Таны оруулсан тоог 2-оор үржүүлэхэд {input_number} гарна.")
#ex18
a = input('a too:')
b = input('b too:')
a = int(a)
b = int(b)
print(a+b)
#ex19
a_too = input('Эхний тоог оруулна уу:')
b_too = input('Хоёр дахь тоог оруулна уу:')
a = int(a)
b = int(b)
c_too= (a-b) 
print(f"Эдгээр тооны ялгавар нь:{c_too}")
#ex20
a_plus = input('Эхний тоог оруулна уу:')
b_plus = input('Хоёр дахь тоог оруулна уу:')
a = int(a)
b = int(b)
c_result= (a*b) 
print(f"Эдгээр тооны үржвэр нь:{c_result}")
#ex21
a_noogdwor = input('Эхний тоог оруулна уу:')
b_noogdwor = input('Хоёр дахь тоог оруулна уу:')
a = int(a)
b = int(b)
c_noogdwor= (a/b) 
print(f"Эдгээр тооны ноогдвор нь:{c_noogdwor}")
#ex22
birth_day = input('Та хэдэн онд төрсөн бэ?')
birth_day = int(birth_day)
birth_day = 2025 - birth_day
print(f"Та ойролцоогоор:{birth_day} настай юм байна.")
#ex23
input_s_tal = input('Квадратын талын уртыг оруулна уу:')
input_s_tal= int(input_s_tal)
input_s =input_s_tal*2
input_s = int(input_s)
print(f"Талын урт нь{input_s_tal} байх квадратын талбайг ол {input_s} гарна.")
#ex24
input_triangle_tal_a = input('Гурвалжны суурийг оруулна уу:')
input_triangle_tal_b = input('Гурвалжны өндрийг оруулна уу:')
input_triangle_tal_b= float(input_triangle_tal_b)
input_triangle_tal_a= float(input_triangle_tal_a)
input_triangle =input_triangle_tal_a * input_triangle_tal_b
input_triangle = float(input_triangle)
print(f"Энэхүү гурвалжны талбай нь: {input_triangle}")