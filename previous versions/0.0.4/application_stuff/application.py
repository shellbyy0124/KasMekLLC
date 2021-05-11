import random
import sys
import json

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

"""
SET THIS CODE TO ALSO BE TRIGGERED BY OUT WEBSITE FOR WHEN PEOPLE WANT TO APPLY FROM ANYWHERE OUTSIDE OF THE COMPANY'S BUILDING
"""

class Application(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("KasMek, LLC - Application")
        self.setStyleSheet("background-color : blue")
        self.UiComponents()
        self.showMaximized()
        self.pay_types = ["Select One", "Hourly", "Salary"]

    def UiComponents(self):

        self.welcome = QLabel("Hi and Welcome! We are happy that you have decided to take a dive into the programming community! Please do keep a few things in mind:\n- Be sure to answer all questions truthfully, and accurately\n- This application does not guaruntee employement", self)
        self.welcome.setWordWrap(False)
        self.welcome.setGeometry(350, 50, 950, 60)
        self.welcome.setStyleSheet("border : 1px solid black; background-color : silver; color : black; text-decoration : underline")

        self.name = QLabel("First, Middle, Last Name:", self)
        self.name.setWordWrap(False)
        self.name.setGeometry(100, 150, 225, 50)
        self.name.setStyleSheet("border : 1px solid black; color : silver")
        
        self.address = QLabel("Address, City, State, Zip Code:", self)
        self.address.setWordWrap(False)
        self.address.setGeometry(100, 200, 225, 50)
        self.address.setStyleSheet("border : 1px solid black; color : silver")

        self.phone_number = QLabel("Phone Number:", self)
        self.phone_number.setWordWrap(False)
        self.phone_number.setGeometry(100, 250, 225, 50)
        self.phone_number.setStyleSheet("border : 1px solid black; color : silver")

        self.email_address = QLabel("Email Address:", self)
        self.email_address.setWordWrap(False)
        self.email_address.setGeometry(100, 300, 225, 50)
        self.email_address.setStyleSheet("border : 1px solid black; color : silver")

        self.dob = QLabel("Date Of Birth:", self)
        self.dob.setWordWrap(False)
        self.dob.setGeometry(100, 350, 225, 50)
        self.dob.setStyleSheet("border : 1px solid black; color : silver")

        self.desired_job = QLabel("Desired Job:", self)
        self.desired_job.setWordWrap(False)
        self.desired_job.setGeometry(100, 400, 225, 50)
        self.desired_job.setStyleSheet("border : 1px solid black; color : silver")

        self.desired_pay = QLabel("Desired Pay:", self)
        self.desired_pay.setWordWrap(False)
        self.desired_pay.setGeometry(100, 450, 225, 50)
        self.desired_pay.setStyleSheet("border : 1px solid black; color : silver")

        self.race = QLabel("Ethnicity:", self)
        self.race.setWordWrap(False)
        self.race.setGeometry(100, 500, 225, 50)
        self.race.setStyleSheet("border : 1px solid black; color : silver")

        self.age = QLabel("Age:", self)
        self.age.setWordWrap(False)
        self.age.setGeometry(100, 550, 225, 50)
        self.age.setStyleSheet("border : 1px solid black; color : silver")

        self.religion = QLabel("Religion Status:", self)
        self.religion.setWordWrap(False)
        self.religion.setGeometry(100, 600, 225, 50)
        self.religion.setStyleSheet("border : 1px solid black; color : silver")

        self.ssn = QLabel("Social Security Number", self)
        self.ssn.setWordWrap(False)
        self.ssn.setGeometry(100, 650, 225, 50)
        self.ssn.setStyleSheet("border : 1px solid black; color : silver")

        self.nname = QLineEdit(self)
        self.nname.setGeometry(350, 150, 225, 50)
        self.nname.setStyleSheet("border : 1px solid black; background-color : silver; color : black")

        self.aaddress = QLineEdit(self)
        self.aaddress.setGeometry(350, 200, 225, 50)
        self.aaddress.setStyleSheet("border : 1px solid black; background-color : silver; color : black")

        self.pphone_number = QLineEdit(self)
        self.pphone_number.setGeometry(350, 250, 225, 50)
        self.pphone_number.setStyleSheet("border : 1px solid black; background-color : silver; color : black")

        self.eemail_address = QLineEdit(self)
        self.eemail_address.setGeometry(350, 300, 225, 50)
        self.eemail_address.setStyleSheet("border : 1px solid black; background-color : silver; color : black")

        self.ddob = QLineEdit(self)
        self.ddob.setGeometry(350, 350, 225, 50)
        self.ddob.setStyleSheet("border : 1px solid black; background-color : silver; color : black")

        self.ddesired_job = QLineEdit(self)
        self.ddesired_job.setGeometry(350, 400, 225, 50)
        self.ddesired_job.setStyleSheet("border : 1px solid black; background-color : silver; color : black")

        self.ddesired_pay = QLineEdit(self)
        self.ddesired_pay.setGeometry(350, 450, 225, 50)
        self.ddesired_pay.setStyleSheet("border : 1px solid black; background-color : silver; color : black")

        self.rrace = QLineEdit(self)
        self.rrace.setGeometry(350, 500, 225, 50)
        self.rrace.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        
        self.aage = QComboBox(self)
        self.aage.setGeometry(350, 550, 225, 50)
        self.aage.setStyleSheet("border : 1px solid black; background-color : silver; color : black")

        ages = ["Select Age"]

        for i in range(100):
            ages.append(str(i))

        self.aage.addItems(ages)

        self.rreligion = QLineEdit(self)
        self.rreligion.setGeometry(350, 600, 225, 50)
        self.rreligion.setStyleSheet("border : 1px solid black; background-color : silver; color : black")

        self.s_ssn = QLineEdit(self)
        self.s_ssn.setGeometry(350, 650, 225, 50)
        self.s_ssn.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.s_ssn.show()

        self.essay = QLabel("Please Write 3-5 sentences tell us why you would make a great asset to KasMek, LLC.", self)
        self.essay.setWordWrap(False)
        self.essay.setGeometry(700, 150, 600, 50)
        self.essay.setStyleSheet("border : 1px solid black; color : silver; text-decoration : underline")

        self.eessay = QLineEdit(self)
        self.eessay.setGeometry(700, 200, 700, 300)
        self.eessay.setStyleSheet("border : 1px solid black; background-color : silver; color : black")

        self.button = QPushButton("Exit", self)
        self.button.setGeometry(350, 700, 225, 50)
        self.button.setStyleSheet("border : 1px solid black; background-color : white; color : black; text-decoration : underline")
        self.button.clicked.connect(self.exit_button)

        self.button2 = QPushButton("Next", self)
        self.button2.setGeometry(950, 700, 225, 50)
        self.button2.setStyleSheet("border : 1px solid black; background-color : white; color : black; text-decoration : underline")
        self.button2.clicked.connect(self.history_one)

    def history_one(self):

        self.welcome.hide()
        self.name.hide()
        self.address.hide()
        self.phone_number.hide()
        self.email_address.hide()
        self.desired_job.hide()
        self.desired_pay.hide()
        self.age.hide()
        self.religion.hide()
        self.race.hide()
        self.button2.hide()
        self.nname.hide()
        self.aaddress.hide()
        self.pphone_number.hide()
        self.eemail_address.hide()
        self.ddesired_job.hide()
        self.ddesired_pay.hide()
        self.rrace.hide()
        self.aage.hide()
        self.rreligion.hide()
        self.ssn.hide()
        self.s_ssn.hide()
        self.essay.hide()
        self.eessay.hide()

        self.previous_employement = QLabel("Previous Work History", self)
        self.previous_employement.setWordWrap(False)
        self.previous_employement.setGeometry(720, 0, 160, 30)
        self.previous_employement.setStyleSheet("border : 1px solid black; color : Silver; text-decoration : underline")
        self.previous_employement.show()

        self.history_1 = QLabel("Previous Work History 1:", self)
        self.history_1.setWordWrap(False)
        self.history_1.setGeometry(5, 100, 180, 50)
        self.history_1.setStyleSheet("border : 1px solid black; color : silver; text-decoration : underline")
        self.history_1.show()

        self.history_1_name = QLabel("Previous Employeers Name:", self)
        self.history_1_name.setWordWrap(False)
        self.history_1_name.setGeometry(5, 150, 320, 50)
        self.history_1_name.setStyleSheet("border : 1px solid black; color : silver")
        self.history_1_name.show()

        self.history_1_phone = QLabel("Previous Employeers Phone Number:", self)
        self.history_1_phone.setWordWrap(False)
        self.history_1_phone.setGeometry(5, 200, 320, 50)
        self.history_1_phone.setStyleSheet("border : 1px solid black; color : silver")
        self.history_1_phone.show()

        self.history_1_address = QLabel("Previous Employeers Address, City, State, Zip:", self)
        self.history_1_address.setWordWrap(False)
        self.history_1_address.setGeometry(5, 250, 320, 50)
        self.history_1_address.setStyleSheet("border : 1px solid black; color : silver")
        self.history_1_address.show()

        self.history_1_job = QLabel("Previous Job Title:", self)
        self.history_1_job.setWordWrap(False)
        self.history_1_job.setGeometry(5, 300, 320, 50)
        self.history_1_job.setStyleSheet("border : 1px solid black; color : silver")
        self.history_1_job.show()

        self.history_1_job_duties = QLabel("Previous Job Duties:", self)
        self.history_1_job_duties.setWordWrap(False)
        self.history_1_job_duties.setGeometry(5, 350, 320, 50)
        self.history_1_job_duties.setStyleSheet("border : 1px solid black; color : silver")
        self.history_1_job_duties.show()

        self.history_1_pay = QLabel("Previous Pay Rate:", self)
        self.history_1_pay.setWordWrap(False)
        self.history_1_pay.setGeometry(5, 400, 320, 50)
        self.history_1_pay.setStyleSheet("border : 1px solid black; color : silver")
        self.history_1_pay.show()

        self.history_1_pay_type = QLabel("Previous Pay Type (Hourly or Salary):", self)
        self.history_1_pay_type.setWordWrap(False)
        self.history_1_pay_type.setGeometry(5, 450, 320, 50)
        self.history_1_pay_type.setStyleSheet("border : 1px solid black; color : silver")
        self.history_1_pay_type.show()

        self.history_1_date_start = QLabel("Previous Employement Start Date:", self)
        self.history_1_date_start.setWordWrap(False)
        self.history_1_date_start.setGeometry(5, 500, 320, 50)
        self.history_1_date_start.setStyleSheet("border : 1px solid black; color : silver")
        self.history_1_date_start.show()

        self.history_1_date_end = QLabel("Previous Employment End Date:", self)
        self.history_1_date_end.setWordWrap(False)
        self.history_1_date_end.setGeometry(5, 550, 320, 50)
        self.history_1_date_end.setStyleSheet("border : 1px solid black; color : silver")
        self.history_1_date_end.show()

        self.history_1_previous_sup = QLabel("Previous Supervisors Name:", self)
        self.history_1_previous_sup.setWordWrap(False)
        self.history_1_previous_sup.setGeometry(5, 600, 320, 50)
        self.history_1_previous_sup.setStyleSheet("border : 1px solid black; color : silver")
        self.history_1_previous_sup.show()

        self.history_1_nname = QLineEdit(self)
        self.history_1_nname.setGeometry(330, 150, 200, 50)
        self.history_1_nname.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.history_1_nname.show()

        self.history_1_pphone = QLineEdit(self)
        self.history_1_pphone.setGeometry(330, 200, 200, 50)
        self.history_1_pphone.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.history_1_pphone.show()

        self.history_1_aaddress = QLineEdit(self)
        self.history_1_aaddress.setGeometry(330, 250, 200, 50)
        self.history_1_aaddress.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.history_1_aaddress.show()

        self.history_1_jjob = QLineEdit(self)
        self.history_1_jjob.setGeometry(330, 300, 200, 50)
        self.history_1_jjob.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.history_1_jjob.show()

        self.history_1_jjob_duties = QLineEdit(self)
        self.history_1_jjob_duties.setGeometry(330, 350, 200, 50)
        self.history_1_jjob_duties.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.history_1_jjob_duties.show()

        self.history_1_ppay = QLineEdit(self)
        self.history_1_ppay.setGeometry(330, 400, 200, 50)
        self.history_1_ppay.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.history_1_ppay.show()

        self.history_1_ppay_type = QComboBox(self)
        self.history_1_ppay_type.setGeometry(330, 450, 200, 50)
        self.history_1_ppay_type.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.history_1_ppay_type.addItems(self.pay_types)
        self.history_1_ppay_type.show()

        self.history_1_ddate_start = QLineEdit(self)
        self.history_1_ddate_start.setGeometry(330, 500, 200, 50)
        self.history_1_ddate_start.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.history_1_ddate_start.show()

        self.history_1_ddate_end = QLineEdit(self)
        self.history_1_ddate_end.setGeometry(330, 550, 200, 50)
        self.history_1_ddate_end.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.history_1_ddate_end.show()

        self.history_1_pprevious_sup = QLineEdit(self)
        self.history_1_pprevious_sup.setGeometry(330, 600, 200, 50)
        self.history_1_pprevious_sup.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.history_1_pprevious_sup.show()

        self.button3 = QPushButton("Next", self)
        self.button3.setGeometry(950, 700, 225, 50)
        self.button3.setStyleSheet("border : 1px solid black; background-color : white; color : black; text-decoration : underline")
        self.button3.clicked.connect(self.history_two)
        self.button3.show()

    def history_two(self):

        self.button3.hide()

        self.history_2 = QLabel("Previous Work History 2:", self)
        self.history_2.setWordWrap(False)
        self.history_2.setGeometry(540, 100, 170, 50)
        self.history_2.setStyleSheet("border : 1px solid black; color : silver; text-decoration : underline")
        self.history_2.show()

        self.history_2_name = QLabel("Previous Employeers Name:", self)
        self.history_2_name.setWordWrap(False)
        self.history_2_name.setGeometry(540, 150, 320, 50)
        self.history_2_name.setStyleSheet("border : 1px solid black; color : silver")
        self.history_2_name.show()

        self.history_2_phone = QLabel("Previous Employeers Phone Number:", self)
        self.history_2_phone.setWordWrap(False)
        self.history_2_phone.setGeometry(540, 200, 320, 50)
        self.history_2_phone.setStyleSheet("border : 1px solid black; color : silver")
        self.history_2_phone.show()

        self.history_2_address = QLabel("Previous Employeers Address, City, State, Zip:", self)
        self.history_2_address.setWordWrap(False)
        self.history_2_address.setGeometry(540, 250, 320, 50)
        self.history_2_address.setStyleSheet("border : 1px solid black; color : silver")
        self.history_2_address.show()

        self.history_2_job = QLabel("Previous Job Title:", self)
        self.history_2_job.setWordWrap(False)
        self.history_2_job.setGeometry(540, 300, 320, 50)
        self.history_2_job.setStyleSheet("border : 1px solid black; color : silver")
        self.history_2_job.show()

        self.history_2_job_duties = QLabel("Previous Job Duties:", self)
        self.history_2_job_duties.setWordWrap(False)
        self.history_2_job_duties.setGeometry(540, 350, 320, 50)
        self.history_2_job_duties.setStyleSheet("border : 1px solid black; color : silver")
        self.history_2_job_duties.show()

        self.history_2_pay = QLabel("Previous Pay Rate:", self)
        self.history_2_pay.setWordWrap(False)
        self.history_2_pay.setGeometry(540, 400, 320, 50)
        self.history_2_pay.setStyleSheet("border : 1px solid black; color : silver")
        self.history_2_pay.show()

        self.history_2_pay_type = QLabel("Previous Pay Type (Hourly or Salary):", self)
        self.history_2_pay_type.setWordWrap(False)
        self.history_2_pay_type.setGeometry(540, 450, 320, 50)
        self.history_2_pay_type.setStyleSheet("border : 1px solid black; color : silver")
        self.history_2_pay_type.show()

        self.history_2_date_start = QLabel("Previous Employement Start Date:", self)
        self.history_2_date_start.setWordWrap(False)
        self.history_2_date_start.setGeometry(540, 500, 320, 50)
        self.history_2_date_start.setStyleSheet("border : 1px solid black; color : silver")
        self.history_2_date_start.show()

        self.history_2_date_end = QLabel("Previous Employment End Date:", self)
        self.history_2_date_end.setWordWrap(False)
        self.history_2_date_end.setGeometry(540, 550, 320, 50)
        self.history_2_date_end.setStyleSheet("border : 1px solid black; color : silver")
        self.history_2_date_end.show()

        self.history_2_previous_sup = QLabel("Previous Supervisors Name:", self)
        self.history_2_previous_sup.setWordWrap(False)
        self.history_2_previous_sup.setGeometry(540, 600, 320, 50)
        self.history_2_previous_sup.setStyleSheet("border : 1px solid black; color : silver")
        self.history_2_previous_sup.show()

        self.history_2_nname = QLineEdit(self)
        self.history_2_nname.setGeometry(865, 150, 200, 50)
        self.history_2_nname.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.history_2_nname.show()

        self.history_2_pphone = QLineEdit(self)
        self.history_2_pphone.setGeometry(865, 200, 200, 50)
        self.history_2_pphone.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.history_2_pphone.show()

        self.history_2_aaddress = QLineEdit(self)
        self.history_2_aaddress.setGeometry(865, 250, 200, 50)
        self.history_2_aaddress.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.history_2_aaddress.show()

        self.history_2_jjob = QLineEdit(self)
        self.history_2_jjob.setGeometry(865, 300, 200, 50)
        self.history_2_jjob.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.history_2_jjob.show()

        self.history_2_jjob_duties = QLineEdit(self)
        self.history_2_jjob_duties.setGeometry(865, 350, 200, 50)
        self.history_2_jjob_duties.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.history_2_jjob_duties.show()

        self.history_2_ppay = QLineEdit(self)
        self.history_2_ppay.setGeometry(865, 400, 200, 50)
        self.history_2_ppay.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.history_2_ppay.show()

        self.history_2_ppay_type = QComboBox(self)
        self.history_2_ppay_type.setGeometry(865, 450, 200, 50)
        self.history_2_ppay_type.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.history_2_ppay_type.addItems(self.pay_types)
        self.history_2_ppay_type.show()

        self.history_2_ddate_start = QLineEdit(self)
        self.history_2_ddate_start.setGeometry(865, 500, 200, 50)
        self.history_2_ddate_start.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.history_2_ddate_start.show()

        self.history_2_ddate_end = QLineEdit(self)
        self.history_2_ddate_end.setGeometry(865, 550, 200, 50)
        self.history_2_ddate_end.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.history_2_ddate_end.show()

        self.history_2_pprevious_sup = QLineEdit(self)
        self.history_2_pprevious_sup.setGeometry(865, 600, 200, 50)
        self.history_2_pprevious_sup.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.history_2_pprevious_sup.show()

        self.button4 = QPushButton("Next", self)
        self.button4.setGeometry(950, 700, 225, 50)
        self.button4.setStyleSheet("border : 1px solid black; background-color : white; color : black; text-decoration : underline")
        self.button4.clicked.connect(self.history_three)
        self.button4.show()

    def history_three(self):

        self.button4.hide()

        self.history_3 = QLabel("Previous Work History 3:", self)
        self.history_3.setWordWrap(False)
        self.history_3.setGeometry(1075, 100, 175, 50)
        self.history_3.setStyleSheet("border : 1px solid black; color : silver; text-decoration : underline")
        self.history_3.show()

        self.history_3_name = QLabel("Previous Employeers Name:", self)
        self.history_3_name.setWordWrap(False)
        self.history_3_name.setGeometry(1075, 150, 320, 50)
        self.history_3_name.setStyleSheet("border : 1px solid black; color : silver")
        self.history_3_name.show()

        self.history_3_phone = QLabel("Previous Employeers Phone Number:", self)
        self.history_3_phone.setWordWrap(False)
        self.history_3_phone.setGeometry(1075, 200, 320, 50)
        self.history_3_phone.setStyleSheet("border : 1px solid black; color : silver")
        self.history_3_phone.show()

        self.history_3_address = QLabel("Previous Employeers Address, City, State, Zip:", self)
        self.history_3_address.setWordWrap(False)
        self.history_3_address.setGeometry(1075, 250, 320, 50)
        self.history_3_address.setStyleSheet("border : 1px solid black; color : silver")
        self.history_3_address.show()

        self.history_3_job = QLabel("Previous Job Title:", self)
        self.history_3_job.setWordWrap(False)
        self.history_3_job.setGeometry(1075, 300, 320, 50)
        self.history_3_job.setStyleSheet("border : 1px solid black; color : silver")
        self.history_3_job.show()

        self.history_3_job_duties = QLabel("Previous Job Duties:", self)
        self.history_3_job_duties.setWordWrap(False)
        self.history_3_job_duties.setGeometry(1075, 350, 320, 50)
        self.history_3_job_duties.setStyleSheet("border : 1px solid black; color : silver")
        self.history_3_job_duties.show()

        self.history_3_pay = QLabel("Previous Pay Rate:", self)
        self.history_3_pay.setWordWrap(False)
        self.history_3_pay.setGeometry(1075, 400, 320, 50)
        self.history_3_pay.setStyleSheet("border : 1px solid black; color : silver")
        self.history_3_pay.show()

        self.history_3_pay_type = QLabel("Previous Pay Type (Hourly or Salary):", self)
        self.history_3_pay_type.setWordWrap(False)
        self.history_3_pay_type.setGeometry(1075, 450, 320, 50)
        self.history_3_pay_type.setStyleSheet("border : 1px solid black; color : silver")
        self.history_3_pay_type.show()

        self.history_3_date_start = QLabel("Previous Employement Start Date:", self)
        self.history_3_date_start.setWordWrap(False)
        self.history_3_date_start.setGeometry(1075, 500, 320, 50)
        self.history_3_date_start.setStyleSheet("border : 1px solid black; color : silver")
        self.history_3_date_start.show()

        self.history_3_date_end = QLabel("Previous Employment End Date:", self)
        self.history_3_date_end.setWordWrap(False)
        self.history_3_date_end.setGeometry(1075, 550, 320, 50)
        self.history_3_date_end.setStyleSheet("border : 1px solid black; color : silver")
        self.history_3_date_end.show()

        self.history_3_previous_sup = QLabel("Previous Supervisors Name:", self)
        self.history_3_previous_sup.setWordWrap(False)
        self.history_3_previous_sup.setGeometry(1075, 600, 320, 50)
        self.history_3_previous_sup.setStyleSheet("border : 1px solid black; color : silver")
        self.history_3_previous_sup.show()

        self.history_3_nname = QLineEdit(self)
        self.history_3_nname.setGeometry(1400, 150, 195, 50)
        self.history_3_nname.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.history_3_nname.show()

        self.history_3_pphone = QLineEdit(self)
        self.history_3_pphone.setGeometry(1400, 200, 195, 50)
        self.history_3_pphone.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.history_3_pphone.show()

        self.history_3_aaddress = QLineEdit(self)
        self.history_3_aaddress.setGeometry(1400, 250, 195, 50)
        self.history_3_aaddress.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.history_3_aaddress.show()

        self.history_3_jjob = QLineEdit(self)
        self.history_3_jjob.setGeometry(1400, 300, 195, 50)
        self.history_3_jjob.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.history_3_jjob.show()

        self.history_3_jjob_duties = QLineEdit(self)
        self.history_3_jjob_duties.setGeometry(1400, 350, 195, 50)
        self.history_3_jjob_duties.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.history_3_jjob_duties.show()

        self.history_3_ppay = QLineEdit(self)
        self.history_3_ppay.setGeometry(1400, 400, 195, 50)
        self.history_3_ppay.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.history_3_ppay.show()

        self.history_3_ppay_type = QComboBox(self)
        self.history_3_ppay_type.setGeometry(1400, 450, 195, 50)
        self.history_3_ppay_type.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.history_3_ppay_type.addItems(self.pay_types)
        self.history_3_ppay_type.show()

        self.history_3_ddate_start = QLineEdit(self)
        self.history_3_ddate_start.setGeometry(1400, 500, 195, 50)
        self.history_3_ddate_start.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.history_3_ddate_start.show()

        self.history_3_ddate_end = QLineEdit(self)
        self.history_3_ddate_end.setGeometry(1400, 550, 195, 50)
        self.history_3_ddate_end.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.history_3_ddate_end.show()

        self.history_3_pprevious_sup = QLineEdit(self)
        self.history_3_pprevious_sup.setGeometry(1400, 600, 195, 50)
        self.history_3_pprevious_sup.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.history_3_pprevious_sup.show()

        self.button5 = QPushButton("Next", self)
        self.button5.setGeometry(950, 700, 225, 50)
        self.button5.setStyleSheet("border : 1px solid black; background-color : white; color : black; text-decoration : underline")
        self.button5.clicked.connect(self.reasons_screen)
        self.button5.show()

    def reasons_screen(self):

        self.previous_employement.hide()
        self.history_1.hide()
        self.history_1_name.hide()
        self.history_1_phone.hide()
        self.history_1_address.hide()
        self.history_1_job.hide()
        self.history_1_job_duties.hide()
        self.history_1_pay.hide()
        self.history_1_pay_type.hide()
        self.history_1_date_start.hide()
        self.history_1_date_end.hide()
        self.history_1_previous_sup.hide()
        self.history_1_nname.hide()
        self.history_1_pphone.hide()
        self.history_1_aaddress.hide()
        self.history_1_jjob.hide()
        self.history_1_jjob_duties.hide()
        self.history_1_ppay.hide()
        self.history_1_ppay_type.hide()
        self.history_1_ddate_start.hide()
        self.history_1_ddate_end.hide()
        self.history_1_pprevious_sup.hide()

        self.history_2.hide()
        self.history_2_name.hide()
        self.history_2_phone.hide()
        self.history_2_address.hide()
        self.history_2_job.hide()
        self.history_2_job_duties.hide()
        self.history_2_pay.hide()
        self.history_2_pay_type.hide()
        self.history_2_date_start.hide()
        self.history_2_date_end.hide()
        self.history_2_previous_sup.hide()
        self.history_2_nname.hide()
        self.history_2_pphone.hide()
        self.history_2_aaddress.hide()
        self.history_2_jjob.hide()
        self.history_2_jjob_duties.hide()
        self.history_2_ppay.hide()
        self.history_2_ppay_type.hide()
        self.history_2_ddate_start.hide()
        self.history_2_ddate_end.hide()
        self.history_2_pprevious_sup.hide()

        self.history_3.hide()
        self.history_3_name.hide()
        self.history_3_phone.hide()
        self.history_3_address.hide()
        self.history_3_job.hide()
        self.history_3_job_duties.hide()
        self.history_3_pay.hide()
        self.history_3_pay_type.hide()
        self.history_3_date_start.hide()
        self.history_3_date_end.hide()
        self.history_3_previous_sup.hide()
        self.history_3_nname.hide()
        self.history_3_pphone.hide()
        self.history_3_aaddress.hide()
        self.history_3_jjob.hide()
        self.history_3_jjob_duties.hide()
        self.history_3_ppay.hide()
        self.history_3_ppay_type.hide()
        self.history_3_ddate_start.hide()
        self.history_3_ddate_end.hide()
        self.history_3_pprevious_sup.hide()
        self.button5.hide()

        self.reas = QLabel("Reasons For Leaving", self)
        self.reas.setWordWrap(False)
        self.reas.setGeometry(720, 0, 140, 30)
        self.reas.setStyleSheet("border : 1px solid black; color : silver; text-decoration : underline")
        self.reas.show()

        self.reason1 = QLabel("Reason For Leaving Previous Employement #1:", self)
        self.reason1.setWordWrap(False)
        self.reason1.setGeometry(90, 100, 325, 50)
        self.reason1.setStyleSheet("border : 1px solid black; color : silver")
        self.reason1.show()

        """
        FIND A WAY TO SET THE CURSOR POSITION AT THE TOP LEFT OF THE QLINEEDIT BOX
        SO THAT WHEN YOU TYPE, IT STARTS AT THE TOP LEFT CORNER INSTEAD OF IN THE MIDDLE
        """

        self.rreason1 = QLineEdit(self)
        self.rreason1.setGeometry(90, 150, 325, 300)
        self.rreason1.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.rreason1.show()

        self.reason2 = QLabel("Reason For Leaving Previous Employement #2:", self)
        self.reason2.setWordWrap(False)
        self.reason2.setGeometry(630, 100, 325, 50)
        self.reason2.setStyleSheet("border : 1px solid black; color : silver")
        self.reason2.show()

        self.rreason2 = QLineEdit(self)
        self.rreason2.setGeometry(630, 150, 325, 300)
        self.rreason2.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.rreason2.show()

        self.reason3 = QLabel("Reason For Leaving Previous Employement #3:", self)
        self.reason3.setWordWrap(False)
        self.reason3.setGeometry(1170, 100, 325, 50)
        self.reason3.setStyleSheet("border : 1px solid black; color : silver")
        self.reason3.show()

        self.rreason3 = QLineEdit(self)
        self.rreason3.setGeometry(1170, 150, 325, 300)
        self.rreason3.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.rreason3.show()

        self.button6 = QPushButton("Next", self)
        self.button6.setGeometry(950, 700, 225, 50)
        self.button6.setStyleSheet("border : 1px solid black; background-color : white; color : black; text-decoration : underline")
        self.button6.clicked.connect(self.college_education_info)
        self.button6.show()

    def college_education_info(self):

        self.reason1.hide()
        self.rreason1.hide()
        self.reason2.hide()
        self.rreason2.hide()
        self.reason3.hide()
        self.rreason3.hide()
        self.button6.hide()
        self.reas.hide()

        self.ed_his = QLabel("Education History", self)
        self.ed_his.setWordWrap(False)
        self.ed_his.setGeometry(725, 0, 130, 30)
        self.ed_his.setStyleSheet("border : 1px solid black; color : silver; text-decoration : underline")
        self.ed_his.show()

        self.college_name = QLabel("College Univerity Name:", self)
        self.college_name.setWordWrap(False)
        self.college_name.setGeometry(5, 50, 275, 50)
        self.college_name.setStyleSheet("border : 1px solid black; color : silver")
        self.college_name.show()

        self.college_address = QLabel("College University Address, City, State:", self)
        self.college_address.setWordWrap(False)
        self.college_address.setGeometry(5, 100, 275, 50)
        self.college_address.setStyleSheet("border : 1px solid black; color : silver")
        self.college_address.show()

        self.college_phone_number = QLabel("College Universitys Phone Number:", self)
        self.college_phone_number.setWordWrap(False)
        self.college_phone_number.setGeometry(5, 150, 275, 50)
        self.college_phone_number.setStyleSheet("border : 1px solid black; color : silver")
        self.college_phone_number.show()

        self.college_start_date = QLabel("Start Date:", self)
        self.college_start_date.setWordWrap(False)
        self.college_start_date.setGeometry(5, 200, 275, 50)
        self.college_start_date.setStyleSheet("border : 1px solid black; color : silver")
        self.college_start_date.show()

        self.college_end_date = QLabel("End Date:", self)
        self.college_end_date.setWordWrap(False)
        self.college_end_date.setGeometry(5, 250, 275, 50)
        self.college_end_date.setStyleSheet("border : 1px solid black; color : silver")
        self.college_end_date.show()

        self.college_grad = QLabel("Did you graduate?", self)
        self.college_grad.setWordWrap(False)
        self.college_grad.setGeometry(5, 300, 275, 50)
        self.college_grad.setStyleSheet("border : 1px solid black; color : silver")
        self.college_grad.show()

        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        SET THIS AREA SO THAT WHEN THEY TOGGLE YES, IT TRIGGERS A SEPARATE SCREEN SETUP TO HANDLE UP TO 5 ADDITIONAL COLLEGES

        # self.add_more = QLabel("Do you have another college to add?", self)
        # self.add_more.setWordWrap(False)
        # self.add_more.setGeometry(5, 350, 275, 50)
        # self.add_more.setStyleSheet("border : 1px solid black; color : silver")
        # self.add_more.show()

        # self.radio = QRadioButton("Yes", self)
        # self.radio.setChecked(False)
        # self.radio.setGeometry(300, 350, 50, 50)
        # self.radio.setStyleSheet('''QRadioButton {border : 1px solid black; background-color : blue; color : silver;}
        #                             QRadioButton::indicator:checked {border : 1px solid black; background-color : blue; color : silver;}
        #                             QRadioButton::indicator:unchecked {border : 1px solid black; background-color : white; color : silver}''')
        # self.radio.toggled.connect(self.toggle_yes)
        # self.radio.show()

        # self.radio2 = QRadioButton("No", self)
        # self.radio2.setChecked(False)
        # self.radio2.setGeometry(350, 350, 50, 50)
        # self.radio2.setStyleSheet('''QRadioButton {border : 1px solid black; background-color : blue; color : silver;}
        #                             QRadioButton::indicator:checked {border : 1px solid black; background-color : blue; color : silver;}
        #                             QRadioButton::indicator:unchecked {border : 1px solid black; background-color : white; color : silver}''')
        # self.radio2.toggled.connect(self.toggle_no)
        # self.radio2.show()

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

        self.college_degree = QLabel("Please tell us about your degree. What kind of degree did you get? Did you graduate with honors?", self)
        self.college_degree.setWordWrap(True)
        self.college_degree.setGeometry(600, 50, 300, 50)
        self.college_degree.setStyleSheet("border : 1px solid black; color : silver")
        self.college_degree.show()

        self.ccollege_name = QLineEdit(self)
        self.ccollege_name.setGeometry(300, 50, 250, 50)
        self.ccollege_name.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.ccollege_name.show()

        self.ccollege_address = QLineEdit(self)
        self.ccollege_address.setGeometry(300, 100, 250, 50)
        self.ccollege_address.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.ccollege_address.show()

        self.ccollege_phone_number = QLineEdit(self)
        self.ccollege_phone_number.setGeometry(300, 150, 250, 50)
        self.ccollege_phone_number.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.ccollege_phone_number.show()

        self.ccollege_start_date = QLineEdit(self)
        self.ccollege_start_date.setGeometry(300, 200, 250, 50)
        self.ccollege_start_date.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.ccollege_start_date.show()

        self.ccollege_end_date = QLineEdit(self)
        self.ccollege_end_date.setGeometry(300, 250, 250, 50)
        self.ccollege_end_date.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.ccollege_end_date.show()

        self.ccollege_grad = QLineEdit(self)
        self.ccollege_grad.setGeometry(300, 300, 250, 50)
        self.ccollege_grad.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.ccollege_grad.show()

        self.ccollege_degree = QLineEdit(self)
        self.ccollege_degree.setGeometry(600, 100, 600, 200)
        self.ccollege_degree.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.ccollege_degree.show()

        self.button7 = QPushButton("Next", self)
        self.button7.setGeometry(950, 700, 225, 50)
        self.button7.setStyleSheet("border : 1px solid black; background-color : white; color : black; text-decoration : underline")
        self.button7.clicked.connect(self.highschool_education_info)
        self.button7.show()

    def highschool_education_info(self):

        self.college_name.hide()
        self.college_address.hide()
        self.college_phone_number.hide()
        self.college_start_date.hide()
        self.college_end_date.hide()
        self.college_grad.hide()
        self.college_degree.hide()
        self.button7.hide()
        self.ccollege_name.hide()
        self.ccollege_address.hide()
        self.ccollege_phone_number.hide()
        self.ccollege_start_date.hide()
        self.ccollege_end_date.hide()
        self.ccollege_grad.hide()
        self.ccollege_degree.hide()

        self.hs_name = QLabel("High School Name:", self)
        self.hs_name.setWordWrap(False)
        self.hs_name.setGeometry(5, 50, 275, 50)
        self.hs_name.setStyleSheet("border : 1px solid black; color : silver")
        self.hs_name.show()

        self.hs_address = QLabel("High School Address, City, State, Zip:", self)
        self.hs_address.setWordWrap(False)
        self.hs_address.setGeometry(5, 100, 275, 50)
        self.hs_address.setStyleSheet("border : 1px solid black; color : silver")
        self.hs_address.show()

        self.hs_phone_number = QLabel("High School Phone Number:", self)
        self.hs_phone_number.setWordWrap(False)
        self.hs_phone_number.setGeometry(5, 150, 275, 50)
        self.hs_phone_number.setStyleSheet("border : 1px solid black; color : silver")
        self.hs_phone_number.show()

        self.hs_start_date = QLabel("Start Date:", self)
        self.hs_start_date.setWordWrap(False)
        self.hs_start_date.setGeometry(5, 200, 275, 50)
        self.hs_start_date.setStyleSheet("border : 1px solid black; color : silver")
        self.hs_start_date.show()

        self.hs_end_date = QLabel("End Date:", self)
        self.hs_end_date.setWordWrap(False)
        self.hs_end_date.setGeometry(5, 250, 275, 50)
        self.hs_end_date.setStyleSheet("border : 1px solid black; color : silver")
        self.hs_end_date.show()

        self.hs_grad = QLabel("Did you graduate?", self)
        self.hs_grad.setWordWrap(False)
        self.hs_grad.setGeometry(5, 300, 275, 50)
        self.hs_grad.setStyleSheet("border : 1px solid black; color : silver")
        self.hs_grad.show()

        self.hs_degree = QLabel("Please tell us about your degree. What kind of degree did you get? Did you graduate with honors?", self)
        self.hs_degree.setWordWrap(True)
        self.hs_degree.setGeometry(600, 50, 300, 50)
        self.hs_degree.setStyleSheet("border : 1px solid black; color : silver")
        self.hs_degree.show()

        self.hhs_name = QLineEdit(self)
        self.hhs_name.setGeometry(300, 50, 250, 50)
        self.hhs_name.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.hhs_name.show()

        self.hhs_address = QLineEdit(self)
        self.hhs_address.setGeometry(300, 100, 250, 50)
        self.hhs_address.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.hhs_address.show()

        self.hhs_phone_number = QLineEdit(self)
        self.hhs_phone_number.setGeometry(300, 150, 250, 50)
        self.hhs_phone_number.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.hhs_phone_number.show()

        self.hhs_start_date = QLineEdit(self)
        self.hhs_start_date.setGeometry(300, 200, 250, 50)
        self.hhs_start_date.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.hhs_start_date.show()

        self.hhs_end_date = QLineEdit(self)
        self.hhs_end_date.setGeometry(300, 250, 250, 50)
        self.hhs_end_date.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.hhs_end_date.show()

        self.hhs_grad = QLineEdit(self)
        self.hhs_grad.setGeometry(300, 300, 250, 50)
        self.hhs_grad.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.hhs_grad.show()

        self.hhs_degree = QLineEdit(self)
        self.hhs_degree.setGeometry(600, 100, 600, 200)
        self.hhs_degree.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.hhs_degree.show()

        self.button8 = QPushButton("Next", self)
        self.button8.setGeometry(950, 700, 225, 50)
        self.button8.setStyleSheet("border : 1px solid black; background-color : white; color : black; text-decoration : underline")
        self.button8.clicked.connect(self.references_info)
        self.button8.show()

    def references_info(self):

        self.ed_his.hide()
        self.hs_name.hide()
        self.hs_address.hide()
        self.hs_phone_number.hide()
        self.hs_start_date.hide()
        self.hs_end_date.hide()
        self.hs_degree.hide()
        self.hs_grad.hide()
        self.hhs_name.hide()
        self.hhs_address.hide()
        self.hhs_phone_number.hide()
        self.hhs_start_date.hide()
        self.hhs_end_date.hide()
        self.hhs_degree.hide()
        self.hhs_grad.hide()
        self.button8.hide()

        self.ref = QLabel("References:", self)
        self.ref.setWordWrap(False)
        self.ref.setGeometry(755, 0, 90, 30)
        self.ref.setStyleSheet("border : 1px solid black; color : silver; text-decoration : underline")
        self.ref.show()

        self.ref_one = QLabel("Reference Number 1:", self)
        self.ref_one.setWordWrap(False)
        self.ref_one.setGeometry(50, 50, 155, 50)
        self.ref_one.setStyleSheet("border : 1px solid black; color : silver")
        self.ref_one.show()

        self.ref_two = QLabel("Reference Number 2:", self)
        self.ref_two.setWordWrap(False)
        self.ref_two.setGeometry(50, 280, 155, 50)
        self.ref_two.setStyleSheet("border : 1px solid black; color : silver")
        self.ref_two.show()

        self.ref_three = QLabel("Reference Number 3:", self)
        self.ref_three.setWordWrap(False)
        self.ref_three.setGeometry(50, 480, 155, 50)
        self.ref_three.setStyleSheet("border : 1px solid black; color : silver")
        self.ref_three.show()

        self.ref_one_name = QLabel("Name:", self)
        self.ref_one_name.setWordWrap(False)
        self.ref_one_name.setGeometry(210, 100, 55, 50)
        self.ref_one_name.setStyleSheet("border : 1px solid black; color : silver")
        self.ref_one_name.show()

        self.ref_two_name = QLabel("Name:", self)
        self.ref_two_name.setWordWrap(False)
        self.ref_two_name.setGeometry(210, 330, 55, 50)
        self.ref_two_name.setStyleSheet("border : 1px solid black; color : silver")
        self.ref_two_name.show()

        self.ref_three_name = QLabel("Name:", self)
        self.ref_three_name.setWordWrap(False)
        self.ref_three_name.setGeometry(210, 530, 55, 50)
        self.ref_three_name.setStyleSheet("border : 1px solid black; color : silver")
        self.ref_three_name.show()

        self.ref_one_phone_number = QLabel("Phone Number:", self)
        self.ref_one_phone_number.setWordWrap(False)
        self.ref_one_phone_number.setGeometry(280, 155, 115, 50)
        self.ref_one_phone_number.setStyleSheet("border : 1px solid black; color : silver")
        self.ref_one_phone_number.show()

        self.ref_two_phone_number = QLabel("Phone Number:", self)
        self.ref_two_phone_number.setWordWrap(False)
        self.ref_two_phone_number.setGeometry(280, 385, 115, 50)
        self.ref_two_phone_number.setStyleSheet("border : 1px solid black; color : silver")
        self.ref_two_phone_number.show()

        self.ref_three_phone_number = QLabel("Phone Number:", self)
        self.ref_three_phone_number.setWordWrap(False)
        self.ref_three_phone_number.setGeometry(280, 585, 115, 50)
        self.ref_three_phone_number.setStyleSheet("border : 1px solid black; color : silver")
        self.ref_three_phone_number.show()

        self.ref_one_address = QLabel("Address:", self)
        self.ref_one_address.setWordWrap(False)
        self.ref_one_address.setGeometry(410, 210, 70, 50)
        self.ref_one_address.setStyleSheet("border : 1px solid black; color : silver")
        self.ref_one_address.show()

        self.ref_two_address = QLabel("Address:", self)
        self.ref_two_address.setWordWrap(False)
        self.ref_two_address.setGeometry(410, 440, 70, 50)
        self.ref_two_address.setStyleSheet("border : 1px solid black; color : silver")
        self.ref_two_address.show()

        self.ref_three_address = QLabel("Address:", self)
        self.ref_three_address.setWordWrap(False)
        self.ref_three_address.setGeometry(410, 640, 70, 50)
        self.ref_three_address.setStyleSheet("border : 1px solid black; color : silver")
        self.ref_three_address.show()

        self.rref_one_name = QLineEdit(self)
        self.rref_one_name.setGeometry(280, 100, 200, 50)
        self.rref_one_name.setStyleSheet('border : 1px solid black; background-color : silver; color : black')
        self.rref_one_name.show()

        self.rref_two_name = QLineEdit(self)
        self.rref_two_name.setGeometry(280, 330, 200, 50)
        self.rref_two_name.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.rref_two_name.show()

        self.rref_three_name = QLineEdit(self)
        self.rref_three_name.setGeometry(280, 530, 200, 50)
        self.rref_three_name.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.rref_three_name.show()

        self.rref_one_phone_number = QLineEdit(self)
        self.rref_one_phone_number.setGeometry(410, 155, 200, 50)
        self.rref_one_phone_number.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.rref_one_phone_number.show()

        self.rref_two_phone_number = QLineEdit(self)
        self.rref_two_phone_number.setGeometry(410, 385, 200, 50)
        self.rref_two_phone_number.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.rref_two_phone_number.show()

        self.rref_three_phone_number = QLineEdit(self)
        self.rref_three_phone_number.setGeometry(410, 585, 200, 50)
        self.rref_three_phone_number.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.rref_three_phone_number.show()

        self.rref_one_address = QLineEdit(self)
        self.rref_one_address.setGeometry(490, 210, 300, 50)
        self.rref_one_address.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.rref_one_address.show()

        self.rref_two_address = QLineEdit(self)
        self.rref_two_address.setGeometry(490, 440, 300, 50)
        self.rref_two_address.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.rref_two_address.show()

        self.rref_three_address = QLineEdit(self)
        self.rref_three_address.setGeometry(490, 640, 300, 50)
        self.rref_three_address.setStyleSheet("border : 1px solid black; background-color : silver; color : black")
        self.rref_three_address.show()

        self.button9 = QPushButton("Next", self)
        self.button9.setGeometry(950, 700, 225, 50)
        self.button9.setStyleSheet("border : 1px solid black; background-color : white; color : black; text-decoration : underline")
        self.button9.clicked.connect(self.app_finished)
        self.button9.show()

    def app_finished(self):

        self.ref.hide()
        self.ref_one.hide()
        self.ref_two.hide()
        self.ref_three.hide()
        self.ref_one_name.hide()
        self.ref_one_address.hide()
        self.ref_one_phone_number.hide()
        self.ref_two_name.hide()
        self.ref_two_address.hide()
        self.ref_two_phone_number.hide()
        self.ref_three_name.hide()
        self.ref_three_address.hide()
        self.ref_three_phone_number.hide()
        self.rref_one_name.hide()
        self.rref_one_address.hide()
        self.rref_one_phone_number.hide()
        self.rref_two_address.hide()
        self.rref_two_name.hide()
        self.rref_two_phone_number.hide()
        self.rref_three_address.hide()
        self.rref_three_name.hide()
        self.rref_three_phone_number.hide()
        self.button9.hide()

        with open('/home/shellbyy/Desktop/KasMekLLC/jsonFiles/applications.json', 'r', encoding='utf-8-sig') as f:
            data = json.load(f)

        emp_id_num = random.randint(100000, 199999)

        while emp_id_num in data.keys():

            emp_id_num = random.randint(100000, 199999)

        else:

            pass

        data["applicants"] = {

            str(emp_id_num) : {
                "applicant_name" : self.nname.text(),
                "applicant_phone_number" : self.pphone_number.text(),
                "applicant_address" : self.aaddress.text(),
                "applicant_email" : self.eemail_address.text(),
                "desired_job" : self.ddesired_job.text(),
                "desired_pay" : self.ddesired_pay.text(),
                "race" : self.rrace.text(),
                "age" : self.aage.currentText(),
                "dob" : self.ddob.currentText(),
                "religion" : self.rreligion.text(),
                "ssn" : self.s_ssn.text(),
                "essay" : self.eessay.text(),
                "job_1_name" : self.history_1_nname.text(),
                "job_1_phone" : self.history_1_pphone.text(),
                "job_1_address" : self.history_1_aaddress.text(),
                "job_1_title" : self.history_1_jjob.text(),
                "job_1_duties" : self.history_1_jjob_duties.text(),
                "job_1_pay" : self.history_1_ppay.text(),
                "job_1_pay_type" : self.history_1_ppay_type.currentText(),
                "job_1_start_date" : self.history_1_ddate_start.text(),
                "job_1_end_date" : self.history_1_ddate_end.text(),
                "job_1_supervisor" : self.history_1_pprevious_sup.text(),
                "job_1_reason" : self.rreason1.text(),
                "job_2_name" : self.history_2_nname.text(),
                "job_2_phone" : self.history_2_pphone.text(),
                "job_2_address" : self.history_2_aaddress.text(),
                "job_2_title" : self.history_2_jjob.text(),
                "job_2_duties" : self.history_2_jjob_duties.text(),
                "job_2_pay" : self.history_2_ppay.text(),
                "job_2_pay_type" : self.history_2_ppay_type.currentText(),
                "job_2_start_date" : self.history_2_ddate_start.text(),
                "job_2_end_date" : self.history_2_ddate_end.text(),
                "job_2_supervisor" : self.history_2_pprevious_sup.text(),
                "job_2_reason" : self.rreason2.text(),
                "job_3_name" : self.history_3_nname.text(),
                "job_3_phone" : self.history_3_pphone.text(),
                "job_3_address" : self.history_3_aaddress.text(),
                "job_3_title" : self.history_3_jjob.text(),
                "job_3_duties" : self.history_3_jjob_duties.text(),
                "job_3_pay" : self.history_3_ppay.text(),
                "job_3_pay_type" : self.history_3_ppay_type.currentText(),
                "job_3_start_date" : self.history_3_ddate_start.text(),
                "job_3_end_date" : self.history_3_ddate_end.text(),
                "job_3_supervisor" : self.history_3_pprevious_sup.text(),
                "job_3_reason" : self.rreason3.text(),
                "college_name" : self.ccollege_name.text(),
                "college_phone" : self.ccollege_phone_number.text(),
                "college_address" : self.ccollege_address.text(),
                "college_start_date" : self.ccollege_start_date.text(),
                "college_end_date" : self.ccollege_end_date.text(),
                "college_grad" : self.ccollege_grad.text(),
                "college_degree" : self.ccollege_degree.text(),
                "highschool_name" : self.hhs_name.text(),
                "highschool_phone" : self.hhs_phone_number.text(),
                "highschool_address" : self.hhs_address.text(),
                "highschool_start_date" : self.hhs_start_date.text(),
                "highschool_end_date" : self.hhs_end_date.text(),
                "highschool_grad" : self.hhs_grad.text(),
                "highschool_degree" : self.hhs_degree.text(),
                "ref_one_name" : self.rref_one_name.text(),
                "ref_one_phone" : self.rref_one_phone_number.text(),
                "ref_one_address" : self.rref_one_address.text(),
                "ref_two_name" : self.rref_two_name.text(),
                "ref_two_phone" : self.rref_two_phone_number.text(),
                "ref_two_address" : self.rref_two_address.text(),                
                "ref_three_name" : self.rref_three_name.text(),
                "ref_three_address" : self.rref_three_address.text(),
                "ref_three_phone" : self.rref_three_phone_number.text()
            }
        }

        with open('/home/shellbyy/Desktop/KasMekLLC/0.0.4/hr/employment/applications.json', 'w', encoding='utf-8-sig') as g:
            data = json.dump(data, g, indent=4)

        self.label = QLabel(self)
        self.pixmap = QPixmap('congratz.png')
        self.label.setPixmap(self.pixmap)
        self.label.setGeometry(575, 0, 700, 50)
        self.resize(self.pixmap.width(),self.pixmap.height())
        self.label.show()

    """""""""""""""""""""""""""""""""""""""""""""""""""
    THESE ARE THE FUNCTIONS TO THE RADIO BUTTONS ABOVE

    # def toggle_yes(self):

    #     pass

    # def toggle_no(self):

    #     pass


    """""""""""""""""""""""""""""""""""""""""""""""""""

    def exit_button(self):

        self.hide()