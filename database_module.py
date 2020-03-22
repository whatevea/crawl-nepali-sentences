import sqlite3

def create_me():
	conn=sqlite3.connect("flask_db.db")
	c=conn.cursor()
	c.execute("CREATE TABLE table2 (names text,age integer)")
	conn.commit()
def insert(name,age):
	conn=sqlite3.connect("flask_db.db")
	c=conn.cursor()
	c.execute(f"INSERT INTO table2 VALUES('{name}',{age})")
	conn.commit()

