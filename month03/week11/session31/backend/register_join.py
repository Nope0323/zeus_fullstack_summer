import psycopg2
from psycopg2 import OperationalError

def connect_db():
    # PostgreSQL мэдээллийн сантай холбогдох функц
    try:
        conn = psycopg2.connect(

#------------------------------------------------------------------------------------------------------------
	    # TODO
        # host, database, user, password утгуудыг өөрийн тохиргоондоо тааруулна
        dbname = "student_db",
        user= "postgres",
        password= "",
        host= "localhost",
        port= "5432"
        )
#------------------------------------------------------------------------------------------------------------

        return conn
    except OperationalError as e:
        print(f"Холболтын алдаа гарлаа: {e}")
        return None

def view_courses(conn):
    # Боломжит хичээлүүдийг харуулах функц
    try:
        cur = conn.cursor()
#------------------------------------------------------------------------------------------------------------

    # TODO
    # courses хүснэгтээс бүх хичээлийн id болон нэрийг авах SQL query бичнэ үү
        cur.execute(f"SELECT id, course_name FROM courses")
        courses = cur.fetchall() #courses хувьсагч зарлаж cur ээр дамжуулж sql - ээс утгуудыг courses д оноож байнав  
        print("\n--- Боломжит хичээлүүд ---")
#------------------------------------------------------------------------------------------------------------

        for course in courses: # courses vs code - дээр үүсгэж байгаа хувьсагч юм
            print(f".[{course[0]}]{course[1]}")
            #яагаад гэдгийг мэдэхгүйч {courses[]}эхний хаал courses ийх бол дотрох нь list төрлөөр орж ирж байна.
        print("-"*28)#хархад зориулсан хязгаалалт
        cur.close()
        return courses
    except Exception as e:
        print(f"Хичээл харахад алдаа гарлаа: {e}")
        return[]# хоосон утга буцааж буй үйлдэл
    
def add_student(conn):
    courses = view_courses(conn)
    if not courses:
        print("Нэмэх боломжтой хичээл олдсонгүй. Эхлээд хичээл нэмнэ үү.")
        return
    try:
        ovog_ner = input("Оюутны овог нэрийг оруулна уу: ")
        email = input("И-мэйл хаягийг оруулна уу: ")
        utas = input("Утасны дугаарыг оруулна уу: ")

        while True:
            course_id = input("Хичээлийн ID-ийг сонгоно уу:")
            if course_id.isdigit() and any(int(course_id) == c[0] for c in courses):
            #isdigit хэрэв ямар нэг тоо байвал буцаана
                break
            else:
                print("Буруу ID байна. Дээрх жагсаалтаас сонгоно уу.")
        cur = conn.cursor()
        
#------------------------------------------------------------------------------------------------------------
	# TODO
        # students хүснэгтэд шинэ оюутны мэдээллийг оруулах SQL query бичнэ үү
        sql_insert = "INSERT INTO actor (ovog_ner,email, utas) VALUES(%s,%s,%s)"
        cur.execute(sql_insert,(ovog_ner,email, utas))
        conn.commit()
#------------------------------------------------------------------------------------------------------------
     
        print(f"'{ovog_ner}' амжилттай бүртгэгдлээ.")
        cur.close()
    except Exception as e:
        print(f"Оюутан нэмэхэд алдаа гарлаа: {e}")
        conn.rollback()

def view_students_with_courses(conn):
# Бүх оюутныг хичээлийнх нь нэртэй хамт харах (JOIN ашиглан)
    try:
        cur = conn.cursor()
    
#------------------------------------------------------------------------------------------------------------
  # TODO
        # students болон courses хүснэгтүүдийг LEFT JOIN ашиглан холбож,
        # оюутны id, овог_нер, email, course_name-г авах SQL query бичнэ үү
        sql_insert01 = "SELECT s.ovog_ner, s.email, s.utas, c.course_name FROM students s LEFT JOIN courses c ON s.course_id = c.id order by s.id"
        cur.execute(sql_insert01)
        rows = cur.fetchall()
        if not rows:
            print("Бүртгэлтэй оюутан байхгүй байна.")
            return
#------------------------------------------------------------------------------------------------------------
        print("\n--- Оюутнууд ба Тэдний Хичээлүүд ---")
        print(f"{'ID':<5} {'Овог нэр':<25} {'И-мэйл':<30} {'Хичээл':<30}")
        print("-" * 95)
        for row in rows:
             course_name = row[3] if row[3] else "Тодорхойгүй"
             print(f"{row[0]:<5} {row[1]:<25} {row[2]:<30} {course_name:<30}")
             print("-" * 95)
             cur.close()
    except Exception as e:
        print(f"Мэдээлэл харахад алдаа гарлаа: {e}")
        
def main():
            # Програмын үндсэн цэс
    conn = connect_db()
    if conn is None:
        return
    while True:
        print("\n===== Оюутан & Хичээлийн Бүртгэлийн Систем =====")
        print("1. Шинэ оюутан нэмэх")
        print("2. Оюутнуудыг хичээлтэй нь харах")
        print("3. Гарах")
        choice = input("Сонголтоо оруулна уу (1-3): ")
        if choice == '1':
#------------------------------------------------------------------------------------------------------------
            # TODO
            # оюутан нэмэх үйлдлийг гүйцэтгэнэ үү
            add_student(conn)
#------------------------------------------------------------------------------------------------------------
            
        elif choice == '2':
#------------------------------------------------------------------------------------------------------------
            # TODO
            # оюутнуудыг хичээлтэй нь харах үйлдлийг гүйцэтгэнэ үү
            view_students_with_courses(conn)
#------------------------------------------------------------------------------------------------------------
        
        elif choice == '3':
            print("👋 Програмаас гарлаа.")
            break
        else:
            print("Буруу сонголт. 1-3 хооронд сонгоно уу.")
    if conn:
        conn.close()


if __name__ == "__main__":
    main()