import sqlite3

def habit_completion_table_description(db_name:str) -> int:
    print(db_name)
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    # it will display the column information of the table named 'habit_completion'
    c.execute("PRAGMA TABLE_INFO('habit_completion')")
    habit_completion_table_definition = c.fetchall()

    # user must have these columns in the users table
    columns = [(0, 'id', 'INTEGER', 0, None, 1),
               (1, 'habit_id', 'INTEGER', 1, None, 0),
               (2, 'completion_status', 'INTEGER', 1, None, 0),
               (3, 'created_on', 'TEXT', 1, None, 0)]

    # close the connection
    conn.close()

    # check whether they are equal
    if habit_completion_table_definition == columns:
       return (1)

