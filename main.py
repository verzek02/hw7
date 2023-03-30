import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = False
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error as e:
        print(e)

def create_student(conn, student):
    sql = '''INSERT INTO student(fullname, mark, hobby, is_married)
    VALUES(?,?,?,?)
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, student)
        conn.commit()
    except Error as e:
        print(e)

def read_student(conn):
    try:
        sql = '''SELECT * FROM student'''
        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()
        for i in row:
            print(i)
    except Error as e:
        print(e)

def update_student(conn):
    sql = '''UPDATE student SET fullname = 'genius' WHERE mark > 10.0'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    except Error as e:
        print(e)
def delete_student(conn):
    sql = '''DELETE FROM student WHERE mark < 5.0'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    except Error as e:
        print(e)

def clear_table(conn):
    sql = '''DELETE FROM student'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    except Error as e:
        print(e)


database = "user2.db"

sql_create_table = """
CREATE TABLE student(
id INTEGER PRIMARY KEY AUTOINCREMENT, 
fullname VARCHAR(50) NOT NULL,
mark DOUBLE (5,2) NOT NULL DEFAULT 0.0,
hobby TEXT DEFAULT NULL,
is_married BOOLEAN DEFAULT FALSE
);
"""

connection = create_connection(database)

if connection is not None:
    print('All correct')
    create_table(connection, sql_create_table)
    create_student(connection, ('Nazira', 10.0, 'reading', True))
    create_student(connection, ('Mirlan', 10.0, 'football', False))
    create_student(connection, ('Bektur', 9.0, 'driving', True))
    create_student(connection, ('Baimurat', 0.0, 'none', False))
    read_student(connection)
    delete_student(connection)
    update_student(connection)