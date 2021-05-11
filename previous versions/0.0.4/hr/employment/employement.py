import sys
import json
import random

from datetime import datetime

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class EmployementScreen(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("KasMek, LLC - Employement Window")
        self.setStyleSheet("background-color : silver")
        self.UiComponents()
        self.showMaximized()

    def UiComponents(self):

        self.label = QLabel("Future Employees", self)
        self.label.setWordWrap(False)
        self.label.setGeometry(100, 100, 100, 50)
        self.label.setStyleSheet("border : 1px solid blue; background-color : silver; color : black; text-decoration : underline")

        self.button = QPushButton("Applicants", self)
        self.button.setGeometry(110, 150, 100, 50)
        self.button.setStyleSheet("background-color : silver; color : black")
        self.button.clicked.connect(self.show_apps)

        self.button2 = QPushButton("Exit System", self)
        self.button2.setGeometry(300, 600, 100, 50)
        self.button2.setStyleSheet("background-color : silver; color : black")
        self.button2.clicked.connect(self.exit_button)

    def show_apps(self):

        self.label.hide()
        self.button.hide()
        self.button2.hide()

        self.box = QComboBox(self)
        self.box.setGeometry(100, 100, 200, 100)
        self.box.setStyleSheet("border : 1px solid black; background-color : white; color : black")

        with open('./KasMekLLC/0.0.4/hr/employment/applicants.json', 'r', encoding='utf-8-sig') as f:
            data = json.load(f)

        app_id_list = ["Select Applicant"]

        for app_id in data.keys():

            app_id_list.append(data[app_id]["applicant_name"])

        self.box.addItems(app_id_list)
        self.box.currentTextChanged.connect(self.display_applicant)

    def display_applicant(self):

        with open('./KasMekLLC/0.0.4/hr/employment/applicants.json', 'r', encoding='utf-8-sig') as g:
            data = json.load(g)

        for app_id in data.keys():

            name = data[app_id]["applicant_name"]
            age = data[app_id]["applicant_age"]
            phone = data[app_id]["applicant_phone_number"]
            email = data[app_id]["applicant_email"]
            address = data[app_id]["applicant_address"]
            race = data[app_id]["race"]
            religion = data[app_id]["religion"]
            ssn = data[app_id]["ssn"]
            dob = data[app_id]["dob"]
            desired_job = data[app_id]["desired_job"]
            desired_pay = data[app_id]["desired_pay"]
            essay = data[app_id]["essay"]
            job1name = data[app_id]["job_1_name"]
            job1phone = data[app_id]["job_1_phone"]
            job1address = data[app_id]["job_1_address"]
            job1title = data[app_id]["job_1_title"]
            job1duties = data[app_id]["job_1_duties"]
            job1pay = data[app_id]["job_1_pay"]
            job1paytype = data[app_id]["job_1_pay_type"]
            job1start = data[app_id]["job_1_start_date"]
            job1end = data[app_id]["job_1_end_date"]
            job1supervisor = data[app_id]["job_1_supervisor"]
            job1reason = data[app_id]["job_1_reason"]
            job2name = data[app_id]["job_2_name"]
            job2phone = data[app_id]["job_2_phone"]
            job2address = data[app_id]["job_2_address"]
            job2title = data[app_id]["job_2_title"]
            job2duties = data[app_id]["job_2_duties"]
            job2pay = data[app_id]["job_2_pay"]
            job2paytype = data[app_id]["job_2_pay_type"]
            job2start = data[app_id]["job_2_start_date"]
            job2end = data[app_id]["job_2_end_date"]
            job2supervisor = data[app_id]["job_2_supervisor"]
            job2reason = data[app_id]["job_2_reason"]
            job3name = data[app_id]["job_3_name"]
            job3phone = data[app_id]["job_3_phone"]
            job3address = data[app_id]["job_3_address"]
            job3title = data[app_id]["job_3_title"]
            job3duties = data[app_id]["job_3_duties"]
            job3pay = data[app_id]["job_3_pay"]
            job3paytype = data[app_id]["job_3_pay_type"]
            job3start = data[app_id]["job_3_start_date"]
            job3end = data[app_id]["job_3_end_date"]
            job3supervisor = data[app_id]["job_3_supervisor"]
            job3reason = data[app_id]["job_3_reason"]


        self.label1 = QLabel(f"Applicant General Information:", self)
        self.label1.setWordWrap(False)
        self.label1.setGeometry(200, 100, 300, 50)
        self.label1.setStyleSheet("border : 1px solid black; background-color : #add8e6; color : black")
        self.label1.show()

        self.label2 = QLabel(f"{str(name)}\n{str(age)}\n{str(phone)}\n{str(email)}\n{str(address)}\n{str(race)}\n{str(religion)}\n{str(ssn)}\n{str(dob)}\n{str(desired_job)}\n{str(desired_pay)}", self)
        self.label2.setWordWrap(False)
        self.label2.setGeometry(200, 150, 300, 300)
        self.label2.setStyleSheet("border : 1px solid black; background-color : #add8e6; color : black")
        self.label2.show()

        self.label3 = QLabel(f"Applicant's Essay:\n{str(essay)}", self)
        self.label3.setWordWrap(True)
        self.label3.setGeometry(200, 500, 300, 400)
        self.label3.setStyleSheet("border : 1px solid black; background-color : #add8e6; color : black")
        self.label3.show()

        self.label4 = QLabel("Previous Work History:", self)
        self.label4.setWordWrap(False)
        self.label4.setGeometry(400, 100, 250, 50)
        self.label4.setStyleSheet("border : 1px solid black; background-color : #add8e6; color : black")
        self.label4.show()

        self.label5 = QLabel(f"{str(job1name)}\n{str(job1phone)}\n{str(job1address)}\n{str(job1title)}\n{str(job1duties)}\n{str(job1pay)}\n{str(job1paytype)}\n{str(job1start)}{str(job1end)}\n{str(job1supervisor)}\n{str(job1reason)}", self)
        self.label5.setWordWrap(False)
        self.label5.setGeometry(400, 150, 300, 400)
        self.label5.setStyleSheet("border : 1px solid black; background-color : #add8e6; color : black")
        self.label5.show()

        self.label6 = QLabel(f"{str(job2name)}\m{str(job2phone)}\n{str(job2address)}\n{str(job2title)}\n{str(job2duties)}\n{str(job2pay)}\n{str(job2paytype)}\n{str(job2start)}\n{str(job2end)}\n{str(job2supervisor)}\n{str(job2reason)}", self)
        self.label6.setWordWrap(False)
        self.label6.setGeometry(400, 400, 300, 400)
        self.label6.setStyleSheet("border : 1px solid black; background-color : #add8e6; color : black")
        self.label6.show()
        
    def exit_button(self):

        App = QApplication(sys.argv)
        sys.exit(App.exec_())