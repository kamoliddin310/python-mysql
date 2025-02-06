from mysql.connector.cursor import MySQLCursor


def create_books_table(cursor: MySQLCursor):
    """Create a 'books' table in the database if it doesn't exist."""
   
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books(
        Id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        author VARCHAR(100) NOT NULL,
        published_year INT NOT NULL,
        gender VARCHAR(100) NOT NULL,
        price DECIMAL(10,2) NOT NULL,
        available BOOLEAN DEFAULT TRUE NOT NULL);
    """)

    
def insert_book(cursor: MySQLCursor, books):
    """Insert a new books into the 'books' table."""
    
    insert = """
       INSERT INTO books (title, author, published_year, gender, price, available)
       VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.executemany(insert, books)


def show_all_books(cursor: MySQLCursor):
    """Retrieve and display all books from the 'books' table."""
    
    cursor.execute("SELECT * FROM books;")
    books = cursor.fetchall()
    for book in books:
        print(book)
