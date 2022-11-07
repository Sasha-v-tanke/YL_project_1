from Windows import Window
import sys, os.path, sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QSpinBox, QScrollBar, QCheckBox, QFrame, QLabel
from PyQt5.QtCore import QCoreApplication, QSize, QRect, Qt

from Enums import WindowName
from Constants import *


class BasketW(Window):
    def setupUI(self):
        self.lst = []
        self.setWindowTitle("Корзина")

        self.BackToShop = QPushButton(self)
        self.BackToShop.setGeometry(QRect(10, 0, 75, 25))
        self.BackToShop.setText("Назад")
        self.BackToShop.clicked.connect(self.back)

    def addOffer(self, lst):
        self.lst = lst

    def back(self):
        self.manager.backToShop(self.lst)