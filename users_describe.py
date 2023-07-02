import sqlite3

def users_table_description(db_name:str) -> int:
    print(db_name)
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    # it will display the column information of the table named 'users'
    c.execute("PRAGMA TABLE_INFO('users')")
    users_table_definition = c.fetchall()

    # user must have these columns in the users table
    columns = [(0, 'id', 'INTEGER', 0, None, 1), (1, 'title', 'TEXT', 0, None, 0),
               (2, 'first_name', 'TEXT', 1, None, 0), (3, 'last_name', 'TEXT', 1, None, 0),
               (4, 'mail_id', 'TEXT', 0, None, 0), (5, 'phone_number', 'TEXT', 1, None, 0),
               (6, 'created_on', 'TEXT', 1, None, 0)]

    # close the connection
    conn.close()

    # check whether they are equal
    if users_table_definition == columns:
       return (1)

