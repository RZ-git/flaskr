import sqlite3

DATABASE = 'database.db'


def create_book_table():
    con = sqlite3.connect(DATABASE)
    con.execute("CREATE TABLE IF NOT EXISTS book (title, price, arrival_day)")
    con.close()
