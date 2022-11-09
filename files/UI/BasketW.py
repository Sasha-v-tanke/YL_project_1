from Windows import Window
import sys, os.path, sqlite3
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSpinBox, QScrollArea, QFormLayout, QLabel, QVBoxLayout, QMessageBox
from PyQt5.QtCore import QRect
from datetime import datetime
from Enums import WindowName
from Constants import *


class BasketW(Window):
    def setupUI(self):
        self.con = sqlite3.connect(MENU_DB)
        self.cur = self.con.cursor()
        self.lst = list()
        self.setWindowTitle("Корзина")

        self.layout = QVBoxLayout(self)
        self.scroll = QScrollArea()
        self.layout.addWidget(self.scroll)
        self.form = QFormLayout(self.scroll)
        self.form.setHorizontalSpacing(50)
        
        self.BackToShop = QPushButton(self)
        self.BackToShop.setGeometry(QRect(10, 0, 75, 25))
        self.BackToShop.setText("Назад")
        self.BackToShop.clicked.connect(self.back)

        self.Buy = QPushButton(self)
        self.Buy.setGeometry(QRect(SIZE_W[0] - 75, SIZE_W[1] - 25, 75, 25))
        self.Buy.setText("Купить")
        self.Buy.clicked.connect(self.addToBasket)

    def load(self):
        self.dishes = []
        for dish in self.lst:
            d = self.cur.execute("""SELECT 
                            Title, Price
                            FROM Dishes
                            WHERE DishId = ?""", (dish,)).fetchone()
            s = QSpinBox()
            b = QLabel(str(d[1]) + "\t" + d[0])
            self.form.addRow(s, b)
            self.dishes.append((s, dish))

    def addToBasket(self):
        newList = []
        for dish in self.dishes:
            if dish[0].value():
                newList.append((dish[1], dish[0].value()))
        ids = [e[0] for e in self.cur.execute("""SELECT OrderId FROM Orders""").fetchall()]
        if not newList:
            return
        id = 0
        while id in ids:
            id += 1
        time = str(datetime.now().hour) + ":" + str(datetime.now().minute)
        self.cur.execute("""INSERT INTO Orders(OrderId, Time) VALUES(?, ?)""", (id, time))
        self.con.commit()
        for dish in newList:
            self.cur.execute("""INSERT INTO OrderedDishes(DishId, Count, OrderId) VALUES(?, ?, ?)""", (*dish, id))
        self.con.commit()
        mes = QMessageBox()
        mes.setIcon(QMessageBox.Information)
        mes.setText("Номер:                 " + str(id))
        mes.setStandardButtons(QMessageBox.Ok)
        mes.setWindowTitle("Ваш заказ принят")
        mes.exec_()
    
    def __del__(self):
        self.con.close()

    def addOffer(self, lst):
        for elem in lst:
            if elem not in self.lst:
                self.lst.append(elem)
        self.load()

    def back(self):
        self.manager.backToShop(self.lst)