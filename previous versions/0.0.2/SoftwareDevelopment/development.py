import sys
import os 

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from SoftwareDevelopment.back_end.backend import BackEndDevelopment
from SoftwareDevelopment.CyberSecurity.cs import CyberSecurityDevelopment
from SoftwareDevelopment.SoftwareEngineer.se import SoftwareDevelopment

class Development(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("KasMek, LLC - Software Development/Engineering Screen")
        self.setStyleSheet("background-color : indigo")
        self.showMaximized()