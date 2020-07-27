import sqlite3

DROP_TABLE = "DROP TABLE IF EXISTS authors"

CREATE_TABLE='''CREATE TABLE authors
(id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
bio TEXT)'''

INSERT_TABLE='''INSERT INTO authors(id,name,bio)
VALUES(1,'三上延','ビブリア古書堂の事件手帖の新シリーズが、始まった。')
'''

SELECT_TABLE="SELECT * FROM authors"

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

