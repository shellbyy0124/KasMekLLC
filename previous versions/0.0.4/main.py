import os
import sqlite3
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Accounting.timeclock.TimeSheets.clock import ClockSystem
from CyberSecurity.Supervisor.cybermain import CyberSecurityMainScreen

"""
VERSION 0.0.2 AND 0.0.4 ARE NO LONGER COMPATIBLE WITH THE SOFTWARE. VERSION 0.0.6
WILL CONTAIN A WHOLE NEW LAYOUT, NEW FILE NAMES, AND COLOR SCHEMES
"""

class MainScreen(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("KasMek, LLC - Home Scree")
        self.setStyleSheet("background-color : tan")
        self.UiComponents()
        self.showMaximized()

    def UiComponents(self):

        self.mainlabel = QLabel("Employee Functions:", self)
        self.mainlabel.setWordWrap(False)
        self.mainlabel.setGeometry(100, 100, 147, 50)
        self.mainlabel.setStyleSheet("border : 1px solid green; color : black")

        self.secondndmainlabel = QLabel("CEO Functions", self)
        self.secondndmainlabel.setWordWrap(False)
        self.secondndmainlabel.setGeometry(300, 100, 147, 50)
        self.secondndmainlabel.setStyleSheet("border : 1px solid green; color : black")

        self.clockbutton = QPushButton("Clock In/Out", self)
        self.clockbutton.setGeometry(125, 155, 100, 50)
        self.clockbutton.setStyleSheet("border : 1px solid green; color : black")
        self.clockbutton.clicked.connect(self.clockSystem)

        self.cyberbutton = QPushButton("Cyber Security\nDepartment", self)
        self.cyberbutton.setGeometry(325, 155, 100, 50)
        self.cyberbutton.setStyleSheet("border : 1px solid green; color : black")
        self.cyberbutton.clicked.connect(self.cyber_department)

        self.appbutton = QPushButton("Want To Become An\nEmployee? Click Here", self)
        self.appbutton.setGeometry(600, 600, 200, 100)
        self.appbutton.setStyleSheet("border : 1px solid black; background-color : purple; color : blue")
        self.appbutton.clicked.connect(self.application_button)

        self.exitbutton = QPushButton("Exit System", self)
        self.exitbutton.setGeometry(300, 600, 100, 50)
        self.exitbutton.setStyleSheet("border : 1px solid green; color : black")
        self.exitbutton.clicked.connect(self.exit_button)

    def application_button(self):

        file = '/home/shellbyy/Desktop/KasMekLLC/application_stuff/application.txt'
        os.open(file, "r")

    def cyber_department(self):

        self.w = CyberSecurityMainScreen()
        self.w.showMaximized()

    def clockSystem(self):

        self.w = ClockSystem()
        self.w.showMaximized()

    def exit_button(self):

        App = QApplication(sys.argv)
        sys.exit(App.exec_())

App = QApplication(sys.argv)
window = MainScreen()
sys.exit(App.exec_())