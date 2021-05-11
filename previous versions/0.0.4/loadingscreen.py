import sys
import os
import json
import random

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class LoadingScreen(QMainWindow):

    def __init__(self):

        super().__init__()

        self.timeToCount = 15
        self.setWindowTitle("Please Wait")
        self.setStyleSheet("background-color : blue")
        self.showMaximized()
        
        with open('/home/shellbyy/Desktop/KasMekLLC/jsonFiles/quotes.json', 'r', encoding='utf-8-sig') as f:
            data = json.load(f)

        number = random.randint(0, 19)

        inspirational_quotes = data["Quotes"][str(number)]

        label = QLabel(f"{inspirational_quotes}", self)
        label.setGeometry(50, 100, 100, 500)
        label.setWordWrap(False)
        label.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        label.show()

        self.label = QLabel(f"Please Wait While We Work On Your Request. . .{self.timeToCount}s", self)
        self.label.setGeometry(50, 50, 400, 50)
        self.label.setWordWrap(False)
        self.label.setStyleSheet("border : 1px solid black; background-color : siler; color : black")
        self.label.show()

        timer = QTimer(self)
        timer.timeout.connect(self.time)
        timer.start(1000)
        
    def time(self):
        
        self.timeToCount -= 1
        self.label.setText(f"Please Wait While We Work On Your Request. . .{self.timeToCount}s")

        if self.timeToCount == 0:
        
            self.hide()