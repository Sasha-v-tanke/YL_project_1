import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('YL_project_1/WelcomeWindow.ui', self)
        self.AdminAccount.clicked.connect(self.showAdminMenu)
        self.NewOrder.clicked.connect(self.openUserWindow)

    def showAdminMenu(self):
        uic.loadUi('AdminWelcome.ui', self)
        self.AdminAccount.setText("OK")
        self.CheckPassword.clicked.connect(self.checkAdminAccount)

    def checkAdminAccount(self):
        login = self.Login.text()
        password = self.Password.text()
        self.CheckPassword.setText(login + password)

    def openAdminWindow(self):
        pass

    def openUserWindow(self):
        self.NewOrder.setText("ok")

def start():
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())