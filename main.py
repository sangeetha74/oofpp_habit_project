from tkinter import *
from datetime import date
from datetime import datetime
#from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
import sqlite3

class habit_tracker:

    ### initialize the database
    def __init__(self, db):
        self.db = db

    '''
    This window will display the habits in the Treeview in tkinter.
    '''

    def DHabits(self):
        DH_nxt = Tk()
        # set the window size
        DH_nxt.geometry("1050x500")
        DH_nxt.maxsize(1050, 500)
        DH_nxt.minsize(1050, 500)
        DH_nxt.title('User Habits')

        # Add style to our Treeview
        style = ttk.Style()

        # choose a theme for our Treeview
        style.theme_use('default')

        # set Treeview color
        style.configure("Treeview",
                        background="#D3D3D3",
                        foreground="black",
                        rowheight=30,
                        fieldbackground="#D3D3D3")

        # change selected color
        style.map('Treeview',
                  background=[('selected', "#347083")])

        # set a treeview frame
        tree_frame = Frame(DH_nxt, width=845, height=670)
        tree_frame.pack(padx=10, pady=10)

        # set a treeview scrollbar
        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        conn = sqlite3.connect(self.db)
        c = conn.cursor()
        my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="browse")
        my_tree.pack()

        # set the scrollbar
        tree_scroll.config(command=my_tree.yview)

        # set the Treeview columns
        my_tree["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
        my_tree['show'] = 'headings'
        my_tree.column("1", width=50, anchor='c')
        my_tree.column("2", width=500, anchor='w')
        my_tree.column("3", width=50, anchor='c')
        my_tree.column("4", width=50, anchor='c')
        my_tree.column("5", width=50, anchor='c')
        my_tree.column("6", width=50, anchor='c')
        my_tree.column("7", width=50, anchor='c')
        my_tree.column("8", width=50, anchor='c')
        my_tree.column("9", width=50, anchor='c')
        my_tree.column("10", width=100, anchor='c')

        # set the Treeview column names
        my_tree.heading("1", text="ID")
        my_tree.heading("2", text="Habit name")
        my_tree.heading("3", text="Sun")
        my_tree.heading("4", text="Mon")
        my_tree.heading("5", text="Tue")
        my_tree.heading("6", text="Wed")
        my_tree.heading("7", text="Thu")
        my_tree.heading("8", text="Fri")
        my_tree.heading("9", text="Sat")
        my_tree.heading("10", text="Habit status")

        # set color for rows
        my_tree.tag_configure('oddrow', background="white")
        my_tree.tag_configure('evenrow', background="lightblue")

        # initialize the variable
        count = 0

        # Query to select all the rows from Habit table for the customer
        c.execute('SELECT rowid,* FROM habit WHERE users_id=' + str(user_id))
        r = c.fetchall()
        for rd in r:
            if count % 2 == 0:
                my_tree.insert("", 'end', iid=count, text='',
                               values=(rd[0], rd[2], rd[3], rd[4], rd[5], rd[6], rd[7], rd[8], rd[9], rd[10]),
                               tags=('evenrow',))
            else:
                my_tree.insert("", 'end', iid=count, text='',
                               values=(rd[0], rd[2], rd[3], rd[4], rd[5], rd[6], rd[7], rd[8], rd[9], rd[10]),
                               tags=('oddrow',))
            # increment the counter
            count += 1

        # record entry boxes
        data_frame = LabelFrame(DH_nxt, text="Record")
        data_frame.pack(fill="x", expand="yes", padx=20)

        id_label = Label(data_frame, text="ID")
        id_label.grid(row=0, column=0, padx=10, pady=10)
        id_entry = Entry(data_frame)
        id_entry.config(state="disabled")
        id_entry.grid(row=0, column=1, padx=10, pady=10)

        habit_label = Label(data_frame, text="Habit")
        habit_label.grid(row=0, column=2, padx=10, pady=10)
        habit_entry = Entry(data_frame)
        habit_entry.config(state="disabled")
        habit_entry.grid(row=0, column=3, padx=10, pady=10)

        # save the values into the variables
        sun_entry = Entry(data_frame)
        mon_entry = Entry(data_frame)
        tue_entry = Entry(data_frame)
        wed_entry = Entry(data_frame)
        thu_entry = Entry(data_frame)
        fri_entry = Entry(data_frame)
        sat_entry = Entry(data_frame)

        # set habit completion
        def habit_completion():
            # connect to the database
            conn = sqlite3.connect(self.db)

            # create a cursor instance
            c = conn.cursor()

            # get the current datetime and store it in a variable
            c.execute("SELECT datetime('now','localtime')")
            currentDateTime = c.fetchone()[0]

            # find the current day
            c.execute("SELECT strftime('%w','" + currentDateTime + "')");
            currentDay = c.fetchone()[0]

            # check if the Habit is checked-off already, if it is checked-off show the message
            c.execute("SELECT count(*) FROM habit_completion hc WHERE hc.habit_id = " + id_entry.get() +
                      " AND substr(hc.created_on, 1, 10)=substr('" + currentDateTime + "', 1, 10)")

            # get the count into the variable
            habit_completion_count = c.fetchone()[0]

            # check whether the record exists and display the message
            if int(habit_completion_count) == 1:
                messagebox.showinfo(title="Info", message="This Habit is checked-off already!", parent=DH_nxt)
            else:
                # Add a new record into the Habit_Completion table
                c.execute(
                    "INSERT INTO habit_completion(habit_id, completion_status, created_on) VALUES(:habit_id, :completion_status, :created_on)",
                    {
                        'habit_id': id_entry.get(),
                        'completion_status': 1,
                        'created_on': currentDateTime
                    }
                    )
                # save the changes into the database
                conn.commit()
                # display the message to the user
                messagebox.showinfo(title="Info", message="Habit has been checked-off!", parent=DH_nxt)
            # close the connection
            conn.close()

        ###longest_streak
        def longest_streak():
            # connect to the databse
            conn = sqlite3.connect(self.db)
            # open the cursor
            c = conn.cursor()
            myhabitstreak = ""
            # find the longest streak using the query
            try:
                longest_streak_qry = "select myhabit, max(mycount) from (SELECT hb.habit_name myhabit, count(*) mycount FROM habit_completion hc INNER JOIN habit hb WHERE hb.id = hc.habit_id"
                longest_streak_qry = longest_streak_qry + " AND hb.users_id = " + str(
                    user_id) + " AND hb.habit_status='A' AND hc.completion_status=1 GROUP BY hc.habit_id HAVING count(*) > 1 ORDER BY count(*) desc)"
                c.execute(longest_streak_qry)
                row = c.fetchall()
                for data in row:
                    myhabitstreak = myhabitstreak + "\n" + data[0]

            except sqlite3.Error as er:
                print('Longest Streak exception in the database')

            # save the changes into the database
            conn.commit()
            # close the connection
            conn.close()
            # display the message box to the user
            messagebox.showinfo(title="Longest Streak", message="Longest Streak is " + myhabitstreak, parent=DH_nxt)

            ###last month struggle

        def last_month_struggle():
            # connect to the databse
            conn = sqlite3.connect(self.db)
            # open the cursor
            c = conn.cursor()

            ###start of the month
            c.execute("SELECT datetime(datetime('now', 'start of month'), '-1 month')")
            firstdayofmonth = c.fetchone()[0]

            ###end of the month
            c.execute("SELECT datetime(datetime('now', 'start of month'), '-1 day')")
            lastdayofmonth = c.fetchone()[0]

            c.execute("SELECT datetime('now','localtime')")
            currentday = c.fetchone()[0]

            myhabitstreak = ""
            # find the longest streak using the query
            # try:
            last_month_struggle_qry = "SELECT hc.habit_id myhabitid, count(*) mycount "
            last_month_struggle_qry = last_month_struggle_qry + " FROM habit hb INNER JOIN habit_completion hc WHERE hb.id = hc.habit_id"
            last_month_struggle_qry = last_month_struggle_qry + " AND hb.users_id = " + str(
                user_id) + " AND hb.habit_status='A' AND hc.completion_status=1 "
            last_month_struggle_qry = last_month_struggle_qry + " AND hc.created_on BETWEEN '" + firstdayofmonth + "' AND '" + lastdayofmonth + "' GROUP BY hc.habit_id HAVING count(*) > 1 ORDER BY count(*) asc limit 1"

            c.execute(last_month_struggle_qry)
            habitid_struggle = c.fetchone()[0]

            c.execute("SELECT habit_name FROM habit WHERE id=" + str(habitid_struggle))
            habitname_struggle = c.fetchone()[0]

            # for data in row:
            myhabitstreak = myhabitstreak + "\n" + habitname_struggle

            # except sqlite3.Error as er:
            #    print('exception from last_month_struggle()')

            # save the changes into the database
            conn.commit()
            # close the connection
            conn.close()
            # display the message box to the user
            messagebox.showinfo(title="Last month struggle",
                                message="User had the struggle with the following habit \n" + myhabitstreak,
                                parent=DH_nxt)

            ###current daily habits

        def current_habits():
            # connect to the database
            conn = sqlite3.connect(self.db)
            # open the cursor
            c = conn.cursor()
            myhabitstreak = ""
            # execute the query to get the current active habits
            try:
                current_habits_qry = "SELECT hb.habit_name FROM habit hb WHERE hb.users_id = " + str(
                    user_id) + " AND habit_status='A' ORDER BY hb.id"
                c.execute(current_habits_qry)
                row = c.fetchall()
                for data in row:
                    myhabitstreak = myhabitstreak + "\n" + data[0]

            except sqlite3.Error as er:
                print('Longest Streak exception')

            # save the changes into the database
            conn.commit()
            # close the connection
            conn.close()
            messagebox.showinfo(title="My current habits", message=myhabitstreak, parent=DH_nxt)

            # add a new habit

        def add_habit():
            habit = Tk()
            habit.title('Create a new habit')
            # create a new window
            habit.geometry("500x500")
            habit.maxsize(500, 500)
            habit.minsize(500, 500)

            new_habit_label = Label(habit, text="Create habit", font="Arial 20 bold")
            new_habit_label.place(x=130, y=30)

            # entry for Habit
            habit_label = Label(habit, text="Habit")
            habit_label.place(x=20, y=100)
            new_habit_entry = Entry(habit, width=50)
            new_habit_entry.place(x=100, y=100)

            # entry for sunday
            habit_sun = Label(habit, text="Sun (1 or 0)")
            habit_sun.place(x=20, y=130)
            habit_sun_entry = Entry(habit)
            habit_sun_entry.insert(0, 0)
            habit_sun_entry.place(x=100, y=130)

            # entry for Monday
            habit_mon = Label(habit, text="Mon (1 or 0)")
            habit_mon.place(x=20, y=160)
            habit_mon_entry = Entry(habit)
            habit_mon_entry.insert(0, 0)
            habit_mon_entry.place(x=100, y=160)

            # entry for Tuesday
            habit_tue = Label(habit, text="Tue (1 or 0)")
            habit_tue.place(x=20, y=190)
            habit_tue_entry = Entry(habit)
            habit_tue_entry.insert(0, 0)
            habit_tue_entry.place(x=100, y=190)

            # entry for Wednesday
            habit_wed = Label(habit, text="Wed (1 or 0)")
            habit_wed.place(x=20, y=220)
            habit_wed_entry = Entry(habit)
            habit_wed_entry.insert(0, 0)
            habit_wed_entry.place(x=100, y=220)

            # entry for Thursday
            habit_thu = Label(habit, text="Thu (1 or 0)")
            habit_thu.place(x=20, y=250)
            habit_thu_entry = Entry(habit)
            habit_thu_entry.insert(0, 0)
            habit_thu_entry.place(x=100, y=250)

            # entry for Friday
            habit_fri = Label(habit, text="Fri (1 or 0)")
            habit_fri.place(x=20, y=280)
            habit_fri_entry = Entry(habit)
            habit_fri_entry.insert(0, 0)
            habit_fri_entry.place(x=100, y=280)

            # entry for Saturday
            habit_sat = Label(habit, text="Sat (1 or 0)")
            habit_sat.place(x=20, y=310)
            habit_sat_entry = Entry(habit)
            habit_sat_entry.insert(0, 0)
            habit_sat_entry.place(x=100, y=310)

            new_habit_entry.focus_set()

            # save the new Habit to the database table
            def save_habit():
                # connect to the database
                conn = sqlite3.connect(self.db)
                # create a cursor instance
                c = conn.cursor()
                # get the current datetime and store it in a variable
                c.execute("SELECT datetime('now','localtime')")
                currentDateTime = c.fetchone()[0]
                # if user didn't enter 1 or 0 then it will display the message to the user
                try:
                    if int(habit_sun_entry.get()) not in (1, 0):
                        raise TypeError
                    if int(habit_mon_entry.get()) not in (1, 0):
                        raise TypeError
                    if int(habit_tue_entry.get()) not in (1, 0):
                        raise TypeError
                    if int(habit_wed_entry.get()) not in (1, 0):
                        raise TypeError
                    if int(habit_thu_entry.get()) not in (1, 0):
                        raise TypeError
                    if int(habit_fri_entry.get()) not in (1, 0):
                        raise TypeError
                    if int(habit_sat_entry.get()) not in (1, 0):
                        raise TypeError

                    # check whether user selected any one day. If not display message to select atleast one day!
                    if int(habit_sun_entry.get()) == 0:
                        if int(habit_mon_entry.get()) == 0:
                            if int(habit_tue_entry.get()) == 0:
                                if int(habit_wed_entry.get()) == 0:
                                    if int(habit_thu_entry.get()) == 0:
                                        if int(habit_fri_entry.get()) == 0:
                                            if int(habit_sat_entry.get()) == 0:
                                                raise ValueError

                    # Add a new record into the Habit table
                    c.execute(
                        "INSERT INTO habit(habit_name, sun, mon, tue, wed, thu, fri, sat, habit_status, users_id, created_on)" +
                        "VALUES(:habit_name, :sun, :mon, :tue, :wed, :thu, :fri, :sat, :habit_status, :users_id, :created_on)",
                        {
                            'habit_name': new_habit_entry.get(),
                            'sun': habit_sun_entry.get(),
                            'mon': habit_mon_entry.get(),
                            'tue': habit_tue_entry.get(),
                            'wed': habit_wed_entry.get(),
                            'thu': habit_thu_entry.get(),
                            'fri': habit_fri_entry.get(),
                            'sat': habit_sat_entry.get(),
                            'habit_status': 'A',
                            'users_id': user_id,
                            'created_on': currentDateTime
                        }
                        )
                    # save the changes to the database
                    conn.commit()
                    # display the message to the user
                    messagebox.showinfo(title="Info", message="New Habit has been created!", parent=habit)
                    # close the connection
                    conn.close()
                    # clear the previous input
                    new_habit_entry.delete(0, END)
                    habit_sun_entry.delete(0, END)
                    habit_mon_entry.delete(0, END)
                    habit_tue_entry.delete(0, END)
                    habit_wed_entry.delete(0, END)
                    habit_thu_entry.delete(0, END)
                    habit_fri_entry.delete(0, END)
                    habit_sat_entry.delete(0, END)
                    new_habit_entry.focus_set()
                except TypeError:
                    messagebox.showinfo(title="Info",
                                        message="Sun, Mon, Tue, Wed, Thu, Fri and Sat entries must be 1 or 0!",
                                        parent=habit)
                except ValueError:
                    messagebox.showinfo(title="Info",
                                        message="Please select anyone of the day ( Enter 1 in any one of the Day )!",
                                        parent=habit)

            # create a save button
            save_button = Button(habit, text='Save', width=10, height=2, font='bold', fg='white', bg='green',
                                 command=save_habit)
            save_button.place(x=100, y=350)
            # create button to close the current window
            habit_exit_button = Button(habit, text='Close', width=10, height=2, font='bold', fg='white', bg='green',
                                       command=habit.destroy)
            # add exit button
            habit_exit_button.place(x=250, y=350)

        # delete a record
        def delete_record():
            x = my_tree.selection()[0]
            my_tree.delete(x)
            # call the function from function_collection module to delete the record
            try:
                # connect to the database
                conn = sqlite3.connect(self.db)
                # open the cursor
                c = conn.cursor()
                # set the query to delete datas from the habit_completion table
                del_habit_comp_qry = "DELETE FROM habit_completion WHERE habit_id = " + id_entry.get()
                # execute the query
                c.execute(del_habit_comp_qry)
                # set the query to delete the data from the habit table
                del_query = "DELETE FROM habit WHERE oid = " + id_entry.get()
                # execute the query
                c.execute(del_query)
                # save the changes to the database
                conn.commit()

            except sqlite3.Error as er:
                print('delete exception on the database')

            # display the message to the user
            messagebox.showinfo(title="Info", message="Record has been deleted!", parent=DH_nxt)
            # clear the entry boxes
            clear_entry_boxes()

        # refresh the current window
        def refresh_curr_win():

            for row in my_tree.get_children():
                my_tree.delete(row)
            # set the variable to 0
            count = 0
            # Query to select all the rows from Habit table for the customer
            c.execute('SELECT rowid,* FROM habit WHERE users_id=' + str(user_id))
            r = c.fetchall()
            for rd in r:
                if count % 2 == 0:
                    my_tree.insert("", 'end', iid=count, text='',
                                   values=(rd[0], rd[2], rd[3], rd[4], rd[5], rd[6], rd[7], rd[8], rd[9], rd[10]),
                                   tags=('evenrow',))
                else:
                    my_tree.insert("", 'end', iid=count, text='',
                                   values=(rd[0], rd[2], rd[3], rd[4], rd[5], rd[6], rd[7], rd[8], rd[9], rd[10]),
                                   tags=('oddrow',))
                # increment the counter
                count += 1

            # bind the treeview
            my_tree.bind("<ButtonRelease-1>", fill_entries)

        # clear all the entry boxes
        def clear_entry_boxes():
            id_entry.delete(0, END)
            habit_entry.delete(0, END)
            sun_entry.delete(0, END)
            mon_entry.delete(0, END)
            tue_entry.delete(0, END)
            wed_entry.delete(0, END)
            thu_entry.delete(0, END)
            fri_entry.delete(0, END)
            sat_entry.delete(0, END)

        # fill_entry boxes
        def fill_entries(e):
            # clear entry boxes
            id_entry.delete(0, END)
            habit_entry.delete(0, END)
            sun_entry.delete(0, END)
            mon_entry.delete(0, END)
            tue_entry.delete(0, END)
            wed_entry.delete(0, END)
            thu_entry.delete(0, END)
            fri_entry.delete(0, END)
            sat_entry.delete(0, END)

            # get the record number
            selected = my_tree.focus()

            # get record values
            values = my_tree.item(selected, 'values')

            # output to entry boxes
            id_entry.config(state="normal")
            id_entry.delete(0, END)
            id_entry.insert(0, values[0])
            id_entry.config(state="disabled")

            habit_entry.config(state="normal")
            habit_entry.delete(0, END)
            habit_entry.insert(0, values[1])
            habit_entry.config(state="disabled")

            sun_entry.config(state="normal")
            sun_entry.delete(0, END)
            sun_entry.insert(0, values[2])
            # set the check box for sunday
            var1 = IntVar()
            chksun = Checkbutton(data_frame, text="Sun", variable=var1, state="disabled")
            if int(sun_entry.get()) == 1:
                chksun.select()
                # r=1
                sun_entry.insert(0, 1)
            else:
                chksun.deselect()
                # r=0
                sun_entry.insert(0, 0)
            chksun.grid(row=0, column=4, padx=10, pady=10)
            # set the check box for monday
            mon_entry.insert(0, values[3])
            var2 = IntVar()
            chkmon = Checkbutton(data_frame, text="Mon", variable=var2, state="disabled")
            if int(mon_entry.get()) == 1:
                chkmon.select()
            else:
                chkmon.deselect()
            chkmon.grid(row=0, column=5, padx=10, pady=10)
            # set the check box for tuesday
            tue_entry.insert(0, values[4])
            var3 = IntVar()
            chktue = Checkbutton(data_frame, text="Tue", variable=var3, state="disabled")
            if int(tue_entry.get()) == 1:
                chktue.select()
            else:
                chktue.deselect()
            chktue.grid(row=0, column=6, padx=10, pady=10)
            # set the check box for wednesday
            wed_entry.insert(0, values[5])
            var4 = IntVar()
            chkwed = Checkbutton(data_frame, text="Wed", variable=var4, state="disabled")
            if int(wed_entry.get()) == 1:
                chkwed.select()
            else:
                chkwed.deselect()
            chkwed.grid(row=0, column=7, padx=10, pady=10)
            # set the check box for thursday
            thu_entry.insert(0, values[6])
            var5 = IntVar()
            chkthu = Checkbutton(data_frame, text="Thu", variable=var5, state="disabled")
            if int(thu_entry.get()) == 1:
                chkthu.select()
            else:
                chkthu.deselect()
            chkthu.grid(row=0, column=8, padx=10, pady=10)
            # set the check box for friday
            fri_entry.insert(0, values[7])
            var6 = IntVar()
            chkfri = Checkbutton(data_frame, text="Fri", variable=var6, state="disabled")
            if int(fri_entry.get()) == 1:
                chkfri.select()
            else:
                chkfri.deselect()
            chkfri.grid(row=0, column=9, padx=10, pady=10)
            # set the check box for saturday
            sat_entry.insert(0, values[8])
            var7 = IntVar()
            chksat = Checkbutton(data_frame, text="Sat", variable=var7, state="disabled")
            if int(sat_entry.get()) == 1:
                chksat.select()
            else:
                chksat.deselect()
            chksat.grid(row=0, column=10, padx=10, pady=10)

            # get the current datetime and store it in a variable
            c.execute('SELECT DATE()')
            currentDateTime = c.fetchone()[0]
            # get the current day from the date
            c.execute("SELECT strftime('%w','" + currentDateTime + "')");
            currentDay = c.fetchone()[0]

            # initialize the variables to find the day
            sunday = 0
            monday = 0
            tuesday = 0
            wednesday = 0
            thursday = 0
            friday = 0
            saturday = 0
            '''
               In sqlite database it returns values based on the day.
               So here I am setting the day value based on user input.
            '''
            if int(values[2]) == 1:  # if the user input for sunday is 1 then I am setting value for Sunday
                sunday = 0
            if int(values[3]) == 1:
                monday = 1
            if int(values[4]) == 1:
                tuesday = 2
            if int(values[5]) == 1:
                wednesday = 3
            if int(values[6]) == 1:
                thursday = 4
            if int(values[7]) == 1:
                friday = 5
            if int(values[8]) == 1:
                saturday = 6

            # after selecting the row in a tree enable the delete button
            delete_button.config(state='normal')
            # check if the user input is the currentday then only user can set the habit is complete
            if (int(currentDay) in (sunday, monday, tuesday, wednesday, thursday, friday, saturday)) and values[
                9] == str('A'):
                habit_button.config(state='normal')
            else:
                habit_button.config(state='disabled')

        # add buttons here
        button_frame = LabelFrame(DH_nxt, text="Commands")
        button_frame.pack(fill="x", expand="yes", padx=20)

        # button to set complete
        habit_button = Button(button_frame, text="checked-off", font='bold', width=15, height=1, fg='white', bg='green',
                              command=habit_completion, state=DISABLED)
        habit_button.grid(row=0, column=1, padx=10, pady=10)

        # button to delete a record
        delete_button = Button(button_frame, text="Delete Record", font='bold', width=15, height=1, fg='white',
                               bg='green', command=delete_record, state=DISABLED)
        delete_button.grid(row=0, column=2, padx=10, pady=10)

        # button to add a new habit
        exit_button = Button(button_frame, text="Add new Habit", font='bold', width=15, height=1, fg='white',
                             bg='green', command=add_habit)
        exit_button.grid(row=0, column=3, padx=10, pady=10)

        # button to close the current window
        exit_button = Button(button_frame, text="Close", font='bold', width=15, height=1, fg='white', bg='green',
                             command=DH_nxt.destroy)
        exit_button.grid(row=0, column=4, padx=10, pady=10)

        # button to referesh the current window
        exit_button = Button(button_frame, text="Refresh", font='bold', width=15, height=1, fg='white', bg='green',
                             command=refresh_curr_win)
        exit_button.grid(row=0, column=5, padx=10, pady=10)

        ###### report analysis
        # add buttons here
        rep_button_frame = LabelFrame(DH_nxt, text="Reports")
        rep_button_frame.pack(fill="x", expand="yes", padx=20)

        # button to set complete
        habit_button1 = Button(rep_button_frame, text="Longest streak", font='bold', width=15, height=1, fg='white',
                               bg='green', command=longest_streak)
        habit_button1.grid(row=0, column=1, padx=10, pady=10)

        # button to show the current habits
        current_habits = Button(rep_button_frame, text="Current Habits", font='bold', width=15, height=1, fg='white',
                                bg='green', command=current_habits)
        current_habits.grid(row=0, column=2, padx=10, pady=10)

        # button to show with which habits did I struggle most last month?
        struggle_button = Button(rep_button_frame, text="last month struggle", font='bold', width=15, height=1,
                                 fg='white', bg='green', command=last_month_struggle)
        struggle_button.grid(row=0, column=3, padx=10, pady=10)

        # bind the treeview
        my_tree.bind("<ButtonRelease-1>", fill_entries)

    # setting the initial window for the project
    def tracker(self):
        # set the window
        root = Tk()
        root.title('Habit tracker application Window')
        # set window size
        root.geometry("500x500")
        root.maxsize(500, 500)
        root.minsize(500, 500)

        # display the image on the screen
        #img = Image.open("habit_tracker_image.jpg")
        #img = img.resize((100, 100))
        #habitimage = ImageTk.PhotoImage(img)
        #label = Label(root, image=habitimage)
        #label.place(x=200, y=20)
        global user_id
        # display the text on the window
        l1 = Label(root, text="Habit Tracker App", font="Arial 20 bold")
        l1.place(x=130, y=120)

        # connect to the database
        conn = sqlite3.connect(self.db)
        # open the cursor
        c = conn.cursor()

        # here we have to select the current user with their email id. It is unique in the Customer table
        c.execute("SELECT rowid,* FROM users WHERE mail_id='sangeetha.krishnamoorthy@gmail.com'")
        r = c.fetchall()

        for i in r:
            '''Display the label for rowid'''
            lid = Label(root, text="ID")
            lid.place(x=20, y=180)
            id = Label(root, bg='white', width=50, text=i[0], anchor='w')
            user_id = i[0]
            id.place(x=100, y=180)
            '''Display the label for first name'''
            lfname = Label(root, text="First Name")
            lfname.place(x=20, y=210)
            fname = Label(root, bg='white', width=50, text=i[3], anchor='w')
            fname.place(x=100, y=210)
            '''Display the label for last name'''
            llname = Label(root, text="Last Name")
            llname.place(x=20, y=240)
            lname = Label(root, bg='white', width=50, text=i[4], anchor='w')
            lname.place(x=100, y=240)
            '''Display the label for E-Mail ID'''
            lemail = Label(root, text="E-Mail ID")
            lemail.place(x=20, y=270)
            email = Label(root, bg='white', width=50, text=i[5], anchor='w')
            email.place(x=100, y=270)
            '''Display the phone number'''
            lphone = Label(root, text="Phone No.")
            lphone.place(x=20, y=300)
            phone = Label(root, bg='white', width=50, text=i[6], anchor='w')
            phone.place(x=100, y=300)

        # create button for show habits
        habit_button = Button(root, text='Show Habits', font='bold', width=10, height=1, fg='white', bg='green',
                              command=self.DHabits)
        # add button to the window
        habit_button.place(x=100, y=350)

        # create button to close the current window
        exit_button = Button(root, text='Exit', width=10, height=1, font='bold', fg='white', bg='green',
                             command=root.destroy)
        # add exit button
        exit_button.place(x=250, y=350)

        # close the connection
        conn.close()
        # close the mainloop
        root.mainloop()


# create the object using class
ht = habit_tracker("test.db")
# call the tracker method using the object
ht.tracker()

