from tkinter import *
from tkinter import filedialog
import schedule
import os
import time
from datetime import datetime
import shutil
# first we create gui

transfer = Tk()
transfer.title('File Upload')
transfer.geometry('200x150')

# creating functions
def get_folder():
    newpath = 'C:/Users/mmtz1/Desktop/folder_b'
    newpath = os.path.realpath(newpath)
    os.startfile(newpath)
def fileopen():
    transfer.withdraw()  # prevents an empty tkinter window from appearing
    opener = filedialog.askopenfilename()

# get file directory
def automate():
    # create 24 hour from current moment variable
    today = datetime.datetime.today()
    yesterday = today - datetime.timedelta(days=1)
    # chose directory to grab files from
    path = 'C:/Users/mmtz1/Desktop/folder_a'
    directory = filter(os.path.isfile, glob.glob(path + '*'))
    # got file date date from files
    filedate = time.strftime('%M/%D/%Y', time.gmtime(os.path.getmtime(file)))
    # created condition if file is younger than 24 hours send to directory b
    for file in directory:
        # create 24 hour restriction
        if filedate < yesterday:
            sender = 'C:/Users/mmtz1/Desktop/folder_a'
            receiver = 'C:/Users/mmtz1/Desktop/folder_b'
            transact = shutil.move(sender, receiver)
            print(transact)
        else:
            print(file + 'this file is too old')

# making the frame for the buttons
main_frame = Frame(transfer)
main_frame.pack()
# creating the buttons that will be used
open_explore = Button(main_frame, text='Open', fg='blue', command=fileopen)
open_explore.pack(side=TOP, pady=20)
# create open transfer folder
open_trans = Button(main_frame, text='Upload', fg='red', command=get_folder)
open_trans.pack(side=BOTTOM, pady=20)
# this function automates at 6pm every day, calling function file transfer
def routine():
    interval = schedule.every().day.at('18:00').do(automate)

transfer.mainloop()