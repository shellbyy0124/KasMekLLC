import json
import sys
import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class AddEmployee(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("KasMek, LLC - Add Employee")
        self.setStyleSheet("background-color : blue")
        self.UiComponents()
        self.showMaximized()

    def UiComponents(self):

        with open('/home/shellbyy/Desktop/KasMekLLC/jsonFiles/applications.json', 'r', encoding='utf-8-sig') as applicant:
            data = json.load(applicant)

        label = QLabel("Select Applicant:", self)
        label.setWordWrap(False)
        label.setGeometry(50, 50, 200, 50)
        label.setStyleSheet("border : 1px solid white; color : silver")

        self.box = QComboBox(self)
        self.box.setGeometry(50, 100, 180, 50)
        self.box.setStyleSheet("border : 1px solid black; background-color : white; color : black")

        applicants = ["Select Applicant"]

        for applicant_id in data["applicants"].keys():

            applicant_name = data["applicants"][applicant_id]["employee_name"]

            applicants.append(applicant_name)

        self.box.addItems(applicants)
        self.box.currentTextChanged.connect(self.load_applicant)
    
    def load_applicant(self):

        with open('/home/shellbyy/Desktop/KasMekLLC/jsonFiles/applications.json', 'r', encoding='utf-8-sig') as applicant_info:
            data = json.load(applicant_info)

        for iden in data["applicants"].keys():

            self.label1 = QLabel(f'Applicant Name: {str(data["applicants"][iden]["employee_name"])}', self)
            self.label1.setWordWrap(False)
            self.label1.setGeometry(250, 100, 400, 50)
            self.label1.setStyleSheet("background-color : black; color : silver")
            self.label1.show()

            self.label2 = QLabel(f'Phone Number: {str(data["applicants"][iden]["employee_phone_number"])}', self)
            self.label2.setWordWrap(False)
            self.label2.setGeometry(250, 150, 400, 50)
            self.label2.setStyleSheet("background-color : black; color : silver")
            self.label2.show()

            self.label3 = QLabel(f'Address: {str(data["applicants"][iden]["employee_address"])}', self)
            self.label3.setWordWrap(False)
            self.label3.setGeometry(250, 200, 400, 50)
            self.label3.setStyleSheet("background-color : black; color : silver")
            self.label3.show()

            self.label4 = QLabel(f'Email Address: {str(data["applicants"][iden]["employee_email"])}', self)
            self.label4.setWordWrap(False)
            self.label4.setGeometry(250, 250, 400, 50)
            self.label4.setStyleSheet("background-color : black; color : silver")
            self.label4.show()

            self.label5 = QLabel(f'Desired Job: {str(data["applicants"][iden]["desired_job"])}', self)
            self.label5.setWordWrap(False)
            self.label5.setGeometry(250, 300, 400, 50)
            self.label5.setStyleSheet("background-color : black; color : silver")
            self.label5.show()

            self.label6 = QLabel(f'Desired Pay Rate: {str(data["applicants"][iden]["desired_pay"])}', self)
            self.label6.setWordWrap(False)
            self.label6.setGeometry(250, 350, 400, 50)
            self.label6.setStyleSheet("background-color : black; color : silver")
            self.label6.show()

            self.label7 = QLabel(f'Race: {str(data["applicants"][iden]["race"])}', self)
            self.label7.setWordWrap(False)
            self.label7.setGeometry(250, 400, 400, 50)
            self.label7.setStyleSheet("background-color : black; color : silver")
            self.label7.show()

            self.label8 = QLabel(f'Religion: {str(data["applicants"][iden]["religion"])}', self)
            self.label8.setWordWrap(False)
            self.label8.setGeometry(250, 450, 400, 50)
            self.label8.setStyleSheet("background-color : black; color : silver")
            self.label8.show()

            self.label9 = QLabel(f'Social Security Number: {str(data["applicants"][iden]["ssn"])}', self)
            self.label9.setWordWrap(False)
            self.label9.setGeometry(250, 500, 400, 50)
            self.label9.setStyleSheet("background-color : black; color : silver")
            self.label9.show()

            self.label10 = QLabel(f'Work History 1:\n{str(data["applicants"][iden]["job_1_name"])}\n{str(data["applicants"][iden]["job_1_phone"])}\{str(data["applicants"][iden]["job_1_address"])}\{str(data["applicants"][iden]["job_1_title"])}\n{str(data["applicants"][iden]["job_1_duties"])}\n{str(data["applicants"][iden]["job_1_pay"])}\n{str(data["applicants"][iden]["job_1_pay_type"])}\n{str(data["applicants"][iden]["job_1_start_date"])}\n{str(data["applicants"][iden]["job_1_end_date"])}\{str(data["applicants"][iden]["job_1_supervisor"])}\n{str(data["applicants"][iden]["job_1_reason"])}', self)
            self.label10.setWordWrap(True)
            self.label10.setGeometry(690, 100, 400, 200)
            self.label10.setStyleSheet("background-color : black; color : silver")
            self.label10.show()