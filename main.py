import sqlite3
import sys, os

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
# from modules.Ui_window_creator import Ui_mainWindow

from modules.cyber.login_security.login import LoginSystem

# insert Ui_mainWindow, QMainWindow into class MainWindow() instead of just class MainWindow(QMainWindow):

class MainWindow(QMainWindow):
    
    def __init__(self):

        super().__init__() # change to super(MainWindow, self).__init__()

        """
        REMOVE THE NEXT 4 LINES IF USING THE COMMENTED OUT CODE BELOW
        """

        self.setWindowTitle("KasMek, LLC - Login") # remove this
        self.setStyleSheet("background : black") # remove this
        self.UiComponents() # remove this
        self.showMaximized() # remove this
        self.check = [] # keep this but move to another file for login system along with lines 51-102. Those are the login verification ~~ KasMekLLC/modules/cyber/login_sec/login.py
    
        # super(MainWindow, self).__init__()

        # self.setupUi(self)

        # self.button_exit.clicked.connect(self.exit_button)
        # self.button_login.clicked.connect(self.switch)

    def UiComponents(self):

        button_login = QPushButton("Login", self)
        button_login.setGeometry(500, 500, 100, 50)
        button_login.setStyleSheet("border : 1px solid green; color : green; text-decoration : underline")
        button_login.clicked.connect(self.next_window)

    def next_window(self):

        self.w = LoginSystem()
        self.w.showMaximized()

    def exit_button(self):

        self.close()

App = QApplication(sys.argv)
window = MainWindow()
sys.exit(App.exec_())