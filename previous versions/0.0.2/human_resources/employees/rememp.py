import json
import sys
import os
import datetime

from datetime import datetime

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class RemEmployee(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("KasMek, LLC - Remove Employee Screen")
        self.setStyleSheet("background-color : #EE82EE")
        self.UiComponents()
        self.showMaximized()

    def UiComponents(self):

        self.file_name = datetime.today().__format__('%m_%d_%y')
        
        self.label = QLabel("Please Choose A Deparment:", self)
        self.label.setWordWrap(False)
        self.label.setGeometry(300, 300, 200, 50)
        self.label.setStyleSheet("border : 1px solid black; color : black")

        self.box = QComboBox(self)
        self.box.setGeometry(300, 400, 200, 50)
        self.box.setStyleSheet("border : 1px solid black; background-color : white; color : black")

        with open(f'{self.file_name}.json', 'r', encoding='utf-8-sig') as f:
            data = json.load(f)

        for emp_id in data.keys():

            emp_dep = data[emp_id]["job_title"]
            self.box.addItems(emp_dep)

        self.box.currentTextChanged.connect(self.next_sec)

    def next_sec(self):

        self.label = QLabel("To pull up an employee, please enter only the Employee ID Number (EIN)", self)
        self.label.setWordWrap(True)
        self.label.setGeometry(100, 100, 400, 50)
        self.label.setStyleSheet("border : 1px solid black; background-color : #add8e6; color : black")
        self.label.show()

        self.line1 = QLineEdit(self)
        self.line1.setGeometry(100, 300, 200, 50)
        self.line1.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.line1.show()

        self.button = QPushButton("Search", self)
        self.button.setGeometry(100, 400, 100, 50)
        self.button.clicked.connect(self.search_emp)
        self.button.show()

        self.button2 = QPushButton("Back", self)
        self.button2.setGeometry(250, 400, 100, 50)
        self.button2.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.button2.clicked.connect(self.back_button)

    def back_button(self):
        self.hide()

    def search_emp(self):

        with open(f'{self.file_name}.json', 'r', encoding='utf-8-sig') as f:
            data = json.load(f)

        while self.line1.text() not in data.keys():

            self.label_error = QLabel("This EIN doesn't match our records. Please double check the EIN entered, or have the employee double check their email to ensure that they have the correct EIN", self)
            self.label_error.setWordWrap(True)
            self.label_error.setGeometry(300, 300, 200, 300)
            self.label_error.setStyleSheet("border : 1px solid red; color : red")
            self.label_error.show()
            break

        else:

            self.label.hide()
            self.line1.hide()
            self.button.hide()

            self.name_use = data[self.line1.text()]["emp_name"]

            self.name = QLabel(f'{self.name_use}', self)
            self.name.setWordWrap(False)
            self.name.setGeometry(400, 100, 150, 50)
            self.name.setStyleSheet("border : 1px solid blue; color : silver")
            self.name.show()

            emp_info = []

            for info in data[self.line1.text()].keys():

                if info == "employee_name":

                    pass

                elif info != "employee_name":

                    emp_info.append(info)

            for i in range(len(emp_info)):
                height = i+250
                width = i+250

            self.detailes = QLabel(f'{emp_info}', self)
            self.details.setWordWrap(True)
            self.details.setGeometry(400, 150, width, height)
            self.details.show()