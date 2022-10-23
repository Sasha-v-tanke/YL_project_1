import sys, os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui

from Exceptions import *
from Windows import *
from Constants import *
from Enums import WindowName

class Manager:
    def __init__(self):
        self.changeMaket(WindowName.WELCOME_WINDOW)
        self.window.show()

    def changeMaket(self, name: WindowName):
        if name == WindowName.WELCOME_WINDOW:
            self.window = WelcomeWindow(self)


def start():
    app = QApplication(sys.argv)
    manager = Manager()
    sys.exit(app.exec_())