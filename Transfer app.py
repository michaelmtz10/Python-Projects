import time
from tkinter import *
from tkinter import filedialog
import shutil
import datetime as datetime
import os

app = Tk()
app.title('File Transfer')
app.geometry('350x150')

# assigning variable
# transfers selected file into selected folder
def transfer():
    # make comparison per folder
    # listing files in folder, and saving onto variable filelist
    filelist = os.listdir(foldname)
    # iterates through list of files
    for file in filelist:
        # creates variable that holds entire path including filename
        full_path = foldname + '/' + file
        # gets mod time in mtime format
        mtime = os.path.getmtime(full_path)
        # converts m time to datetime format
        mod_time = datetime.datetime.fromtimestamp(mtime)
        # makes variable that holds the time 24 hours ago
        twenty_four = datetime.datetime.now() - datetime.timedelta(hours=24)
        # if mod_time was more recent than twenty four hours ago move file to dname.
        if mod_time > twenty_four:
            shutil.move(full_path, d_name)


# open file explore and allows user to select file
def getfile():
    global foldname
    foldname = filedialog.askdirectory()
    find_file.insert(END, foldname)
# allows user to select folder
def dest_file():
    global d_name
    d_name = filedialog.askdirectory()
    destiny_file.insert(END, d_name)

 
# creating buttons
# searches file explorer for desired folder
search_btn = Button(app, text='Search', command=getfile, width=10)
search_btn.grid(row=1, column=1, padx=10, pady=10)
# opens file explorer to get folder destination
send_btn = Button(app, text='Send to', width=10, command=transfer)
send_btn.grid(row=2, column=1, pady=5, padx=10)
# transfers selected files to folder
transfer_btn = Button(app, text='Transfer', command=dest_file, width=10)
transfer_btn.grid(row=3, column=1, padx=5, pady=10)
#
# creating entry fields
find_file = Entry(app)
find_file.grid(row=1, column=2)
# created entry field
destiny_file = Entry(app)
destiny_file.grid(row=3, column=2)
#
# create label to inform user
guide = Label(app, text='Click to transfer selected files')
guide.grid(row=2, column=2)
app.mainloop()

