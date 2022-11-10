from Windows import Window
from Enums import WindowName
from Constants import SIZE_W

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QRect, Qt


class WelcomeW(Window):
    def goToAdminMenu(self):
        self.manager.changeMaket(WindowName.ADMIN_WINDOW)

    def openUserWindow(self):
        self.manager.changeMaket(WindowName.SHOP_WINDOW)

    def setupUI(self):
        self.setWindowTitle("Добро пожаловать")
        
        size = (120, 100)
        self.NewOrder = QPushButton(self)
        self.NewOrder.setGeometry(QRect(int(SIZE_W[0] - size[0]) / 2, int(SIZE_W[1] - size[1]) / 2, *size))
        self.NewOrder.clicked.connect(self.openUserWindow)
        self.NewOrder.setText("Новый заказ")
        
    def keyPressEvent(self, event):
        if int(event.modifiers()) == Qt.AltModifier:
            if event.key() == Qt.Key_C:
                self.manager.setType("creator")
                self.manager.changeMaket(WindowName.ADMIN_WINDOW)
            if event.key() == Qt.Key_M:
                self.manager.setType("manager")
                self.manager.changeMaket(WindowName.ADMIN_WINDOW)