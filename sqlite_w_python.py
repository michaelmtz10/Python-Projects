import sqlite3

ron = sqlite3.connect('cars.db')
dom = ron.cursor()

# creating the table with columns

dom.execute('''CREATE TABLE first_attempt(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    FILE_NAME VARCHAR(50) NOT NULL
    )''')

ron.commit()
ron.close()

ron = sqlite3.connect('cars.db')
dom = ron.cursor()
# created a tuple with the files
files = ('information.docx', 'Hello.txt','myImage.png','myMovies.png','World.txt','data.pdf','myphoto.jpg')
# creating a loop to find file with txt and inserting into the table
for file in files:
    if file.endswith('txt'):
        print(file)
        dom.execute("INSERT INTO first_attempt(FILE_NAME) VALUES (?)", (file,))

ron.commit()
ron.close()


#dom.execute('''INSERT INTO first_attempt(FILE_NAME, FILE_DATE) VALUES
    #('information.docx', '5-5-45'),
    #('Hello.txt', '5-5-45'),
    #('myImage.png', '5-5-45'),
    #('myMovies.png', '5-5-45'),
    #('World.txt', '5-5-45'),
    #('data.pdf', '5-5-45'),
    #('myphoto.jpg', '5-5-45')''')



