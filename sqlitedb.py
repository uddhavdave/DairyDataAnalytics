import sqlite3
conn= sqlite3.connect('cattle.db')
cur = conn.cursor()
cur.execute(
    #"""CREATE TABLE  cattle (
        #                    name text,
       #                     age integer,
      #                       prod integer,
     #                        birth date )""")

cur.execute)
conn.commit()
conn.close()