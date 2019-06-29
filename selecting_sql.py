import sqlite3
conn = sqlite3.connect("my_friends.db")
c = conn.cursor()
c.execute("SELECT * FROM friends")
for res in c:
    print(res)
# for printing the result in a list type:
# print(c.fetchall())
# fetch a single result type:
# print(c.fetchone())
conn.commit()
conn.close()