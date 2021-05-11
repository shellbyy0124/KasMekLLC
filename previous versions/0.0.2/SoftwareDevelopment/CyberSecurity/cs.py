import sys
import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class CyberSecurityDevelopment(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("KasMek, LLC - Cyber Security Development")
        self.setStyleSheet("background-color : red")
        self.showMaximized()