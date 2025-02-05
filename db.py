from mysql.connector.cursor import MySQLCursor


def create_books_table(cursor: MySQLCursor):
    """
    Create a 'books' table in the database if it doesn't exist.
    """
    
def insert_book(cursor: MySQLCursor, title, author, published_year, genre, price, available):
    """
    Insert a new book into the 'books' table.
    """

def show_all_books(cursor: MySQLCursor):
    """
    Retrieve and display all books from the 'books' table.
    """
