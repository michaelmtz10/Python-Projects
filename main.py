from tkinter import *
import sqlite3 as db

# code block to create database and table
conn = db.connect('Student_Tracker.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS STUDENTS
    (
        id INTEGER PRIMARY KEY NOT NULL,
        fname TEXT,
        lname TEXT,
        p_number TEXT,
        e_email INTEGER,
        c_course TXT
        )''')
cur.close()
conn.commit()
conn.close()


# method for putting data in db
# get method gets values from variables
def send_to():
    conn = db.connect('Student_Tracker.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO STUDENTS (fname, lname, p_number, e_email, c_course) VALUES('%s', '%s', '%s', '%s', '%s')"%(fname.get(), lname.get(), p_number.get(), e_mail.get(), c_course.get()))
    cur.close()
    conn.commit()
    conn.close()
    status.set('Data Added')
# delete file selected
def delete_from():
    conn = db.connect('Student_Tracker.db')
    cur = conn.cursor()
    cur.execute('''DELETE from STUDENTS WHERE fname = (SELECT MAX(fname) FROM STUDENTS);''')
    cur.close()
    conn.commit()
    status.set('Data Removed')
# creating the gui
window = Tk()
window.title('Student Picker')
window.geometry('500x300')

# assigning variables
fname = StringVar()
lname = StringVar()
p_number = StringVar()
e_mail = StringVar()
c_course = StringVar()
status = StringVar()



# create labels for instructing user
Label(window, text='First Name').grid(row=0, column=0)
Label(window, text='Last Name').grid(row=1, column=0)
Label(window, text='Phone Number').grid(row=2, column=0)
Label(window, text='Email').grid(row=3, column=0)
Label(window, text='Course').grid(row=4, column=0)
Label(window, text='', textvariable=status).grid(row=5, columnspan=2)

# creating entry forms for input

Entry(window, textvariable=fname).grid(row=0, column=1)
Entry(window, textvariable=lname).grid(row=1, column=1)
Entry(window, textvariable=p_number).grid(row=2, column=1)
Entry(window, textvariable=e_mail).grid(row=3, column=1)
Entry(window, textvariable=c_course).grid(row=4, column=1)
# add button for entering data
# while using the grid method

Button(window, text='Submit', command=send_to).grid(row=6, columnspan=2)
Button(window, text='Delete', command=delete_from).grid(row=6, columnspan=1)

mainloop()