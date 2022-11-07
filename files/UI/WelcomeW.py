from Windows import Window
from Enums import WindowName
from Constants import SIZE_W

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QRect



class WelcomeW(Window):
    def goToAdminMenu(self):
        self.manager.changeMaket(WindowName.ADMIN_WINDOW)

    def openUserWindow(self):
        self.manager.changeMaket(WindowName.SHOP_WINDOW)

    def setupUI(self):
        self.setWindowTitle("Добро пожаловать")
        
        size = (120, 100)
        self.NewOrder = QPushButton(self.widget)
        self.NewOrder.setGeometry(QRect(int(SIZE_W[0] - size[0]) / 2, int(SIZE_W[1] - size[1]) / 2, *size))
        self.NewOrder.clicked.connect(self.openUserWindow)
        self.NewOrder.setText("Новый заказ")
        
        size = (150, 20)
        self.GoToAdminAccount = QPushButton(self)
        self.GoToAdminAccount.setGeometry(QRect(int(SIZE_W[0] - 1.1 * size[0]), int(SIZE_W[1] - 1.1 * size[1]), *size))
        self.GoToAdminAccount.clicked.connect(self.goToAdminMenu)
        self.GoToAdminAccount.setText("Войти как администратор")