from Windows import Window

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication, QSize, QRect

from Enums import WindowName
from Constants import SIZE_W


class WelcomeWindow(QWidget):
    def __init__(self, manager):
        self.manager = manager
        super().__init__()
        self.setupUi()

    def goToAdminMenu(self):
        self.manager.changeMaket(WindowName.ADMIN_WINDOW)

    def openUserWindow(self):
        self.manager.changeMaket(WindowName.SHOP_WINDOW)

    def setupUi(self):
        self.setGeometry(0, 0, 0, 0)
        self.setMinimumSize(QSize(*SIZE_W))
        self.setMaximumSize(QSize(*SIZE_W))
        self.setWindowTitle("Добро пожаловать")

        self.NewOrder = QPushButton(self)
        self.NewOrder.setGeometry(QRect(340, 250, 120, 100))
        self.NewOrder.clicked.connect(self.openUserWindow)
        self.NewOrder.setText("НОВЫЙ ЗАКАЗ")

        self.GoToAdminAccount = QPushButton(self)
        self.GoToAdminAccount.setGeometry(QRect(630, 560, 160, 30))
        self.GoToAdminAccount.clicked.connect(self.goToAdminMenu)
        self.GoToAdminAccount.setText("ВОЙТИ КАК АДМИНИСТРАТОР")