import mysql.connector
import settings
from db import (
    create_books_table,
    insert_book,
    show_all_books,
)


if __name__ == "__main__":
    connection = mysql.connector.connect(
        host=settings.host,
        user=settings.user,
        password=settings.password,
        port=settings.port
    )

    cursor = connection.cursor()

    # db dagi functionni ishlating

    # close
    cursor.close()
    connection.close()
