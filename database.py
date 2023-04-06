import sqlite3

conn = sqlite3.connect('books.sqlite')

cursor = conn.cursor()
sql_query = """ CREATE TABLE BOOKS 
                (ID integer PRIMARY KEY, AUTHOR text NOT NULL, 
                 TITLE text NOT NULL, PAGES text NOT NULL) """

cursor.execute(sql_query)