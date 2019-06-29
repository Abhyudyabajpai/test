import sqlite3
conn = sqlite3.connect("my_friends.db")
c = conn.cursor()
# c.execute("CREATE TABLE friends(first_name TEXT,last_name TEXT ,closeness INTEGER);")
insert_query ='''INSERT INTO friends
                    VALUES ('Anre','Lee',6)'''

c.execute(insert_query)
conn.commit()
conn.close()