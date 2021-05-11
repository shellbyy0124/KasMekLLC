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
    
    def UiComponents(self):

        self.h_r = QPushButton("Human\nResources", self)
        self.h_r.setGeometry(200, 100, 100, 50)
        self.h_r.setStyleSheet("border : 1px solid green; color : green")