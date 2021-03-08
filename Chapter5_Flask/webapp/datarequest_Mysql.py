import mysql.connector

dbconfig = {'host': '127.0.0.1',
            'user': 'root',
            'password': 'root',
            'database': 'datarequestDB'}

conn = mysql.connector.connect(**dbconfig)

cursor = conn.cursor()

#_SQL = """describe log"""

_SQL = """Insert into log
         (phrase, letters, ip, browser_sring, results) 
         values 
         (%s, %s, %s, %s, %s)"""
  #I mispelled "string" in browser_string, when making the log in sql. Couldn't
    #figure out how to change the log though, so kept mispelling here.
       
cursor.execute(_SQL, ('hitch-hiker', 'xyz', '127.0.0.1', 'Opera', "set{'x', 'y'}"))

conn.commit()

_SQL = """select * from log"""

cursor.execute(_SQL)

for row in cursor.fetchall():
    print(row)
    
cursor.close()

conn.close()



