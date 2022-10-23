import sys, os.path
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui

from Exceptions import *
from Constants import *
from Enums import WindowName


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

    def changeMaket(self,  maket: str):
        try:
            if '.ui' not in maket:
                raise NameFileException
            elif not os.path.exists('.\\' + maket):
                raise DirectoryFileException
            else:
                uic.loadUi(maket, self)
                return True
        except Exception as exc:
            print(exc)
            return False


class WelcomeWindow(Window):
    def __init__(self, manager):
        self.manager = manager
        super().__init__()
        if self.changeMaket(PATH_UI_WELCOME_WINDOW):
            self.GoToAdminAccount.clicked.connect(self.goToAdminMenu)
            self.NewOrder.clicked.connect(self.openUserWindow)

    def goToAdminMenu(self):
        self.manager.changeMaket(WindowName.ADMIN_WINDOW)

    def openUserWindow(self):
        self.manager.changeMaket(WindowName.SHOP_WINDOW)
        #login = self.Login.text()
        #password = self.Password.text()
        #self.CheckPassword.setText(login + password)



class AdminWindow(Window):
    def __init__(self):
        super().__init__()
        if self.changeMaket(PATH_UI_WELCOME):
            pass
            #self.CheckPassword.clicked.connect(self.checkAdminAccount)
            

class UserWindow(Window):
    def __init__(self):
        super().__init__()
        if self.changeMaket(PATH_UI_SHOP_WINDOW):
            pass
            #self.CheckPassword.clicked.connect(self.checkAdminAccount)


def start():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())