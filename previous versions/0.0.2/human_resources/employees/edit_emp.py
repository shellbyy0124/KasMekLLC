import sys
import os
import json

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class EditEmployee(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("KasMek, LLC - Edit Employee Screen")
        self.setStyleSheet("background-color : purple")
        self.UiComponents()
        self.showMaximized()

    def UiComponents(self):

        self.path = '/home/shellbyy/Desktop/KasMekLLC/jsonFiles/employees.json'

        with open(f'{self.path}', 'r', encoding='utf-8-sig') as f:
            data = json.load(f)

        self.label = QLabel("Please Select An Employee:", self)
        self.label.setWordWrap(False)
        self.label.setGeometry(100, 100, 100, 50)
        self.label.setStyleSheet("border : 1px solid black; color : black")
        
        self.box = QComboBox(self)
        self.box.setGeometry(100, 150, 200, 50)
        self.box.setStyleSheet("border : 1px solid black; background-color : silver; color : black")

        employee_names = []

        for emp_id in data.keys():

            emp_name = data[emp_id]["employee_name"]
            employee_names.append(emp_name)
        
        self.box.addItems(employee_names)
        
        self.button = QPushButton("Back", self)
        self.button.setGeometry(300, 600, 100, 50)
        self.button.clicked.connect(self.back_button)

        self.button = QPushButton("Next", self)
        self.button.setGeometry(500, 600, 100, 50)
        self.button.clicked.connect(self.show_emp)

    def show_emp(self):

        self.label.hide()
        self.box.hide()
        self.button.hide()

        with open(f'{self.path}', 'r', encoding='utf-8-sig') as g:
            data = json.load(g)

        self.label2 = QLabel(f"Employee Name: {data[self.box.currentText()]['employee_name']}", self)
        self.label2.setWordWrap(False)
        self.label2.setGeometry(100, 100, 800, 50)
        self.label2.setStyleSheet("border : 1px solid black; color : black")
        self.label2.show()

        information = []

        for info in data[self.box.currentText()].keys():

            information.append(info)

        self.back_button()

    def back_button(self):

        self.hide()