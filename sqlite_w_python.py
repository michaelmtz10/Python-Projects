import sqlite3

ron = sqlite3.connect('hello.db')
dom = ron.cursor()

# creating the table

dom.execute('''CREATE TABLE first_attempt(
    FILE_NAME VARCHAR(50) NOT NULL,
    FILE_DATE
    )''')

ron.commit()
ron.close()

ron = sqlite3.connect('hello.db')
dom = ron.cursor()

dom.execute('''INSERT INTO first_attempt(FILE_NAME, FILE_DATE) VALUES
    ('information.docx', '5-5-45'),
    ('Hello.txt', '5-5-45'),
    ('myImage.png', '5-5-45'),
    ('myMovies.png', '5-5-45'),
    ('World.txt', '5-5-45'),
    ('data.pdf', '5-5-45'),
    ('myphoto.jpg', '5-5-45')''')

ron.commit()
ron.close()

ron = sqlite3.connect('hello.db')
dom = ron.cursor()

dom.execute('''SELECT * FROM first_attempt WHERE FILE_NAME = "Hello.txt"; ''')

files = dom.fetchall()

for file in files:
    print(file)

ron.commit()
ron.close()