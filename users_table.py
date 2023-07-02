from tkinter import *
from datetime import datetime
import sqlite3
#connect to the test database
conn = sqlite3.connect("test.db")
c = conn.cursor()

#create the table users
conn.execute('''CREATE TABLE IF NOT EXISTS users(
	id INTEGER PRIMARY KEY,
	title TEXT,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	mail_id TEXT UNIQUE,
	phone_number TEXT NOT NULL,
	created_on TEXT NOT NULL)'''
	)

#get the current local date and time
c.execute("SELECT datetime('now','localtime')")
currentDateTime  = c.fetchone()[0]

#insert the data into users table
conn.execute("INSERT INTO users(title, first_name, last_name, mail_id, phone_number, created_on)"+
             " VALUES('Mrs', 'Sangeetha', 'Krishnamoorthy', 'sangeetha.krishnamoorthy@gmail.com','+49 176 466 26 093','"+currentDateTime+"')")

#save data permanently in the database
conn.commit()
#close the connection to the database
conn.close()
