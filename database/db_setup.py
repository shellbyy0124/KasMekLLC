# import sqlite3

# with sqlite3.connect('kasmek.db') as db:

#     cursor = db.cursor()

#     cursor.execute('''CREATE TABLE IF NOT EXISTS employees
#         (ID PRIMARY_KEY INT,
#         NAME TEXT,
#         PASSWORD TEXT,
#         JOB_TITLE TEXT);''')

#     db.commit()

#     cursor.execute('INSERT INTO employees (ID, NAME, PASSWORD, JOB_TITLE) \
#         VALUES (1, "Shellbyy", "whynot123", "CEO");')

#     cursor.execute('INSERT INTO employees (ID, NAME, PASSWORD, JOB_TITLE) \
#         VALUES (2, "Kastien", "testing123", "CFO");')

#     db.commit()

#     cursor.execute('SELECT * FROM employees')

#     result = cursor.fetchall()

#     print(result)

#     cursor.close()

import sqlite3

conn = sqlite3.connect('kasmek.db')