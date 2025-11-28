
try:
    a_numb = int(input("Нэг бүхэл тоог оруулна уу: "))
    if a_numb > 0:
        print("Энэ бол эерэг тоо.")
    elif a_numb < 0:
        print("Энэ бол сөрөг тоо.")
    else:
        print("Энэ бол 0.")
except ValueError:
    print("Тоон утга биш байна!")


#ex02
age_numb = input('Таны насыг оруулна уу:')
age_numb= int(age_numb)
if age_numb>20:
    print("Та насанд хүрсэн байна.")
else :
    print("Та насанд хүрээгүй байна.")

#ex03
password = int(input('Нууц үгээ оруулна уу:'))
if password == "python123":
    print("Нууц үг зөв байна. Нэвтэрлээ.")
else :
    print("Нууц үг буруу байна. Хандах эрхгүй.")

#ex04
code = int(input('Шалгах тоогоо оруулна уу:'))
if code%2==0:
    print("бол тэгш тоо.")
else :
    print("бол сондгой тоо.")

#ex05
score = int(input('Шалгалтын оноогоо оруулна уу:'))
if score >= 0 and score <= 59:
    print("Харамсалтай байна. Та тэнцээгүй.")
elif score >= 60 and score <= 69:
    print("Харамсалтай байна. Та тэнцээгүй.")
elif score >=70 and score <=79:
   print("Баяр хүргэе! Та тэнцсэн байна.")   
elif score >=80 and score <=89:
    print("Баяр хүргэе! Та тэнцсэн байна.")  
elif score >=90 and score <=100:
    print("Баяр хүргэе! Та тэнцсэн байна.")  
elif score<0 :
    pass

#ex06
temp = int(input("Агаарын хэмийг цельсээр оруулна уу: "))
if temp > 0:
    print("Ус хөлдөх цэгээс дээш байна.")
else :
    print("Ус хөлдөх цэгээс доош байна.")

#ex07
word = input("Нэг үг бичнэ үү: ")
if len(word) > 8:
    print("Энэ бол урт үг юм байна.")
else :
    print("Энэ бол богино үг юм байна.")

#ex08

try:
    num = int(input('Нэг тоо оруулна уу:'))
    if num > 0:
        print("Энэ бол эерэг тоо.")
    elif num < 0:
        print("Энэ бол сөрөг тоо.")
    else:
        print("Энэ бол 0.")
except ValueError:
    print("Тоон утга биш байна!")

#ex09

score = int(input('Шалгалтын оноогоо оруулна уу:'))
if score >= 0 and score <= 59:
    print("Харамсалтай байна.F Та тэнцээгүй байна.")
elif score >= 60 and score <= 69:
    print("Харамсалтай байна. D үнэлгээ авсан байна.")
elif score >=70 and score <=79:
   print("Баяр хүргэе! Та С үнэлгээ авсан байна.")   
elif score >=80 and score <=89:
    print("Баяр хүргэе! Та Б үнэлгээ авсан  байна.")  
elif score >=90 and score <=100:
    print("Баяр хүргэе! Та A үнэлгээ авсан байна.")  
elif score<0 :
    pass

#ex10

week = (input('Долоо хоногийн гаригийг оруулна уу:'))
weekend={"Бямба","Ням"}
if week== weekend:
    print("Ажлын өдөр.")
else :
    print("Амралтын өдөр.")

#ex11
username = input('Нэвтрэх нэр оруулна уу:')
if username ==  "admin":
    password = (input('Нууц үгээ оруулна уу:'))
    if password == "python123":
        print("Нууц үг зөв байна. Нэвтэрлээ.")
    else :
        print("Нууц үг буруу байна. Хандах эрхгүй.")
else :
    print("хандах эрхгүй")

#ex12
egshigt=("А","Э","И","О","У","Ө","Ү")

giiguulegch=("Б","В","Г","Д", "Ж", "З","Й", "К", "Л", "М", "Н","Ң","П","Р","С","Т","Ф", "Х", "Ц", "Ч", "Ш")

#ex13