from mysql.connector.cursor import MySQLCursor

def created_table(cursor: MySQLCursor):
    cursor.execute("USE kutubxona;")
    cursor.execute( """
        CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        age INT NOT NULL);
    """)


def insert_into(cursor: MySQLCursor, users):
    a = "INSERT INTO users (name, age) VALUES(%s, %s)"
    cursor.executemany(a, users)
    print("Jadval yaratildi ")


def update_table(cursor: MySQLCursor, users_id, users_age):
    a = """
        UPDATE users
        SET age = %s
        WHERE id = %s;
    """
    cursor.execute(a, (users_id, users_age))
    cursor._connection.commit()
    if cursor.rowcount > 0:
        print(f"{users_age} - idning yoshi {users_id} ga uzgartirildi :)")
    else:
        print("bunaqa id yuq :(")


def delete_from(cursor: MySQLCursor, id):
    a = "DELETE FROM users WHERE id = %s"
    cursor.execute(a, (id,))
    cursor._connection.commit()
    if cursor.rowcount > 0:
        print(f"{id} - Uchirildi :)")
    else:
        print("Bunaqa id yuq : (")


def select_from_where(cursor: MySQLCursor):
    
    cursor.execute("SELECT * FROM users WHERE age > 25")
    users = cursor.fetchall()
    for user in users:
        print(user)
