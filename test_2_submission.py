import sqlite3

conn = sqlite3.connect('test2.db')
# creating a table within the db 'test2' with an ID col, and file name col
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXIST tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file_name)")
    conn.commit()
conn.close()
# connectin to the data base
conn = sqlite3.connect('test2.db')
# adding data into the table
with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_files(col_file_name) VALUES (?)", \
                ('Hello.txt'))
    
    cur.execute("INSERT INTO tbl_files(col_file_name) VALUES (?)", \
                ('World.txt'))
    conn.commit()
conn.close()

conn = sqlite3.connect('test2.db')
#creating a statement by fetching picked data from the table
with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_file_name FROM tbl_files WHERE col_file_name = 'Hello,txt'")
    varfile = cur.fetchall()
    for file in varfile:
        msg = "File name: ()".format(item[0])
    print(msg)
    
