import sys, os

from Exceptions import NameFileException, DirectoryFileException

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui

PATH_UI_WELCOME_WINDOW = "UI\\WelcomeWindow.ui"
PATH_UI_ADMIN_WINDOW = "UI\\AdminWelcome.ui"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        if self.changeMaket(PATH_UI_WELCOME):
            self.AdminAccount.clicked.connect(self.showAdminMenu)
            self.NewOrder.clicked.connect(self.openUserWindow)

    def showAdminMenu(self):
        self.changeMaket(PATH_UI_ADMIN_WINDOW)
        self.CheckPassword.clicked.connect(self.checkAdminAccount)

    def checkAdminAccount(self):
        login = self.Login.text()
        password = self.Password.text()
        self.CheckPassword.setText(login + password)

    def openAdminWindow(self):
        pass

    def openUserWindow(self):
        self.NewOrder.setText("ok")

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


def start():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())