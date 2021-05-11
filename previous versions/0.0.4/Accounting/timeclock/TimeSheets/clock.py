import random
import json
import sys
import os
import datetime

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from datetime import datetime

from loadingscreen import LoadingScreen

class ClockSystem(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("KasMek, LLC - Click System")
        self.setStyleSheet("background-color : blue")
        self.UiComponents()
        self.showMaximized()

    def UiComponents(self):

        label = QLabel("Emp ID Num:", self)
        label.setWordWrap(False)
        label.setGeometry(300, 300, 100, 50)
        label.setStyleSheet("border : 1px solid black; background-color : gray; color : black")
        
        label = QLabel("Password:", self)
        label.setWordWrap(False)
        label.setGeometry(300, 400, 100, 50)
        label.setStyleSheet("border : 1px solid black; background-color : gray; color : black")

        self.line1 = QLineEdit(self)
        self.line1.setGeometry(450, 300, 200, 50)
        self.line1.setStyleSheet("border : 1px solid black; background-color : silver; color : black")

        self.line2 = QLineEdit(self)
        self.line2.setGeometry(450, 400, 200, 50)
        self.line2.setStyleSheet("border : 1px solid black; background-color : silver; color : black")

        button = QPushButton("Back", self)
        button.setGeometry(300, 500, 100, 50)
        button.setStyleSheet("border : 1px solid black; background-color : gray; color : black")
        button.clicked.connect(self.exit_button)

        button = QPushButton("Clock In", self)
        button.setGeometry(450, 500, 100, 50)
        button.setStyleSheet("border : 1px solid black; background-color : gray; color : black")
        button.clicked.connect(self.check_user_id)

        button = QPushButton("Clock Out", self)
        button.setGeometry(600, 500, 100, 50)
        button.setStyleSheet("border : 1px solid black; background-color : gray; color : black")
        # button.clicked.connect(self.file_check)

        self.check_user_id()

    def check_user_id(self):

        """
        THIS IS A CHECK TO SEE IF THE ID ENTERED INTO SELF.LINE1.TEXT() MATCHES ANY OF THE ID'S IN THE
        DATABASE. IF NOT, SHOW ERROR AND ALLOW USER TO TRY AGAIN, OTHERWISE CALL NEXT FUNCTION
        """

        # for row in cursor_one:

            # while self.line1.text() not in row:

            #     self.error_label = QLabel("That id does not exist in this database", self)
            #     self.error_label.setWordWrap(False)
            #     self.error_label.setGeometry(600, 300, 250, 50)
            #     self.error_label.setStyleSheet("color : red")
            #     self.error_label.show()
            #     break # or what goes here?
                
            # else:
                
            #     self.check_user_password()

            #     conn_one.close()

    def check_user_password(self):

        """
        THIS IS A CHECK TO SEE IF THE PASSWORD ENTERED INTO SELF.LINE2.TEXT() MATCHES THE PASSWORD ASSOCIATED
        WITH THE ID USED ABOVE. IF NOT, SHOW ERROR, OTHERWISE, CALL NEXT FUNCTION
        """

        for row2 in cursor_two:

            while self.line2.text() not in row2:

                self.error_label2 = QLabel("That password does not exist in this database", self)
                self.error_label2.setWordWrap(False)
                self.error_label2.setGeometry(600, 400, 300, 50)
                self.error_label2.setStyleSheet("color : red")
                self.error_label2.show()
            
            else:

                self.file_check()

    def file_check(self):

        """
        THIS IS A CHECK TO SEE IF THE DATABASE FILE EXISTS THROUGH THE OS LIBRARY, THEN USING THE SQLITE3
        LIBRARY TO CREATE THE DATABASE IF IT DOESN'T EXIST, THEN IT CREATES THE TABLE WITH THE COLUMN NAMES,
        THEN IT'S SUPPOSED TO CALL THE NEXT FUNCTION
        """

        self.table_name = datetime.today().__format__('%m_%d_%y')

        if not os.path.exists(f'/home/shellbyy/Desktop/KasMekLLC/0.0.4/Accounting/timeclock/TimeSheets/current_week/pay_periods.db'):

            self.clock_in_user()

        else:

            self.clock_in_user()

    def clock_in_user(self):

        """
        THIS IS THE CLOCK IN SYSTEM. IT'S SUPPOSED TO ADD THE EMPLOYEES ID TO THE PAY_PERIODS.DB IF IT DOESN'T
        EXIST, THEN ADD THE 'TIME_IN' ROW TO THE EMPLOYEE ID COLUMN WITH THE SELF.CLOCK_IN TIME STAMP. ONCE
        SUCCESSFUL, DISPLAY LABEL SHOWING SUCCESSFUL CLOCK IN
        """

        self.clock_in = datetime.today().__format__('%H:%M:%S, %m/%d/%y')

        self.success = QLabel(f"You Have Sucessfully Clocked In At {self.clock_in}", self)
        self.success.setWordWrap(False)
        self.success.setGeometry(300, 100, 250, 50)
        self.success.setStyleSheet("color : white; text-decoration : underline")
        self.success.show()

    def exit_button(self):

        self.hide()