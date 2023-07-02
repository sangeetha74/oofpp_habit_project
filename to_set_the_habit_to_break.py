from tkinter import *
from datetime import datetime
import sqlite3

# connect to the database
conn = sqlite3.connect('test.db')
c = conn.cursor()

# get the current
c.execute("SELECT datetime('now','localtime')")
currentDateTime = c.fetchone()[0]

c.execute("SELECT strftime('%w','" + currentDateTime + "')")
currentDay = c.fetchone()[0]

c.execute("SELECT rowid FROM users WHERE mail_id='sangeetha.krishnamoorthy@gmail.com'")
UserID = c.fetchone()[0]

if int(currentDay) == 0:
    c.execute("SELECT rowid,* FROM habit WHERE users_id=" + str(UserID) + " AND habit_status='A' AND sun=1")
elif int(currentDay) == 1:
    c.execute("SELECT rowid,* FROM habit WHERE users_id=" + str(UserID) + " AND habit_status='A' AND mon=1")
elif int(currentDay) == 2:
    c.execute("SELECT rowid,* FROM habit WHERE users_id=" + str(UserID) + " AND habit_status='A' AND tue=1")
elif int(currentDay) == 3:
    c.execute("SELECT rowid,* FROM habit WHERE users_id=" + str(UserID) + " AND habit_status='A' AND wed=1")
elif int(currentDay) == 4:
    c.execute("SELECT rowid,* FROM habit WHERE users_id=" + str(UserID) + " AND habit_status='A' AND thu=1")
elif int(currentDay) == 5:
    c.execute("SELECT rowid,* FROM habit WHERE users_id=" + str(UserID) + " AND habit_status='A' AND fri=1")
elif int(currentDay) == 6:
    c.execute("SELECT rowid,* FROM habit WHERE users_id=" + str(UserID) + " AND habit_status='A' AND sat=1")

rows = c.fetchall()
for i in rows:
    '''
    Check whether the user has checked-off the habit.
    If user checked-off the habit then it will ignore that habit.
    Otherwise it will update the habit table with habit_status as 'NA' (not active)
    '''
    c.execute("SELECT count(*) FROM habit_completion hc WHERE hc.habit_id = " + str(i[1]) +
              " AND substr(hc.created_on, 1, 10)=substr('" + currentDateTime + "', 1, 10) AND hc.completion_status=1")
    habit_completion_count = c.fetchone()[0]

    if int(habit_completion_count) == 1:
        # messagebox.showinfo(title="Info",message="This Habit is checked-off already!", parent=DH_nxt)
        print("The Habit '" + str(i[2]) + "' is checked-off already!")
    else:
        '''
        It will update the habit table with habit_status as 'NA' (not active).
        Which means the habit is brocken.
        '''
        # set habit_status in habit table to not active. It is broken.
        c.execute("UPDATE habit SET habit_status='NA' WHERE id=" + str(i[1]))
        conn.commit()
        # Add a new record into the Habit_Completion table and set completion_status to 0
        c.execute(
            "INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(:habit_id, :completion_status, :created_on)",
            {
                'habit_id': i[1],
                'completion_status': 0,
                'created_on': currentDateTime
            }
            )
        # set completion_status in habit_completion table to 0 for the habit_id
        c.execute("UPDATE habit_completion SET completion_status = 0 WHERE habit_id=" + str(i[1]))
        # save the changes to the database
        conn.commit()

        print("The Habit '" + str(i[2]) + "' has been brocken!")

conn.close()
