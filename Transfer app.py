from tkinter import * 
from tkinter import filedialog
import shutil

app = Tk()
app.title('File Transfer')
app.geometry('350x150')

# assigning variable
# transfers selected file into selected folder
def transfer():
    transfer_path = shutil.move(filename, d_name)
 # open file explore and allows user to select file   
def getfile():
    global filename
    filename = filedialog.askopenfilename()
    find_file.insert(END, filename)
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

