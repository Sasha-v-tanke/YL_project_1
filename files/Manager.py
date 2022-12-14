from PyQt5.QtWidgets import QMainWindow
from Exceptions import *
from UI import WelcomeW, CreatorW, AdminW, ShopW, BasketW, OrdersW
from Constants import SIZE_W
from Enums import WindowName

class Manager:
    def __init__(self):
        self.coor = (200, 200)
        self.start()
        self.tabIndex = -1
        self.password = ''

    def changeMaket(self, name: WindowName, password=''):
        self.coor = (self.window.x() + 1, self.window.y() + 31)  # без понятия почему окно смещается при открытии
        self.window.close()
        if name == WindowName.WELCOME_WINDOW:
            self.window = WelcomeW.WelcomeW(self)
        elif name == WindowName.SHOP_WINDOW:
            self.window = ShopW.ShopW(self)
        elif name == WindowName.ADMIN_WINDOW:
            self.window = AdminW.AdminW(self)
            self.window.setType(self.type)
        elif name == WindowName.CREATOR_WINDOW:
            self.window = CreatorW.CreatorW(self)
            self.password = password
        elif name == WindowName.BASKET_WINDOW:
            self.window = BasketW.BasketW(self)
        elif name == WindowName.ORDERS_WINDOW:
            self.window = OrdersW.OrdersW(self)
        self.window.setGeometry(*self.coor, *SIZE_W)
        self.window.show()

    def getPassword(self):
        return self.password

    def setType(self, type):
        self.type = type

    def updateCreator(self, tabIndex):
        self.changeMaket(WindowName.CREATOR_WINDOW)
        self.window.setSettings(tabIndex)

    def start(self):
        self.window = WelcomeW.WelcomeW(self)
        self.window.setGeometry(*self.coor, self.window.width(), self.window.height())
        self.window.show()

    def setOffer(self, lst):
        self.changeMaket(WindowName.BASKET_WINDOW)
        self.window.addOffer(lst)

    def backToShop(self, lst):
        self.changeMaket(WindowName.SHOP_WINDOW)
        self.window.addOffer(lst)
