import sqlite3
def createuserstable():
  database = sqlite3.connect('baza.sqlite')
  cursor = database.cursor()

  cursor.execute('''CREATE TABLE IF NOT EXISTS users(
  user_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
  fullname VARCHAR,
  username VARCHAR,
  chatid INTEGER UNIQUE
  )''')

  database.commit()
  database.close()

createuserstable()

def registeruser(full_name, user_name, chat_id):
  database = sqlite3.connect('baza.sqlite')
  cursor = database.cursor()
  cursor.execute('''INSERT INTO users(fullname, username, chatid)
  VALUES(?,?,?)''', (full_name, user_name, chat_id))
  database.commit()
  database.close()




git config --global user.name "Sanjarbek"
 git config --global user.email "jonpolat957@gmail.com"
git init
Reinitialized existing Git repository in C:/Users/IT Center 12/Desktop/90/.git/
 git add .
 git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/sanjarbek011/90.git

git push -u origin main








