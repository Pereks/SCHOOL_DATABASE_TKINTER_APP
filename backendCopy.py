import sqlite3
from datetime import datetime

def connect():
    connection = sqlite3.connect("courses1.db")
    cursor = connection.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS course(id INTEGER PRIMARY KEY, name TEXT, category TEXT,
                   author TEXT, price TEXT, created_date TEXT)
                   ''')
    connection.commit()
    connection.close()

def create(name, category, author, price):
    try:
        connection = sqlite3.connect("courses1.db")
        cursor = connection.cursor()
        created_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO course VALUES(NULL,?,?,?,?,?)", (name, category, author, price, created_date))
        connection.commit()
        connection.close()
    except sqlite3.Error as e:
        print("Error:", e)


def read_all():
    connection = sqlite3.connect("courses1.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM course")
    rows = cursor.fetchall()
    connection.close()
    return rows


def update(id, name, category, author, price):
    try:
        connection = sqlite3.connect("courses1.db")
        cursor = connection.cursor()
        cursor.execute("UPDATE course SET name=?, category=?, author=?, price=? WHERE id=?",
                       (name, category, author, price, id))
        connection.commit()
    except sqlite3.Error as e:
        print("Error updating course:", e)
    finally:
        connection.close()

def delete(id):
    try:
        connection = sqlite3.connect("courses1.db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM course WHERE id=?", (id,))
        connection.commit()
    except sqlite3.Error as e:
        print("Error deleting course:", e)
    finally:
        connection.close()
