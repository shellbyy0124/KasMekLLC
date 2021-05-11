import sqlite3
import sys

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from modules.CEO.ceo import ChiefExecOfficer

class LoginSystem(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("KasMek, LLC - Login")
        self.setStyleSheet("background-color : black")
        self.UiComponents()

    def UiComponents(self):

            self.id_num = QLabel("Employee ID:", self)
            self.id_num.setWordWrap(False)
            self.id_num.setGeometry(300, 100, 150, 50)
            self.id_num.setStyleSheet("border : 1px solid green; color : green; text-decoration : underline")

            self.id_entry = QLineEdit(self)
            self.id_entry.setGeometry(450, 100, 150, 50)
            self.id_entry.setStyleSheet("border : 1px solid green; color : black")
            self.id_entry.editingFinished.connect(self.check_id)

            self.pw_label = QLabel("Employee PW:", self)
            self.pw_label.setWordWrap(False)
            self.pw_label.setGeometry(300, 150, 150, 50)
            self.pw_label.setStyleSheet("border : 1px solid green; color : green; text-decoration : underlind")

            self.pw_entry = QLineEdit(self)
            self.pw_entry.setGeometry(450, 150, 150, 50)
            self.pw_entry.setStyleSheet("border : 1px solid green; color : black")
            self.pw_entry.editingFinished.connect(self.check_pw)

            self.button_exit = QPushButton("Exit", self)
            self.button_exit.setGeometry(300, 300, 100, 50)
            self.button_exit.setStyleSheet("border : 1px solid green; color : green; text-decoration : underline")
            self.button_exit.clicked.connect(self.exit_button)

            self.button_login = QPushButton("Login", self)
            self.button_login.setGeometry(450, 300, 100, 50)
            self.button_login.setStyleSheet("border : 1px solid green; color : green; text-decoration : underline")
            self.button_login.setEnabled(False)

    def check_id(self):

        conn = sqlite3.connect('kasmek.db')
        cursor = conn.cursor()
        sql = 'SELECT id FROM employees where ID = ?'
        vals = (id,)
        cursor.execute(sql, vals)
        check_id = cursor.fetchone()

        if int(self.id_entry.text()) != check_id:

            self.error_id = QLabel("That ID does not match our records. Try Again!", self)
            self.error_id.setWordWrap(False)
            self.error_id.setGeometry(600, 100, 300, 50)
            self.error_id.setStyleSheet("border : 1px solid red, color : red")
            self.error_id.show()

        else:

            self.check.append("Yes")

    def check_pw(self):

        conn = sqlite3.connect('kasmek.db')
        cursor = conn.cursor()
        sql = 'SELECT id FROM employees WHERE id = ?'
        vals = (id,)
        cursor.execute(sql, vals)
        check_pw = cursor.fetchone()

        if self.pw_entry.text() != check_pw:

            self.error_pw = QLabel("That password does not match our records. Try Again!", self)
            self.error_pw.setWordWrap(False)
            self.error_pw.setGeometry(600, 150, 300, 50)
            self.error_pw.setStyleSheet("border : 1px solid red; color : red")
            self.error_pw.show()

        else:

            self.check.append("Yes")
            self.continu()

    def continu(self):

        check_list = ["Yes", "Yes"]

        if self.check == check_list:

            self.button_login.setEnabled(True)
            self.button_login.clicked.connect(self.next_window)

            conn = sqlite3.connect('kasmek.db')
            cursor = conn.cursor()
            sql = 'SELECT job_title FROM employees where id = ?'
            vals = (id,)
            cursor.execute(sql, vals)
            job_title = cursor.fetchone()

            if job_title == "CEO":

                self.w = None

            else:

                pass
        
        else:

            self.UiComponents()

        

App = QApplication(sys.argv)
window = LoginSystem()
sys.exit(App.exec_())