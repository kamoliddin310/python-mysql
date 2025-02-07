from mysql.connector import connect
import kod
from funktion import(
    created_table,
    insert_into,
    update_table,
    delete_from,
    select_from_where
)

s = connect(
        host =       kod.host,
        user =       kod.user,
        password =   kod.password,
        port =       kod.port,
        database =   kod.database
)
cursor = s.cursor()
cursor.execute("TRUNCATE TABLE users;")

created_table(cursor)

    # Ma'lumot qushish
a = [
    ("Ali", 32),
    ("Sherbe", 19),
    ("Olim", 19)
]
insert_into(cursor, a)
s.commit()

    # yoshni yangilash
b = int(input("Foydalanuvchini id raqamini kiriting --> " ))
a = int(input("Foyadalanuvchini yangi yoshini kiriting --> " ))
update_table(cursor, a, b)
print("\n")


    # Uchirish
a = int(input("Uchirmoqchi bulgan insonni id raqamini kiriting --> " ))
delete_from(cursor, a)
print("\n")


    # 25 yoshdan katta bulgan foydalanuvchilarni chiqarish
select_from_where(cursor)


cursor.close()
s.close()