import sqlite3
import csv
con = sqlite3.connect("data.db")
cur = con.cursor()
#cur.execute("create table data( s_mt text ,s_mr text, s_mre text ,s_price real ,)")
#con.close()
#print("Table created")

a_file = open("model.csv")
rows = csv.reader(a_file)
cur.executemany("INSERT INTO data VALUES (?, ?, ?, ?)", rows)

cur.execute("SELECT * FROM data")
print(cur.fetchall())

con.commit()
con.close()