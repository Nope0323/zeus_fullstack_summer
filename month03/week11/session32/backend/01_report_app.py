# report_app.py
import psycopg2
from psycopg2 import OperationalError

def connect_db():
    """PostgreSQL мэдээллийн сантай холбогдох функц"""
    try:
        #-- Холболтын мэдээллийг өөрийн тохиргоогоор солих
        conn = psycopg2.connect(
            dbname = "students_db",
            user= "postgres",
            password= "",
            host= "localhost",
            port= "5432"
        )
        return conn
    except OperationalError as e:
        print(f"Холболтын алдаа гарлаа: {e}")
        return None

def setup_database(conn):
        """Програмыг анх ажиллуулахад шаардлагатай хүснэгтүүдийг үүсгэж,
        анхдагч мэдээллийг оруулах функц."""
        try:
            cur = conn.cursor()
#------------------------------------------------------------------------------------------------------------
            # TODO
            # courses (хичээлүүд) хүснэгтийг үүсгэх курсорыг ажиллуулна уу.
            # id багана нь PRIMARY KEY бас давтахгүй байх,
            # course_name багана нь UNIQUE байх, NOT NULL байх ёстой.
            cur.execute("""
                CREATE TABLE IF NOT EXISTS courses (
                id SERIAL PRIMARY KEY,
                course_name VARCHAR(100) UNIQUE NOT NULL);
                        """)
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
            # TODO
            # students (оюутнууд) хүснэгтийг үүсгэх
            # id багана нь PRIMARY KEY бас давтахгүй байх,
            # ovog_ner багана нь NOT NULL байх,
            # email багана нь UNIQUE байх,
            # grade багана нь 0-100 хооронд байх шалгалттай,
            # жишээ нь: grade INTEGER CHECK (grade >= 0 AND grade <= 100) гэжүүсгэнэ.
            # course_id багана нь courses хүснэгтийн id-г заах гадаад түлхүүр байх.
            cur.execute("""
                CREATE TABLE IF NOT EXIXSTS students(id SERIAL PRIMARY KEY, 
                        ovog_ner VARCHAR(100) NOT NULL,
                        email VARCHAR(100) UNIQUE, 
                        grade INTEGER CHECK (grade >= 0 AND grade <= 100), 
                        students VARCHAR(100) UNIQUE NOT NULL );
            """)
#------------------------------------------------------------------------------------------------------------
            # Анхдагч хичээлүүдийг нэмэх (хэрэв байхгүй бол)
            cur.execute("""INSERT INTO courses (course_name)
            VALUES
            ('Програмчлалын үндэс'),
            ('Веб хөгжүүлэлт'),
            ('Өгөгдлийн сан') ON CONFLICT (course_name) DO NOTHING;
            """)
            conn.commit()
            cur.close()
            print("Мэдээллийн сангийн бүтэц амжилттай бэлтгэгдлээ.")
        except Exception as e:
            print(f"Мэдээллийн сан бэлтгэхэд алдаа гарлаа: {e}")
            conn.rollback()

def view_courses(conn):
            """Боломжит хичээлүүдийг харуулах функц"""
    try:
        pass
        cur = conn.cursor()
#------------------------------------------------------------------------------------------------------------
            # TODO
            # курсор ашиглан бүх хичээлийн ID болон нэрийг авах SQL-гажиллуулна уу
        cur = 
#------------------------------------------------------------------------------------------------------------
        print("\n--- Боломжит хичээлүүд ---")
        for course in courses:
            print(f"[{course[0]}] {course[1]}")
        print("-" * 28)
        cur.close()
        return courses
    except Exception as e:
        print(f"Хичээл харахад алдаа гарлаа: {e}")
        return []

def add_student(conn):
    """Шинэ оюутныг дүн, хичээлийн хамт бүртгэх"""
    courses = view_courses(conn)
    if not courses:
        print("Бүртгэлтэй хичээл алга байна.")
        return
    try:
        ovog_ner = input("Оюутны овог нэрийг оруулна уу: ")
        email = input("И-мэйл хаягийг оруулна уу: ")
        
        grade = -1
        while not (0 <= grade <= 100):
            try:
                grade = int(input("Дүнг оруулна уу (0-100): "))
            except ValueError:
                    print("Зөвхөн тоон утга оруулна уу.")
        course_id_str = ""
        valid_ids = [str(c[0]) for c in courses]
        while course_id_str not in valid_ids:
            course_id_str = input("Дээрх жагсаалтаас хичээлийн ID-г сонгоно уу: ")
        
            cur = conn.cursor()
        
            query = """
            # TODO
            # query-д холбогдох утгуудыг оруулж, курсорыг ашиглан
            # SQL-г ажиллуулах query үүсгэнэ.
            # ovog_ner, email, grade, course_id-г ашиглан query-г датагаа
            # нэмдэг болгоно уу.
            """
            cur.execute(query, (ovog_ner, email, grade, int(course_id_str)))
            conn.commit()

            print(f"'{ovog_ner}' амжилттай бүртгэгдлээ.")
            cur.close()
    except Exception as e:
            print(f"Оюутан нэмэхэд алдаа гарлаа: {e}")
            conn.rollback()

def show_course_statistics(conn):
            """Хичээл тус бүрийн статистикийг SQL нэгтгэх функц ашиглан
            харуулах"""
    try:
        cur = conn.cursor()
        query = """
        # TODO
        # Хичээл тус бүрийн нэр, оюутны тоо, дундаж дүн, их дүн, бага дүнг
        # харуулах SQL query-г бичнэ үү. (SELECT, JOIN, GROUP BY,COUNT, AVG, MAX, MIN ашиглана)
        """
        cur.execute(query)
        rows = cur.fetchall()
        if not rows:
            print("Статистик гаргах мэдээлэл олдсонгүй.")
            return
        print("\n--- Хичээлүүдийн Дүнгийн Нэгдсэн Тайлан ---")
        print(f"{'Хичээлийн нэр':<25} {'Оюутны тоо':<15} {'Дундаж дүн':
        <15} {'Их дүн':<10} {'Бага дүн':<10}")
        print("-" * 85)
        
        for row in rows:
        # Хэрэв хичээлд оюутан байхгүй бол (LEFT JOIN-оос болж) утгуудыг 0 гэж харуулах
            student_count = row[1]
            avg_grade = row[2] if student_count > 0 else 0
            max_grade = row[3] if student_count > 0 else 0
            min_grade = row[4] if student_count > 0 else 0
            print(f"{row[0]:<25} {student_count:<15} {avg_grade:<15.2f}
            {max_grade:<10} {min_grade:<10}")
            print("-" * 85)
            cur.close()
            except Exception as e:
            print(f"Статистик харахад алдаа гарлаа: {e}")
def main():
    """Програмын үндсэн удирдлага, цэс"""
    conn = connect_db()
    if conn is None:
        return
        # Програмыг эхлүүлэхэд мэдээллийн санг бэлтгэх
        setup_database(conn)    
    while True:
        print("\n===== Оюутны Дүнгийн Систем =====")
        print("1. Шинэ оюутан бүртгэх")
        print("2. Хичээлийн дүнгийн тайлан харах")
        print("3. Гарах")
        choice = input("Сонголтоо оруулна уу (1-3): ")
        if choice == '1':
        # Шинэ оюутан нэмэх функцийг дуудах
        elif choice == '2':
        # Хичээлийн статистикийг харуулах функцийг дуудах
        elif choice == '3':
        print("Програмаас гарлаа.")
        break
        else:
        print("Буруу сонголт. 1-3 хооронд сонгоно уу.")
        if conn:
        conn.close()
    if __name__ == "__main__":
        main()