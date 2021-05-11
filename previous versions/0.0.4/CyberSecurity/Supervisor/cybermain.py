import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from hr.scheduling.schedule import ScheduleSystem

class CyberSecurityMainScreen(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("KasMek, LLC - Cyber Security Department")
        self.setStyleSheet("background-color : red")
        self.UiComponents()
        self.showMaximized()

    def UiComponents(self):

        label = QLabel("Employee Functions", self)
        label.setWordWrap(False)
        label.setGeometry(100, 100, 150, 50)
        label.setStyleSheet("border : 1px solid gray; color : blue")

        button = QPushButton("Schedule", self)
        button.setGeometry(125, 155, 100, 50)
        button.setStyleSheet("border : 1px solid purple; color : blue")
        button.clicked.connect(self.show_schedule)

        exitbutton = QPushButton("Exit System", self)
        exitbutton.setGeometry(300, 600, 100, 50)
        exitbutton.setStyleSheet("border : 1px solid green; color : black")
        exitbutton.clicked.connect(self.exit_button)

    def show_schedule(self):

        self.w = ScheduleSystem()
        self.w.showMaximized()

    def exit_button(self):

        App = QApplication(sys.argv)
        sys.exit(App.exec_())