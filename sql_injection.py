import sqlite3
conn = sqlite3.connect("users.db")

u = input("please enter your username....")
p = input("please enter your password...")
query =f"SELECT *FROM users WHERE username='{u}' AND password = '{p}'"

c =conn.curor()
c.execute(query)

res = c.fetchone()
if (res):
    print("WELCOME BACK")
else:
    print("FAILED LOGIN")
conn.commit()
conn.close()
