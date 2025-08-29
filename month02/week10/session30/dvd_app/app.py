import psycopg2

def connect():
    return psycopg2.connect(
        dbname = "dvdrentle",
        user= "postgres",
        password= "",
        host= "localhost",
        port= "5432"
        )

def show_table(table_name ):
    conn= connect()
    cur = conn.cursor()
    try:
        # TODO table_name ашиглан тухайн хүснэгтийн эхний 5 мөрийг
        # харуулах код бичнэ үү
        cur.execute(f"SELECT * FROM {table_name} LIMIT 5;")
        print(f"\n===={table_name.upper()} хүснэгт (эхний 5 мөр)====")
        rows = cur.fetchall()
    
        for row in rows:
            print(row)
    except Exception as e:
        print("⚠Алдаа:", e)

    finally:
        cur.close()
        conn.close()
        return None

def insert_actor():
    conn = connect()
    cur = conn.cursor()
    try:
        first = input("(first_name):")
        last = input("(last_name):")
    
        sql_insert = "INSERT INTO actor (first_name,last_name) VALUES(%s,%s)"

        cur.execute(sql_insert,(first,last))
        conn.commit()
        print(f"'{first}{last}'✅ Жүжигчинг амжилттай нэмлээ!")
        cur.close()
    except Exception as e:
        print("⚠Алдаа:",e)
    finally:
        
        conn.close()
def main_menu():
    while True:
        print("\n=== DVD Rental App ===")
        print("1. Actor хүснэгт харуулах")
        print("2. Film хүснэгт харуулах")
        print("3. Customer хүснэгт харуулах")
        print("4. Actor хүснэгтэд шинэ өгөгдөл нэмэх")
        print("0. Гарах")

        choice = input("Сонголтоо оруулна уу: ")
        if choice == "1":
            show_table("actor")
        elif choice == "2":
            show_table("film")
        elif choice == "3":
            show_table("customer")
        elif choice == "4":
            insert_actor()
        elif choice == "0":
            print("👋 Програм дууслаа.")
            break
        else:
            print("⚠Буруу сонголт, дахин оролдоно уу.")

if __name__=="__main__":
    main_menu()
