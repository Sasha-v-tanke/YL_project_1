import sys, os
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from Exceptions import *
from UI import WelcomeW, CreatorW, AdminW, ShopW, BasketW, OrdersW
from Constants import *
from Enums import WindowName

class Manager:
    def __init__(self):
        self.coor = (200, 200)
        self.start()
        self.tabIndex = -1

    def changeMaket(self, name: WindowName):
        self.coor = (self.window.x() + 1, self.window.y() + 31)  # без понятия почему окно смещается при открытии
        self.window.close()
        if name == WindowName.WELCOME_WINDOW:
            self.window = WelcomeW.WelcomeW(self)
        elif name == WindowName.SHOP_WINDOW:
            self.window = ShopW.ShopW(self)
        elif name == WindowName.ADMIN_WINDOW:
            self.window = AdminW.AdminW(self)
        elif name == WindowName.CREATOR_WINDOW:
            self.window = CreatorW.CreatorW(self)
        elif name == WindowName.BASKET_WINDOW:
            self.window = BasketW.BasketW(self)
        self.window.setGeometry(*self.coor, *SIZE_W)
        self.window.show()

    def updateCreator(self, tabIndex):
        self.changeMaket(WindowName.CREATOR_WINDOW)
        self.window.setSettings(tabIndex)

    def start(self):
        self.window = ShopW.ShopW(self)
        self.window.setGeometry(*self.coor, self.window.width(), self.window.height())
        self.window.show()

    def setOffer(self, lst):
        self.changeMaket(WindowName.BASKET_WINDOW)
        self.window.addOffer(lst)

    def backToShop(self, lst):
        self.changeMaket(WindowName.SHOP_WINDOW)
        self.window.addOffer(lst)


def start():
    app = QApplication(sys.argv)
    manager = Manager()
    sys.exit(app.exec_())