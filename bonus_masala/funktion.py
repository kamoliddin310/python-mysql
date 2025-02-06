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
    a = """
        INSERT INTO users (name, age)
        VALUES(%s, %s)
    """
    cursor.executemany(a, users)


def update_table(cursor: MySQLCursor):
    pass
def deleate_from(cursor: MySQLCursor):
    pass
def select_from_where(cursor: MySQLCursor):
    pass