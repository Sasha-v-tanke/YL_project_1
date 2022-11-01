import sys, os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui

from Exceptions import *
#from Windows import *
from UI import MainW, CreatorW, AdminW
from Constants import *
from Enums import WindowName

class Manager:
    def __init__(self):
        self.coor = (200, 200)
        self.start()

    def changeMaket(self, name: WindowName):
        self.coor = (self.window.x() + 1, self.window.y() + 31)  # без понятия почему окно смещается при открытии
        self.window.close()
        if name == WindowName.WELCOME_WINDOW:
            self.window = MainW.WelcomeWindow(self)
        elif name == WindowName.SHOP_WINDOW:
            self.window = ShopWindow(self)
        elif name == WindowName.ADMIN_WINDOW:
            self.window = AdminW.AdminW(self)
        elif name == WindowName.CREATOR_WINDOW:
            self.window = CreatorWindow(self)
        elif name == WindowName.BASKET_WINDOW:
            self.window = BasketWindow(self)
        self.window.setGeometry(*self.coor, *SIZE_W)
        self.window.show()

    def start(self):
        self.window = MainW.WelcomeWindow(self)
        self.window.setGeometry(*self.coor, self.window.width(), self.window.height())
        self.window.show()

def start():
    app = QApplication(sys.argv)
    manager = Manager()
    sys.exit(app.exec_())