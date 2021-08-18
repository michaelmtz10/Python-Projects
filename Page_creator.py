from tkinter import *
import webbrowser

root = Tk()
root.title('QuickPage')
root.geometry('500x450')

# creating function
def clear():
    scratch.delete(1.0, END)

# will open html with whats typed in scratch
def file():
    var = scratch.get(1.0, END)
    page = open('newfile.html', 'w')

    paragraph = f"""<html><head></head>
    <body></body>
    <p>{var}</p>
    </html>""".format(var=var)
    page.write(paragraph)
    page.close()
    webbrowser.open_new_tab('newfile.html')

def set_update():
    capsule.config(text=scratch.get(1.0, END))

# main writing pad
scratch = Text(root, width=50, height=12, font=('Cambria', 16))
scratch.pack(pady=20)
# frame where buttons go
button_frame = Frame(root)
button_frame.pack()
# created clear button
clear_button = Button(button_frame, text='clear', command=clear)
clear_button.grid(row=0, column=0)

# creates the generate button
open_page_btn = Button(button_frame, text='generate', command=file)
open_page_btn.grid(row=0, column=2, pady=20)
# displays label on gui

capsule = Label(root, text='', font=('George', 10))
capsule.pack(pady=20)


root.mainloop()
