import sys
import os 

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class SoftwareDevelopment(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("KasMek, LLC - Software Development")
        self.setStyleSheet("background-color : yellow")
        self.showMaximized()