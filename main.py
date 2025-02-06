from mysql.connector import connect
import set
from db import create_books_table, insert_book, show_all_books

    # MySQL ga bog'lanish
c = connect(
        host =       set.host,
        user =       set.users,
        password =   set.password,
        port =       set.port,
        database =   set.database
    )
cursor = c.cursor()
    # Table yaratish funkiyasi
create_books_table(cursor)


    # kitob qushish
b = [
    ("Atomic Habits", "James Clear", 2018, "Self-help", 15.99, True),
    ("Deep Work", "Cal Newport", 2016, "Productivity", 12.50, True),
    ("Python Crash Course", "Eric Matthes", 2019, "Programming", 22.95, True)
]
insert_book(cursor, b)
    # tableni ma'lumotlarini saqlash uchun keral
c.commit() 


# jadvalni chiqarish
show_all_books(cursor)
    # close
cursor.close()
c.close()
