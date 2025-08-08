import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        print(f"{db_file}database connected")
        return connection
    
    except Error as e:
        print(e)
    return connection

def create_table(connection):
    create_contact_table_sql="""
    CREATE TABLE IF NOT EXISTS contacts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE

    )
    """
    with connection:
        connection.execute(create_contact_table_sql)


def add_contacts(connection, contact_name, contact_email):
# TODO
    add_contact_sql="""
        INSERT INTO contacts (name,email)
        VALUES(?,?);
    
    """
    with connection:
        connection.execute(add_contact_sql,(contact_name,contact_email))

def view_contacts(connection):
    view_contacts_sql="""
        SELECT * FROM contacts;
    """
    with connection:
        cursor = connection.execute(view_contacts_sql)
        entries = [{"ID":row[0],"Name":row[1],"Email":row[2]} for row in cursor.fetchall()]
        print(entries)
def update_contact_email(connection, contact_name, new_email):

    update_contact_by_name ="""
        UPDATE contacts
        SET email= ?
        WHERE name =?
    """
    with connection:
        connection.execute(update_contact_by_name,(new_email,contact_name))

def delete_contacts(connection,contact_name):

    delete_contact_sql ="""
        DELETE FROM contacts WHERE name=?
    """
    with connection:
        connection.execute(delete_contact_sql,(contact_name,))
    

def main():
    """ Main function to run the database operations """

    database = "contacts.db"
    # Create a database connection
    conn = create_connection(database)
    if conn is not None:
    # Create the contacts table
        create_table(conn)
        # --- C: CREATE ---
        print("\n>>> Adding initial contacts...")
        add_contacts(conn, "Alice", "alice@example.com")
        add_contacts(conn, "Bob", "bob@example.com")
        add_contacts(conn, "Charlie", "charlie@example.com")
        # --- R: READ ---
        view_contacts(conn)
        # --- U: UPDATE ---
        print(">>> Updating Bob's email...")
        update_contact_email(conn, "Bob", "bob_new@example.com")
        # View contacts again to see the update
        view_contacts(conn)
        # --- D: DELETE ---
        print(">>> Deleting Charlie...")
        delete_contacts(conn, "Charlie")
        # View the final list of contacts
        view_contacts(conn)
        # Close the connection
        conn.close()
        print("\nDatabase connection closed.")
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()