import datetime
import sqlite3
import sys

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2. QtWidgets import *
from datetime import datetime

class TimeSystem(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("KasMek, LLC - Time Clock")
        self.setStyleSheet("background-color : black")
        self.UiComponents()
        self.check = []

    def UiComponents(self):

        label_one = QLabel("Employee ID:", self)
        label_one.setWordWrap(False)
        label_one.setGeometry(300, 100, 100, 50)
        label_one.setStyleSheet("border : 1px solid green; color : green; text-decoration : underline")

        self.id_entry = QLineEdit(self)
        self.id_entry.setGeometry(450, 100, 100, 50)
        self.id_entry.setStyleSheet("border : 1px solid green; color : green")
        self.id_entry.editingFinished.connect(self.check_id)

        label_two = QLabel("Employee PW:", self)
        label_two.setWordWrap(False)
        label_two.setGeometry(300, 150, 100, 50)
        label_two.setStyleSheet("border : 1px solid green; color : green; text-decoration : underline")

        self.pw_entry = QLineEdit(self)
        self.pw_entry.setGeometry(450, 150, 100, 50)
        self.pw_entry.setStyleSheet("border : 1px solid green; color : green")
        self.pw_entry.editingFinished.connect(self.check_pw)

        self.button_exit = QPushButton("Exit", self)
        self.button_exit.setGeometry(300, 300, 100, 50)
        self.button_exit.setStyleSheet("border : 1px solid green; color : green; text-decoration : underline")
        self.button_exit.clicked.connect(self.exit_button)

        self.button_clock = QPushButton("Clock In", self)
        self.button_clock.setGeometry(450, 300, 100, 50)
        self.button_clock.setStyleSheet("border : 1px solid green; color : gree; text-decoration : underline")
        self.button_clock.clicked.connect(self.exit_button)

    def check_id(self):

        conn = sqlite3.connect('kasmek.db')
        cursor = conn.cursor()
        sql = 'SELECT id FROM employees where id = ?'
        vals = (int(self.id_entry.text()),)
        cursor.execute(sql, vals)
        emp_id = cursor.fetchone()

        if int(self.id_entry.text()) == emp_id:

            self.check.append("Yes")

        else:
            count = 0

            while count < 3:

                count += 1
                
                self.error_id = QLabel("That ID does not match our records. Try Again!", self)
                self.error_id.setWordWrap(False)
                self.error_id.setGeometry(600, 100, 300, 50)
                self.error_id.setStyleSheet("border : 1px solid red; color : red")
                self.error_id.show()

            else:

                self.check.append("Yes")

    def check_pw(self):

        conn = sqlite3.connect('kasmek.db')
        cursor = conn.cursor()
        sql = 'SELECT password from EMPLOYEES where id = ?'
        vals = (int(self.id_entry.text()),)
        cursor.execute(sql, vals)
        emp_pw = cursor.fetchone()

        if self.pw_entry.text() == emp_pw:

            self.check.append("Yes")
            self.final_check()

        else:

            count = 0

            while count < 3:

                count += 1

                self.error_pw = QLabel("That password does not match our system. Try Again!", self)
                self.error_pw.setWordWrap(False)
                self.error_pw.setGeometry(600, 150, 300, 50)
                self.error_pw.setStyleSheet("border : 1px solid red; color : red")
                self.error_pw.show()

            else:

                self.check.append("Yes")
                self.final_check()
    
    def final_check(self):

        check_me = ["Yes", "Yes"]

        try:

            if self.check == check_me:

                conn = sqlite3.connect('kasmek.db')
                cursor = conn.cursor()
                now = datetime.datetime.today().__format__('%m_%d_%y %H:%M:%S')
                sql = 'UPDATE employees SET time_in = {} where id = ?'.__format__(str(now))
                vals = (id,)
                cursor.execute(sql, vals)
                cursor.commit()
                cursor.close()
                conn.close()

                conn = sqlite3.connect('kasmek.db')
                cursor = conn.cursor()
                sql = 'SELECT name FROM  employees where id = ?'
                vals = (id,)
                cursor.execute(sql, vals)
                emp_name = cursor.fetchone()

                self.confirm = QLabel(f"Time Punch For, {emp_name}, was successfull!", self)
                self.confirm.setWordWrap(False)
                self.confirm.setGeometry(300, 400, 250, 50)
                self.confirm.setStyleSheet("border : 1px solid green; color : green; text-decoration : underline")
                self.confirm.show()
        
        except Exception as e:

            print("Error:", e)