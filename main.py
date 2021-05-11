"""
YOU WILL NEED TO GO TO THE MODULES FOLDER, CEO FOLDER, CEO.PY AND REMOVE THE BOTTOM 3 LINES.
I AM LEAVING THE MAIN.PY FILE ALONE AS I CANNOT FIGURE OUT THE ERROR WITH LINE 100
"""
import sqlite3
import sys

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
# from modules.Ui_window_creator import Ui_mainWindow
from modules.CEO.ceo import ChiefExecOfficer

# insert Ui_mainWindow, QMainWindow into class MainWindow() instead of just class MainWindow(QMainWindow):
class MainWindow(QMainWindow):
    
    def __init__(self):

        super().__init__() # change to super(MainWindow, self).__init__()

        """COMMENT OUT THE NEXT 4 LINES IF USING THE COMMENTED OUT CODE BELOW..."""

        self.setWindowTitle("KasMek, LLC - Login") # remove this
        self.setStyleSheet("background : black") # remove this
        self.UiComponents() # remove this
        self.showMaximized() # remove this
        self.check = [] # keep this but move to another file for login system along with lines 51-102. Those are the login verification ~~ KasMekLLC/modules/cyber/login_sec/login.py

        """
        UNCOMMENT THE NEXT 4 LINES BELOW
        """
    
        # super(MainWindow, self).__init__()

        # self.setupUi(self)

        # self.button_exit.clicked.connect(self.exit_button)
        # self.button_login.clicked.connect(self.switch)

    def UiComponents(self): # remove this. Uncomment the import at the top to utilize the Ui_mainWindow for the login screen entry information for the user. see ./modules/Ui_login.py

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

    """
    FROM HERE TO LINE 102 IS THE LOGIN VERIFICATION CODE USING A DATABASE. I DO NOT KNOW IF THIS WORKS, BECAUSE WE ARE NOT SUPPOSED TO USE F-STRING WITH DATABASES BUT I DO NOT KNOW
    ANOTHER WAY TO DO IT. IT'S TAKING THE JOB TITLE OF THE EMPLOYEE, AND THEN MATCHING THAT JOB TITLE TO A jobs TABLE IN THE DATABASE. ONCE IT MATCHES ONE, IT IS SUPPOSED TO OPEN THE CORRESPONDING SCREEN
    THAT IS PERTINENT TO THAT JOB TITLE
    """

    def check_id(self):

        conn = sqlite3.connect('kasmek.db')

        check_id = conn.execute('SELECT id FROM employees where ID = ?')

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

        sql = 'SELECT password FROM employees where ID = ?'
        vals = (id,)

        check_pw = conn.execute(sql, vals)

        if self.pw_entry.text() != check_pw:

            self.error_pw = QLabel("That password does not match our records. Try Again!", self)
            self.error_pw.setWordWrap(False)
            self.error_pw.setGeometry(600, 150, 300, 50)
            self.error_pw.setStyleSheet("border : 1px solid red; color : red")
            self.error_pw.show()

        else:

            self.check.append("Yes")
            self.continu()

    """
    THIS FUNCTION IS DESIGNED TO START THE SCREEN EXCHANGE. THIS FUNCTION NEEDS TO BE MOVED TO THE MANAGER.PY FILE IN THE MAIN FILE (KASMEKLLC). THE PURPOSE OF THIS FUNCTION IS TO TAKE
    THE JOB TITLE OF THE EMPLOYEE AND MATCH IT TO A JOB TITLE WITHIN THE JOBS TABLE OF THE DATABASE, AND THEN OPEN THE SCREEN THAT IS CORRESPONDENT TO THAT JOB TITLE. I HAVE ALREADY CREATED
    A CEO FOLDER WITH A CEO.PY FILE TO START THE HOME SCREEN FROM THERE. I WILL BE GOING BACK AND CREATING OTHER .PY FILES TO HAVE AT LEAST ONE .PY FILE FOR EACH JOB TITLE SO THAT WHEN I UPDATE
    TO THE REPO AGAIN, YOU ALL CAN SEE WHAT DIRECTION I AM HEADED IN WITH THIS PROJECT. DO REMEMBER THAT I AM NOT ALONE IN THIS PROJECT. WITHIN THE PROGRAMMING TEAM WORKING ON THIS PROJECT IS MYSELF,
    KATAREBORN, AND DISCORD USER gamingbuddhist#9599.
    """

    """
    I HAVE COMMENTED OUT THE ABOVE PARAGRAPHS DESCRIPTION CODE BELOW SO THAT I CAN WRITE THE CODE THE WAY THAT I KNOW HOW FOR RIGHT NOW"""

    def continu(self):

        check_list = ["Yes", "Yes"]

        if self.check == check_list:

            self.button_login.setEnabled(True)
            self.button_login.clicked.connect(self.next_window)
        
        else:

            self.UiComponents()

        # conn = sqlite3.connect('kasmek.db')

        # cursor = conn.cursor()

        # job_title = cursor.execute(f'SELECT job_title FROM employees where ID = {int(self.id_entry.text())}')

        # if job_title == "CEO":

        #     self.w = None

        # else:

        #     pass

    def next_window(self):

        self.w = ChiefExecOfficer()
        self.w.showMaximized()

    def exit_button(self):

        self.close()

"""
UNCOMMENT THE BELOW LINE IF GOING WITH VERSION TWO OF THIS CODE. The version that is commented out at the top with instructions on what to do with it.
"""

# if __name__ == '__main__':

#     App = QApplication(sys.argv)
#     window = MainWindow()
#     window.showMaximized()
#     sys.exit(App.exec_())

"""
DELETE ABOVE AND KEEP BELOW IF GOING WITH VERSION ONE OF THIS CODE
"""
App = QApplication(sys.argv)
window = MainWindow()
sys.exit(App.exec_())