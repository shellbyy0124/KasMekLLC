import sqlite3


database = 'Data/Databases/kasmec.db'


def create_test_tables():
    with sqlite3.connect(database) as db:
        cursor = db.cursor()
        cursor.execute('''
                  CREATE TABLE IF NOT EXISTS employees(
                  id TEXT,
                  name TEXT,
                  pass TEXT,
                  job TEXT
                  )
               ''')
        db.commit()
        cursor.close()

def create_test_user_data(data_list):
    with sqlite3.connect(database) as db:
        cursor = db.cursor()
        for x in data_list:
            sql = ("SELECT name FROM employees WHERE ID = ?")
            val = (x[0],)
            exists = cursor.execute(sql, val).fetchone()
            if exists:
                continue
            else:
                sql = ("INSERT INTO employees(id, name, pass, job) VALUES(?,?,?,?)")
                vals = x
                cursor.execute(sql, vals)
        db.commit()
        cursor.close()


def fetch_employee(id):
    with sqlite3.connect(database) as db:
        cursor = db.cursor()
        sql = ("SELECT id, name, pass, job FROM employees WHERE ID = ?")
        val = (id,)
        employee = cursor.execute(sql, val).fetchone()
        cursor.close()
        return employee
