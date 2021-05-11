import subprocess
import sys
import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Accounting.payroll import PayrollScreen
from Accounting.timeclock.TimeSheets.clock import ClockSystem
from human_resources.hr_screen import HumanResourcesScreen
from SoftwareDevelopment.development import SoftwareDevelopment
from human_resources.application_stuff.application import Application

class MainScreen(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("KasMek, LLC - Home Screen")
        self.setStyleSheet("background-color : green")
        self.UiComponents()
        self.showMaximized()

    def UiComponents(self):

        button = QPushButton("Accounting", self)
        button.setGeometry(100, 100, 100, 50)
        button.clicked.connect(self.accounting)

        button = QPushButton("Human\nResources", self)
        button.setGeometry(300, 100, 100, 50)
        button.clicked.connect(self.hresources)

        button = QPushButton("Software\nDevelopment/\nSoftware\nEngineering", self)
        button.setGeometry(500, 100, 100, 50)
        button.clicked.connect(self.SoftwareDevelopment)

        button = QPushButton("Application\n(in house)", self)
        button.setGeometry(300, 200, 100, 50)
        button.clicked.connect(self.application)

        button = QPushButton("Print Paper\nApplication", self)
        button.setGeometry(300, 300, 100, 50)
        button.clicked.connect(self.print_application)

        button = QPushButton("Clock In/Out", self)
        button.setGeometry(0, 0, 100, 50)
        button.clicked.connect(self.clockIn)

        button = QPushButton("Exit", self)
        button.setGeometry(300, 600, 100, 100)
        button.clicked.connect(self.exit_button)

    def application(self):

        self.w = Application()
        self.w.showMaximized()

    def print_application(self):

        filepath = '/home/shellbyy/Desktop/KasMekLLC/human_resources/application_stuff/application.txt'

        subprocess.call(('xdg-open', filepath))

    def SoftwareDevelopment(self):

        self.w = SoftwareDevelopment()
        self.w.showMaximized()

    def hresources(self):

        self.w = HumanResourcesScreen()
        self.w.showMaximized()

    def accounting(self):

        self.w = PayrollScreen()
        self.w.showMaximized()

    def clockIn(self):

        self.w = ClockSystem()
        self.w.showMaximized()

    def exit_button(self):

        App = QApplication(sys.argv)
        sys.exit(App.exec_())

App = QApplication(sys.argv)
window = MainScreen()
sys.exit(App.exec_())