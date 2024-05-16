import sqlite3


def connect():
    connection = sqlite3.connect("courses.db")
    cursor = connection.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS course(id INTEGER PRIMARY KEY, name TEXT, category TEXT,
                   author TEXT, price TEXT)
                   ''')
    connection.commit()
    connection.close()


def create(name, category, author, price):
    connection = sqlite3.connect("courses.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO course VALUES(NULL,?,?,?,?)", (name, category, author, price))
    connection.commit()
    connection.close()


def read_all():
    connection = sqlite3.connect("courses.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM course")
    rows = cursor.fetchall()
    connection.close()
    return rows


def update(id, name, category, author, price):
    connection = sqlite3.connect("courses.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE course SET name=?, category=?, author=?, price=? WHERE id=?",
                   (name, category, author, price, id))
    connection.commit()
    connection.close()


def delete(id, ):
    connection = sqlite3.connect("courses.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM course WHERE id=?", (id,))
    connection.commit()
    connection.close()


def search(name="", category="", author="", price=""):
    connection = sqlite3.connect("courses.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM course WHERE name=? OR category=? or author=? OR price=?")
