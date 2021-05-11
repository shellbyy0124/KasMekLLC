import sys
import os

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from human_resources.employees.addemp import AddEmployee
from human_resources.application_stuff.application import Application
from human_resources.application_stuff.updatingOpportunities import UpdateOpportunitiesJson
from human_resources.employees.addemp import AddEmployee
from human_resources.employees.rememp import RemEmployee

class HumanResourcesScreen(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("KasMek, LLC - Human Resources")
        self.setStyleSheet("background-color : orange")
        self.UiComponents()
        self.showMaximized()

    def UiComponents(self):

        button = QPushButton("Hire Employee", self)
        button.setGeometry(100, 100, 120, 50)
        button.setStyleSheet("border : 1px solid black; color : black")
        button.clicked.connect(self.hire_emp)

        button = QPushButton("Fire Employee", self)
        button.setGeometry(100, 150, 120, 50)
        button.setStyleSheet("border : 1px solid black; color : black")
        button.clicked.connect(self.fire_emp)

        button = QPushButton("Edit Employee", self)
        button.setGeometry(100, 200, 120, 50)
        button.setStyleSheet("border : 1px solid black; color : black")
        button.clicked.connect(self.edit_emp)

        button = QPushButton("View All\nEmployees", self)
        button.setGeometry(100, 250, 120, 50)
        button.setStyleSheet("border : 1px solid black; color : black")
        button.clicked.connect(self.show_all_emp)

    def hire_emp(self):

        self.w = AddEmployee()
        self.w.showMaximized()

    def fire_emp(self):

        self.w = RemEmployee()
        self.w.showMaximized()

    def edit_emp(self):

        pass

    def show_all_emp(self):

        pass