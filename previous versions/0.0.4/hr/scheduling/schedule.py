import sys
import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ScheduleSystem(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("KasMek, LLC - Human Resources Scheduling")
        self.setStyleSheet("background-color : pink")
        self.UiComponents()
        self.showMaximized()

    def UiComponents():

        pass