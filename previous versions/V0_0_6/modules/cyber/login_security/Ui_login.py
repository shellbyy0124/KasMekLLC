# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(944, 657)
        self.actionDiscord_Support_Server = QAction(mainWindow)
        self.actionDiscord_Support_Server.setObjectName(u"actionDiscord_Support_Server")
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 4, 0, 1, 1)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 3, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 3, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer_3, 2, 1, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 4, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 4, 2, 1, 1)

        self.button_login = QPushButton(self.centralwidget)
        self.button_login.setObjectName(u"button_login")

        self.gridLayout.addWidget(self.button_login, 6, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 3, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 7, 1, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 2)

        self.button_exit = QPushButton(self.centralwidget)
        self.button_exit.setObjectName(u"button_exit")

        self.gridLayout.addWidget(self.button_exit, 6, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 5, 1, 1, 2)

        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 944, 22))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        self.menuContact_Us = QMenu(self.menuMenu)
        self.menuContact_Us.setObjectName(u"menuContact_Us")
        mainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.menuContact_Us.menuAction())
        self.menuContact_Us.addAction(self.actionDiscord_Support_Server)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"KasMek, LLC", None))
        self.actionDiscord_Support_Server.setText(QCoreApplication.translate("mainWindow", u"Discord Support Server", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"Employee PW:", None))
        self.button_login.setText(QCoreApplication.translate("mainWindow", u"Login", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"Employee ID:", None))
        self.label_3.setText(QCoreApplication.translate("mainWindow", u"Welcome To KasMek, LLC! Remember: The Day Is What YOU Make It!", None))
        self.button_exit.setText(QCoreApplication.translate("mainWindow", u"Exit", None))
        self.menuMenu.setTitle(QCoreApplication.translate("mainWindow", u"Menu", None))
        self.menuContact_Us.setTitle(QCoreApplication.translate("mainWindow", u"Contact Us", None))
    # retranslateUi

