import psycopg2
from psycopg2 import OperationalError
def connect_db():
    """PostgreSQL мэдээллийн сантай холбогдох функц"""
    try:
        # Мэдээллийн сангийн холболтын мэдээллийг өөрийнхөөрөө солино уу
        conn = psycopg2.connect(
            dbname="student_db",
            user='postgres',
            password="",
            host="localhost",
            port="5432"
        


        ) # TODO холболтын мэдээллийг оруулна уу
        return conn
    except OperationalError as e:
        print(f"Холболтын алдаа гарлаа: {e}")
        return None
def add_student(conn):
    """Шинэ оюутан нэмэх функц"""
    try:
        ovog_ner = input("Оюутны овог нэрийг оруулна уу: ")
        email = input("И-мэйл хаягийг оруулна уу: ")
        utas = input("Утасны дугаарыг оруулна уу: ")
        # Курсор үүсгэх
        cur = conn.cursor()
        # SQL INSERT тушаал
        query ="INSERT INTO students (ovog_ner,email,utas ) VALUES(%s,%s,%s)"
        # TODO оюутан нэмэх sql бичнэ үү.
        # Тушаалыг гүйцэтгэх
        cur.execute(query, (ovog_ner, email, utas))
        # Өөрчлөлтийг мэдээллийн санд хадгалах
        conn.commit()
        print(f"'{ovog_ner}' амжилттай бүртгэгдлээ.")
        # Курсорыг хаах
        cur.close()
    except Exception as e:
        print(f"Оюутан нэмэхэд алдаа гарлаа: {e}")
        conn.rollback() # Алдаа гарвал өөрчлөлтийг буцаах
def view_students(conn):
    """Бүх оюутны мэдээллийг харах функц"""
    try:
        cur = conn.cursor()

        cur.execute("SELECT id, ovog_ner,email,utas FROM students")
        # TODO бүх оюутны мэдээллийг авах sql бичнэ үү.
        rows = cur.fetchall()
        if not rows:
            print("Бүртгэлтэй оюутан байхгүй байна.")
            return
        print("\n--- Бүртгэлтэй оюутнууд ---")
        # Хүснэгтийн толгой хэсгийг хэвлэх
        print(f"{'ID':<5} {'Овог нэр':<25} {'И-мэйл':<30} {'Утас':<15}")
        print("-" * 75)
        # Мөр бүрийг давталтаар хэвлэх
        for row in rows:
            print(f"{row[0]:<5} {row[1]:<25} {row[2]:<30} {row[3]:<15}")
        print("-" * 75)
        cur.close()
    except Exception as e:
        print(f"Мэдээлэл харахад алдаа гарлаа: {e}")

def main():
    """Програмын үндсэн цэс"""
    conn = connect_db()
    if conn is None:
        return # Холбогдож чадаагүй бол програмаас гарах
    
    while True:
        print("\n===== Оюутны Бүртгэлийн Систем =====")
        print("1. Шинэ оюутан нэмэх")
        print("2. Бүх оюутныг харах")
        print("3. Гарах")

        choice = input("Сонголтоо оруулна уу (1-3): ")
        
        if choice == '1':
            add_student(conn)
            # TODO шинэ оюутан нэмэх функцыг дуудна уу
        elif choice == '2':
            view_students(conn)
            # TODO бүх оюутны мэдээллийг харах функцыг дуудна уу
        elif choice == '3':
            print("Програмаас гарлаа.")
            break
        else:
            print("Буруу сонголт. 1-3 хооронд сонгоно уу.")

    if conn:
        conn.close()

if __name__ == "__main__":
    main()