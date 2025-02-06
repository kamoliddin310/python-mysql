from mysql.connector import connect
import set
from db import (
    create_books_table,
    insert_book,
    show_all_books,
    search_books_by_author_or_genre,
    update_book_price,
    update_book_availability,
    delete_book,
    sort_books_by_year,
    count_books,
    price_statistics
)

    # MySQL ga bog'lanish
c = connect(
        host =       set.host,
        user =       set.users,
        password =   set.password,
        port =       set.port,
        database =   set.database
    )
cursor = c.cursor()
    # Shu narsani CHATGPT orqali bilib oldim bu kodni yozmasim oldin har gal ma'lumotni qayta qushib ketdi
cursor.execute("TRUNCATE TABLE books;")
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


    # Ma'lum bir shart bo'yicha qidiruv
d = input("'author' yoki 'gender' kiriting --> " ).strip().lower()
r = input("qidirayotgan narsangizning nomini kiriting --> " ).strip()
search_books_by_author_or_genre(cursor, d, r)


    # kitobni narxini yangilash
book_id = int(input("Narxini yangilamoqchi bulgan kitob id raqamini kiriting --> " ))
new_price = float(input("Yangi narxni kiriting floatda bulsa yaxshi --> " ))
update_book_price(cursor, new_price, book_id)


    # Kitob mavjudligini o'zgartirish
a = int(input("mavjudligini uzgartirmoqchi bulgan kitobni id raqamini kiriting --> " ))
b = int(input("availableni 'True = 1', 'False = 0' raqami buyicha uzgartiring --> " ))
update_book_availability(cursor, a, b)


    # Kitobni uchirish
a = int(input("Uchirmoqchi bulgan narsangizni id raqamini kiritng --> " ))
delete_book(cursor, a)


    # Yil bo'yicha saralash
sort = int(input("1- raqam usish taribida, 2- raqam kamayish tartibida --> ")) 
sort_books_by_year(cursor, sort)


    # Jami kitoblar sonini chiqarish
count_books(cursor)


    # Narx bo'yicha statistikani chiqarish
price_statistics(cursor)


cursor.close()
c.close()