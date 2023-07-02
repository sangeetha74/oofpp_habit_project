from tkinter import *
from datetime import datetime 
import sqlite3
#connect to the test database
conn = sqlite3.connect('test.db')
c = conn.cursor()

#create the table habit_completion
c.execute('''CREATE TABLE IF NOT EXISTS habit_completion(
	id INTEGER PRIMARY KEY,
	habit_id INTEGER NOT NULL,
	completion_status INTEGER NOT NULL,
	created_on TEXT NOT NULL,
	FOREIGN KEY (habit_id) REFERENCES habit(id))'''
	)

'''
Insert datas into the habit_completion table.
'''

###for sunday habits

######4th June
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(4, 1, '2023-06-04 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(5, 1, '2023-06-04 00:00:00')''')

######11th June
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(4, 1, '2023-06-11 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(5, 1, '2023-06-11 00:00:00')''')

######18th June
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(4, 1, '2023-06-18 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(5, 1, '2023-06-18 00:00:00')''')

######25th June
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(4, 1, '2023-06-25 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(5, 1, '2023-06-25 00:00:00')''')

###for Monday habits on

######29th May
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(1, 1, '2023-05-29 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(2, 1, '2023-05-29 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(3, 1, '2023-05-29 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(4, 1, '2023-05-29 00:00:00')''')

######5th June
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(1, 1, '2023-06-05 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(2, 1, '2023-06-05 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(3, 1, '2023-06-05 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(4, 1, '2023-06-05 00:00:00')''')

######12th June
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(1, 1, '2023-06-12 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(2, 1, '2023-06-12 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(3, 1, '2023-06-12 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(4, 1, '2023-06-12 00:00:00')''')

######19th June
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(1, 1, '2023-06-19 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(2, 1, '2023-06-19 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(3, 1, '2023-06-19 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(4, 1, '2023-06-19 00:00:00')''')

######26thth June
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(1, 1, '2023-06-26 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(2, 1, '2023-06-26 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(3, 1, '2023-06-26 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(4, 1, '2023-06-26 00:00:00')''')

###for tuesday habits

######30th May
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(1, 1, '2023-05-30 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(2, 1, '2023-05-30 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(4, 1, '2023-05-30 00:00:00')''')

######6th June
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(1, 1, '2023-06-06 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(2, 1, '2023-06-06 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(4, 1, '2023-06-06 00:00:00')''')

######13th June
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(1, 1, '2023-06-13 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(2, 1, '2023-06-13 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(4, 1, '2023-06-13 00:00:00')''')

######20th June
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(1, 1, '2023-06-20 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(2, 1, '2023-06-20 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(4, 1, '2023-06-20 00:00:00')''')

######27th June
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(1, 1, '2023-06-27 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(2, 1, '2023-06-27 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(4, 1, '2023-06-27 00:00:00')''')

###for wednesday habits

######31st May
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(3, 1, '2023-05-31 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(4, 1, '2023-05-31 00:00:00')''')

######7th June
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(3, 1, '2023-06-07 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(4, 1, '2023-06-07 00:00:00')''')

######14th June
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(3, 1, '2023-06-14 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(4, 1, '2023-06-14 00:00:00')''')

######21st June
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(3, 1, '2023-06-21 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(4, 1, '2023-06-21 00:00:00')''')

######28th June
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(3, 1, '2023-06-28 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(4, 1, '2023-06-28 00:00:00')''')


###for thursday habits

######1st June
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(1, 1, '2023-06-01 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(2, 1, '2023-06-01 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(4, 1, '2023-06-01 00:00:00')''')

######8th June
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(1, 1, '2023-06-08 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(2, 1, '2023-06-08 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(4, 1, '2023-06-08 00:00:00')''')

######15th June
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(1, 1, '2023-06-15 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(2, 1, '2023-06-15 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(4, 1, '2023-06-15 00:00:00')''')

######22nd June
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(1, 1, '2023-06-22 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(2, 1, '2023-06-22 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(4, 1, '2023-06-22 00:00:00')''')

######29th June
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(1, 1, '2023-06-29 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(2, 1, '2023-06-29 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(4, 1, '2023-06-29 00:00:00')''')

###for friday habits

######2nd June
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(1, 1, '2023-06-02 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(2, 1, '2023-06-02 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(3, 1, '2023-06-02 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(4, 1, '2023-06-02 00:00:00')''')

######9th June
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(1, 1, '2023-06-09 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(2, 1, '2023-06-09 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(3, 1, '2023-06-09 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(4, 1, '2023-06-09 00:00:00')''')

######16th June
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(1, 1, '2023-06-16 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(2, 1, '2023-06-16 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(3, 1, '2023-06-16 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(4, 1, '2023-06-16 00:00:00')''')

######23rd June
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(1, 1, '2023-06-23 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(2, 1, '2023-06-23 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(3, 1, '2023-06-23 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(4, 1, '2023-06-23 00:00:00')''')

######30th June
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(1, 1, '2023-06-30 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(2, 1, '2023-06-30 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(3, 1, '2023-06-30 00:00:00')''')
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(4, 1, '2023-06-30 00:00:00')''')

###for saturday habis

######3rd June
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(4, 1, '2023-06-03 00:00:00')''')

######10th June
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(4, 1, '2023-06-10 00:00:00')''')

######17th June
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(4, 1, '2023-06-17 00:00:00')''')

######24th June
c.execute('''INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(4, 1, '2023-06-24 00:00:00')''')


#save data permanently in the database
conn.commit()

#close the connection to the database
conn.close()
