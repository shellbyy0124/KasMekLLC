import json
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Manager:

    def __init__(self):

        super().__init__()

        self.current_window = None
        self.previous_window = None