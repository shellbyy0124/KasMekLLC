import sys
import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class BackEndDevelopment(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("KasMek, LLC - Back End Developement")
        self.setStyleSheet("background-color : orange")
        self.showMaximized()