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

from KasMekLLC.previous_versions.V0_0_6.modules.cyber.login_security.login import LoginSystem

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

        """
        UNCOMMENT THE NEXT 4 LINES BELOW
        """
    
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