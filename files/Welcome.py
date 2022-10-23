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
        self.coor = (200, 200)
        self.start()

    def changeMaket(self, name: WindowName):
        self.coor = (self.window.x() + 1, self.window.y() + 31)  # без понятия почему окно смещается при открытии
        if name == WindowName.WELCOME_WINDOW:
            self.window = WelcomeWindow(self)
        elif name == WindowName.SHOP_WINDOW:
            self.window = UserWindow(self)
        elif name == WindowName.ADMIN_WINDOW:
            self.window = AdminWindow(self)
        elif name == WindowName.CREATOR_WINDOW:
            self.window = CreatorWindow(self)
        self.window.setGeometry(*self.coor, self.window.width(), self.window.height())
        self.window.show()

    def start(self):
        self.window = WelcomeWindow(self)
        self.window.setGeometry(*self.coor, self.window.width(), self.window.height())
        self.window.show()

def start():
    app = QApplication(sys.argv)
    manager = Manager()
    sys.exit(app.exec_())