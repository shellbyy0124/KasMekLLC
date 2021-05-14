# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_screen.ui'
##
## Created by: Qt User Interface Compiler version 6.0.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_login_window(object):
    def setupUi(self, login_window):
        if not login_window.objectName():
            login_window.setObjectName(u"login_window")
        login_window.resize(393, 242)
        login_window.setAutoFillBackground(False)
        login_window.setStyleSheet(u"QMainWindow{\n"
"background-color: rgb(38, 38, 38);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
" {\n"
"     background-color: rgb(25, 25, 25);\n"
"     width: 15px;\n"
"     margin: 15px 3px 15px 3px;\n"
"     border: 1px transparent #2A2929;\n"
"     border-radius: 4px;\n"
" }\n"
"\n"
" QScrollBar::handle:vertical\n"
" {\n"
"     background-color: rgb(55, 55, 55);         /* #605F5F; */\n"
"     min-height: 10px;\n"
"     border-radius: 4px;\n"
" }\n"
"QScrollBar::sub-line:vertical\n"
" {\n"
"     margin: 3px 0px 3px 0px;\n"
"     border-image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"QScrollBar::add-line:vertical\n"
" {\n"
"     margin: 3px 0px 3px 0px;\n"
"     border-image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origi"
                        "n: margin;\n"
" }\n"
"\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
" {\n"
"     background: none;\n"
" }")
        self.centralwidget = QWidget(login_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(38, 38, 38);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.password_label = QLabel(self.frame_2)
        self.password_label.setObjectName(u"password_label")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_label.sizePolicy().hasHeightForWidth())
        self.password_label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        self.password_label.setFont(font)
        self.password_label.setStyleSheet(u"color: rgb(0, 200, 200);")

        self.gridLayout_2.addWidget(self.password_label, 9, 1, 1, 1)

        self.user_id_line_edit = QLineEdit(self.frame_2)
        self.user_id_line_edit.setObjectName(u"user_id_line_edit")
        self.user_id_line_edit.setMinimumSize(QSize(250, 22))
        self.user_id_line_edit.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(25, 25, 25);\n"
"border-radius: 10px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;")

        self.gridLayout_2.addWidget(self.user_id_line_edit, 5, 2, 4, 3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 9, 5, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 12, 0, 1, 1)

        self.version_label = QLabel(self.frame_2)
        self.version_label.setObjectName(u"version_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.version_label.sizePolicy().hasHeightForWidth())
        self.version_label.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(8)
        self.version_label.setFont(font1)
        self.version_label.setStyleSheet(u"color: rgb(136, 55, 0);")
        self.version_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.version_label, 0, 1, 1, 5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 9, 0, 1, 1)

        self.password_line_edit = QLineEdit(self.frame_2)
        self.password_line_edit.setObjectName(u"password_line_edit")
        self.password_line_edit.setMinimumSize(QSize(250, 22))
        self.password_line_edit.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(25, 25, 25);\n"
"border-radius: 10px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;")

        self.gridLayout_2.addWidget(self.password_line_edit, 9, 2, 1, 3)

        self.quit_pushbutton = QPushButton(self.frame_2)
        self.quit_pushbutton.setObjectName(u"quit_pushbutton")
        self.quit_pushbutton.setMinimumSize(QSize(0, 30))
        self.quit_pushbutton.setMaximumSize(QSize(80, 16777215))
        self.quit_pushbutton.setFont(font)
        self.quit_pushbutton.setStyleSheet(u"color: rgb(0, 200, 200);\n"
"background-color: rgb(55, 55, 55);\n"
"border-radius: 10px;\n"
"")
        self.quit_pushbutton.setAutoDefault(True)

        self.gridLayout_2.addWidget(self.quit_pushbutton, 11, 4, 1, 1)

        self.login_pushbutton = QPushButton(self.frame_2)
        self.login_pushbutton.setObjectName(u"login_pushbutton")
        self.login_pushbutton.setMinimumSize(QSize(0, 30))
        self.login_pushbutton.setMaximumSize(QSize(80, 16777215))
        self.login_pushbutton.setFont(font)
        self.login_pushbutton.setStyleSheet(u"color: rgb(0, 200, 200);\n"
"background-color: rgb(55, 55, 55);\n"
"border-radius: 10px;\n"
"")
        self.login_pushbutton.setAutoDefault(True)
        self.login_pushbutton.setFlat(False)

        self.gridLayout_2.addWidget(self.login_pushbutton, 11, 3, 1, 1)

        self.user_id_label = QLabel(self.frame_2)
        self.user_id_label.setObjectName(u"user_id_label")
        sizePolicy.setHeightForWidth(self.user_id_label.sizePolicy().hasHeightForWidth())
        self.user_id_label.setSizePolicy(sizePolicy)
        self.user_id_label.setFont(font)
        self.user_id_label.setStyleSheet(u"color: rgb(0, 200, 200);")

        self.gridLayout_2.addWidget(self.user_id_label, 5, 1, 4, 1)

        self.name_label = QLabel(self.frame_2)
        self.name_label.setObjectName(u"name_label")
        sizePolicy1.setHeightForWidth(self.name_label.sizePolicy().hasHeightForWidth())
        self.name_label.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(36)
        font2.setBold(False)
        self.name_label.setFont(font2)
        self.name_label.setStyleSheet(u"color: rgb(0, 250, 250);")
        self.name_label.setFrameShape(QFrame.NoFrame)
        self.name_label.setFrameShadow(QFrame.Plain)
        self.name_label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.name_label.setWordWrap(False)

        self.gridLayout_2.addWidget(self.name_label, 2, 0, 1, 6)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 4, 0, 1, 1)

        self.description_label = QLabel(self.frame_2)
        self.description_label.setObjectName(u"description_label")
        sizePolicy1.setHeightForWidth(self.description_label.sizePolicy().hasHeightForWidth())
        self.description_label.setSizePolicy(sizePolicy1)
        self.description_label.setFont(font)
        self.description_label.setStyleSheet(u"color: rgb(56, 90, 110);")
        self.description_label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_2.addWidget(self.description_label, 3, 0, 1, 6)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        login_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(login_window)

        self.quit_pushbutton.setDefault(True)
        self.login_pushbutton.setDefault(True)


        QMetaObject.connectSlotsByName(login_window)
    # setupUi

    def retranslateUi(self, login_window):
        login_window.setWindowTitle(QCoreApplication.translate("login_window", u"Login", None))
        self.password_label.setText(QCoreApplication.translate("login_window", u"Password:", None))
        self.version_label.setText(QCoreApplication.translate("login_window", u"1.0.1", None))
        self.quit_pushbutton.setText(QCoreApplication.translate("login_window", u"Quit", None))
        self.login_pushbutton.setText(QCoreApplication.translate("login_window", u"Login", None))
        self.user_id_label.setText(QCoreApplication.translate("login_window", u"User-ID:", None))
        self.name_label.setText(QCoreApplication.translate("login_window", u"<html><head/><body><p><span style=\" font-size:28pt; font-weight:600;\">KasMec LLC</span></p></body></html>", None))
        self.description_label.setText(QCoreApplication.translate("login_window", u"Where innovation was invented", None))
    # retranslateUi

