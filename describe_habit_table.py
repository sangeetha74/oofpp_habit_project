import sqlite3

def habit_table_description(db_name:str) -> int:
    print(db_name)
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    # it will display the column information of the table named 'habit'
    c.execute("PRAGMA TABLE_INFO('habit')")
    habit_table_definition = c.fetchall()

    # user must have these columns in the users table
    columns = [(0, 'id', 'INTEGER', 0, None, 1),
           (1, 'habit_name', 'TEXT', 0, None, 0),
           (2, 'sun', 'INTEGER', 1, None, 0),
           (3, 'mon', 'INTEGER', 1, None, 0),
           (4, 'tue', 'INTEGER', 1, None, 0),
           (5, 'wed', 'INTEGER', 1, None, 0),
           (6, 'thu', 'INTEGER', 1, None, 0),
           (7, 'fri', 'INTEGER', 1, None, 0),
           (8, 'sat', 'INTEGER', 1, None, 0),
           (9, 'habit_status', 'TEXT', 1, None, 0),
           (10, 'users_id', 'INTEGER', 1, None, 0),
           (11, 'created_on', 'TEXT', 1, None, 0)]

    # close the connection
    conn.close()

    # check whether they are equal
    if habit_table_definition == columns:
       return (1)

