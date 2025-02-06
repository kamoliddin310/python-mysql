from mysql.connector import connect
import kod
from funktion import(
    created_table,
    insert_into,
    insert_into,
    deleate_from,
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
cursor.execute("TRUNCATE TABLE books;")

created_table(cursor)


a = [
    ("Ali", 32),
    ("Sherbe", 19),
    ("Olim", 19)
]
insert_into(cursor, a)
s.commit()