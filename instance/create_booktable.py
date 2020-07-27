import sqlite3

DROP_TABLE = "DROP TABLE IF EXISTS books"

CREATE_TABLE='''CREATE TABLE books
(id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
author TEXT,
cover TEXT DEFAULT 'book.png')'''

INSERT_TABLE='''INSERT INTO books(id,title,author,cover)
VALUES(1,'ヤン・フスの宗教改革','佐藤優','book.png')
'''

SELECT_TABLE="SELECT * FROM books"

conn = sqlite3.connect('bookdb.sqlite3')
c = conn.cursor()
c.execute(DROP_TABLE)
c.execute(CREATE_TABLE)
c.execute(INSERT_TABLE)
conn.commit()

c.execute(SELECT_TABLE)
result = c.fetchone()
print(result)
conn.close()

