from tkinter import *
from datetime import datetime
import sqlite3
#from PIL import ImageTk, Image

conn = sqlite3.connect('test.db')

###create the habit table
conn.execute('''CREATE TABLE IF NOT EXISTS habit(
	id INTEGER PRIMARY KEY,
	habit_name TEXT UNIQUE,
	sun INTEGER NOT NULL,
	mon INTEGER NOT NULL,
	tue INTEGER NOT NULL,
	wed INTEGER NOT NULL,
	thu INTEGER NOT NULL,
	fri INTEGER NOT NULL,
	sat INTEGER NOT NULL,
	habit_status TEXT NOT NULL,
	users_id INTEGER NOT NULL,
	created_on TEXT NOT NULL,
    FOREIGN KEY (users_id) REFERENCES users(id)
)''')

c = conn.cursor()

###insert datas into the table
c.execute("insert into habit(habit_name, sun, mon, tue, wed, thu, fri, sat, habit_status, users_id, created_on)"+
   " values('Do Yoga in the morning', 0, 1, 1, 0, 1, 1, 0, 'A', 1, datetime('now','localtime'))")
c.execute("insert into habit(habit_name, sun, mon, tue, wed, thu, fri, sat, habit_status, users_id, created_on)"+
   " values('Drink 2L water', 0, 1, 1, 0, 1, 1, 0, 'A', 1, datetime('now','localtime'))")
c.execute("insert into habit(habit_name, sun, mon, tue, wed, thu, fri, sat, habit_status, users_id, created_on)"+
  " values('Go for jogging', 0, 1, 0, 1, 0, 1, 0, 'A', 1, datetime('now','localtime'))")
c.execute("insert into habit(habit_name, sun, mon, tue, wed, thu, fri, sat, habit_status, users_id, created_on)"+
  "  values('Do Reiki', 1, 1, 1, 1, 1, 1, 1, 'A', 1, datetime('now','localtime'))")
c.execute("insert into habit(habit_name, sun, mon, tue, wed, thu, fri, sat, habit_status, users_id, created_on)"+
  " values('Call Parents', 1, 0, 0, 0, 0, 0, 0, 'A',1, datetime('now','localtime'))")

#save changes to the database
conn.commit()
#close the connection to the database
conn.close()
