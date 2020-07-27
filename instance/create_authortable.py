import sqlite3

DROP_TABLE = "DROP TABLE IF EXISTS authors"

CREATE_TABLE='''CREATE TABLE authors
(id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
bio TEXT)'''

INSERT_TABLE='''INSERT INTO authors(id,name,bio)
VALUES(1,'ニーチェ','この人を見よ、ツァラトゥストゥラ、善悪の彼岸、等多数の著書を残した。超人、神は死んだ、永遠回帰の思想')
'''

SELECT_TABLE="SELECT * FROM authors"

conn = sqlite3.connect('bookdb.sqlite3')
c = conn.cursor()
c.execute(DROP_TABLE)
c.execute(CREATE_TABLE)
c.execute(INSERT_TABLE)
conn.commit()

c.execute(SELECT_TABLE)
result = c.fetchall()
print(result)
