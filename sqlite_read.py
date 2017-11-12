import sqlite3

conn = sqlite3.connect('orders.db')
cur = conn.cursor()

cur.execute("SELECT * FROM users;")
one_result = cur.fetchall()
print(one_result)

cur.execute("DELETE FROM users WHERE lname='Parker' ;")
conn.commit()

cur.execute("SELECT * FROM users;")
one_result1 = cur.fetchall()
print(one_result1)

cur.execute("""
SELECT *, users.fname, users.lname FROM orders 
LEFT JOIN users ON users.userid=orders.userid;
""")

print(cur.fetchall())
