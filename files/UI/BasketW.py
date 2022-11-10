from Windows import Window
import sqlite3
from PyQt5.QtWidgets import QPushButton, QSpinBox, QScrollArea, QFormLayout, QLabel, QVBoxLayout, QMessageBox, QGroupBox
from PyQt5.QtCore import QRect
from datetime import datetime
from Enums import WindowName
from Constants import MENU_DB, SIZE_W


class BasketW(Window):
    def setupUI(self):
        self.setWindowTitle("Корзина")
        self.con = sqlite3.connect(MENU_DB)
        self.cur = self.con.cursor()
        self.lst = list()

        self.Layout = QGroupBox(self)
        self.Layout.setGeometry(QRect(10, 25, 780, 550))
        self.Scroll = QScrollArea(self.Layout)
        self.Scroll.setGeometry(QRect(0, 0, 780, 550))
        self.Form = QFormLayout(self.Scroll)
        self.Form.setHorizontalSpacing(50)
        
        self.BackToShop = QPushButton(self)
        self.BackToShop.setGeometry(QRect(10, 0, 75, 25))
        self.BackToShop.setText("Назад")
        self.BackToShop.clicked.connect(self.back)

        size = (75, 25)
        self.Buy = QPushButton(self)
        self.Buy.setGeometry(QRect(SIZE_W[0] - size[0], SIZE_W[1] - size[1], *size))
        self.Buy.setText("Купить")
        self.Buy.clicked.connect(self.addToBasket)

    def load(self):
        self.rows = []
        for id in self.lst:
            dish = self.cur.execute("""SELECT 
                            Title, Price
                            FROM Dishes
                            WHERE DishId = ?""", (id,)).fetchone()
            Spin = QSpinBox()
            Spin.setValue(1)
            Label = QLabel(str(dish[1]) + "\t" + dish[0])
            self.Form.addRow(Spin, Label)
            self.rows.append((Spin, id))

    def addToBasket(self):
        newList = []
        for row in self.rows:
            if row[0].value():
                newList.append((row[1], row[0].value()))
        ids = [e[0] for e in self.cur.execute("""SELECT OrderId FROM Orders""").fetchall()]
        if not newList:
            return
        orderId = 0
        while orderId in ids:
            orderId += 1

        time = str(datetime.now().hour) + ":" + str(datetime.now().minute)
        self.cur.execute("""INSERT INTO Orders(OrderId, Time) VALUES(?, ?)""", (orderId, time))
        self.con.commit()
        for dish in newList:
            self.cur.execute("""INSERT INTO OrderedDishes(DishId, Count, OrderId) VALUES(?, ?, ?)""", (*dish, orderId))
        self.con.commit()

        Mes = QMessageBox()
        Mes.setIcon(QMessageBox.Information)
        Mes.setText("Номер:                 " + str(orderId))
        Mes.setStandardButtons(QMessageBox.Ok)
        Mes.setWindowTitle("Ваш заказ принят")
        Mes.exec_()

        self.manager.changeMaket(WindowName.WELCOME_WINDOW)
    
    def __del__(self):
        self.con.close()

    def addOffer(self, lst):
        for elem in lst:
            if elem not in self.lst:
                self.lst.append(elem)
        self.load()

    def back(self):
        self.manager.backToShop(self.lst)