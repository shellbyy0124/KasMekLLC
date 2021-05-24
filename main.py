import sys
import re
from Modules import database
from Modules.CEO.ceo import ChiefExecOfficer
from Modules.manager import WindowManager
from database import database_user_test_data
from PySide6 import QtGui, QtWidgets, QtCore
from PySide6.QtWidgets import QApplication, QMainWindow
from UI.login_screen import Ui_login_window


class LoginScreen(Ui_login_window, QMainWindow):
    def __init__(self, window_manager):
        super(LoginScreen, self).__init__()
        self.setupUi(self)
        self.window_manager = window_manager
        database.create_test_tables()
        database.create_test_user_data(database_user_test_data.data)

        # Set constants
        self.version = "0.7.0.0"
        self.version_label.setText(self.version)

        # Set variables
        self.password = ""

        # Make window borderless
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Hash password as typed (cannot use * in passwords)
        self.password_line_edit.textChanged.connect(self.hash_password)

        # Buttons
        self.login_pushbutton.clicked.connect(self.login)
        self.quit_pushbutton.clicked.connect(self.escape)

        # Event filter for enter key
        self.user_id_line_edit.installEventFilter(self)
        self.password_line_edit.installEventFilter(self)

    def hash_password(self):
        current_text = self.password_line_edit.text()
        if len(current_text) < len(self.password):
            self.password = self.password[:len(current_text)]
        elif len(current_text) > len(self.password):
            self.password += ''.join([x for x in current_text if x != '*'])
            self.password_line_edit.setText(len(self.password) * '*')
        elif len(current_text) == len(self.password) and '*' not in current_text:
            self.password = ''.join([x for x in current_text if x != '*'])
            self.password_line_edit.setText(len(self.password) * '*')

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.KeyPress and (obj is self.password_line_edit or obj is self.user_id_line_edit):
            if event.key() == QtCore.Qt.Key_Enter or event.key() == QtCore.Qt.Key_Return:
                self.login()
        return super().eventFilter(obj, event)

    def login(self):
        msg = QtWidgets.QMessageBox()
        user_id = self.user_id_line_edit.text()
        password = self.password
        password_pattern = r'^[\w!@#$%^&()~]*$'
        employee = database.fetch_employee(user_id)
        if password == employee[2]:
            print(f'Welcome {employee[1]}! You have logged in successfully')
            new_window = ChiefExecOfficer(window_manager)
            self.window_manager.open_window(new_window)
        else:
            print(f'Incorrect password. A virus has been released onto your PC. Good luck!')

    @staticmethod
    def escape():
        sys.exit()


if __name__ == '__main__':
    window_manager = WindowManager()
    app = QApplication(sys.argv)
    window = LoginScreen(window_manager)
    window_manager.open_window(window)

    # set window and application icons
    app.setWindowIcon(QtGui.QIcon('./Data/Icons/innovation.ico'))
    window.setWindowIcon(QtGui.QIcon('./Data/Icons/innovation.ico'))

    sys.exit(app.exec_())