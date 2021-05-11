import sqlite3
import sys

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class ChiefExecOfficer(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("KasMek, LLC - CEO Station")
        self.setStyleSheet("background-color : black")
        self.UiComponents()
        self.showMaximized()
    
    def UiComponents(self):

        self.h_r = QPushButton("Human\nResources", self)
        self.h_r.setGeometry(200, 100, 100, 50)
        self.h_r.setStyleSheet("border : 1px solid green; color : green; text-decoration : underline")
        self.h_r.clicked.connect(self.human_resources)

        self.acct = QPushButton("Accounting", self)
        self.acct.setGeometry(350, 100, 100, 50)
        self.acct.setStyleSheet("border : 1px solid green; color : green; text-decoration : underline")
        self.acct.clicked.connect(self.accounting)

        self.timeclock = QPushButton("Time\nClock", self)
        self.timeclock.setGeometry(200, 150, 100, 50)
        self.timeclock.setStyleSheet("border : 1px solid green; color : green; text-decoration : underline")
        self.timeclock.clicked.connect(self.time_clock)

        self.s_d = QPushButton("Software Development\Department", self)
        self.s_d.setGeometry(350, 150, 100, 50)
        self.s_d.setStyleSheet("border : 1px solid green; color : green; text-decoration : underline")
        self.s_d.clicked.connect(self.software_dept)

        self.c_s = QPushButton("Cyber\nSecurity", self)
        self.c_s.setGeometry(200, 200, 100, 50)
        self.c_s.setStyleSheet("border : 1px solid green; color : green; text-decoration : underline")
        self.c_s.clicked.connect(self.cyber_sec)

    def human_resources(self):

        pass

    def accounting(self):

        pass

    def time_clock(self):

        pass

    def software_dept(self):

        pass

    def cyber_sec(self):

        pass


App = QApplication(sys.argv)
window = ChiefExecOfficer()
sys.exit(App.exec_())