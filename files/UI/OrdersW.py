from Windows import Window
import sqlite3
from PyQt5.QtWidgets import QPushButton, QScrollArea, QTableWidget, QAbstractItemView, QTableWidgetItem
from PyQt5.QtCore import QRect
from Enums import WindowName
from Constants import *


class OrdersW(Window):
    """окно менеджера;
    показывает список всех заказов
   и список всех заказанных блюд"""

    def setupUI(self):
        self.con = sqlite3.connect(MENU_DB)
        self.cur = self.con.cursor()
        self.lst = list()
        self.setWindowTitle("Заказы")

        self.BackToShop = QPushButton(self)
        self.BackToShop.setGeometry(QRect(10, 0, 75, 25))
        self.BackToShop.setText("Назад")
        self.BackToShop.clicked.connect(self.back)

        self.AllOrders = QPushButton(self)
        self.AllOrders.setGeometry(QRect(410, 20, 90, 40))
        self.AllOrders.setText("Все заказы")
        self.AllOrders.clicked.connect(self.showOrders)

        self.AllDishes = QPushButton(self)
        self.AllDishes.setGeometry(QRect(300, 20, 90, 40))
        self.AllDishes.setText("Все блюда")
        self.AllDishes.clicked.connect(self.showDishes)

        self.Dishes = QTableWidget(self)
        self.Dishes.setGeometry(QRect(10, 70, 780, 510))
        self.Dishes.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Dishes.setVisible(False)

        self.Orders = QTableWidget(self)
        self.Orders.setGeometry(QRect(10, 70, 780, 510))

        self.load()
        
    def load(self):
        self.setupOrders()
        self.setupDishes()

    def setupOrders(self):
        """в таблицу заносим номер и время заказа и список ввсех позиций в нем"""
        orders = self.cur.execute("""SELECT OrderId, Time FROM Orders""").fetchall()
        self.Orders.setRowCount(len(orders))
        self.Orders.setColumnCount(2)
        self.Orders.setHorizontalHeaderLabels(["id", "блюда"])
        for number, order in enumerate(orders):
            lst = ""
            dishes = self.cur.execute("""SELECT DishId, Count FROM OrderedDishes WHERE OrderId = ?""", (order[0],)).fetchall()
            for dish in dishes:
                lst += str(dish[1]) + " x " + self.cur.execute("""SELECT Title FROM Dishes WHERE DishId = ?""", (dish[0],)).fetchone()[0] + " | "
            self.Orders.setItem(number, 0, QTableWidgetItem("N" + str(order[0]) + ", время: " + order[1]))
            self.Orders.setItem(number, 1, QTableWidgetItem(lst))

    def setupDishes(self):
        """в таблицу заносим список всех заказанных позиций """
        dishIds = self.cur.execute("""SELECT Title, DishId FROM Dishes""").fetchall()
        dishCount = self.cur.execute("""SELECT DishId, Count FROM OrderedDishes""").fetchall()
        dishes_ = []
        for id in dishCount:
            dishes_.append((id[1], dishIds[[title[1] for title in dishIds].index(id[0])][0]))
        dishes = {}
        for dish in dishes_:
            dishes[dish[1]] = 0
        for dish in dishes_:
            dishes[dish[1]] += dish[0]
        self.Dishes.setRowCount(len(dishes.keys()))
        self.Dishes.setColumnCount(2)
        self.Dishes.setHorizontalHeaderLabels(["колво", "название"])
        for number, dish in enumerate(dishes.keys()):
            self.Dishes.setItem(number, 0, QTableWidgetItem(str(dishes[dish])))
            self.Dishes.setItem(number, 1, QTableWidgetItem(dish))
    
    def __del__(self):
        self.con.close()

    def showOrders(self):
        self.Dishes.setVisible(False)
        self.Orders.setVisible(True)

    def showDishes(self):
        self.Dishes.setVisible(True)
        self.Orders.setVisible(False)

    def back(self):
        self.manager.changeMaket(WindowName.WELCOME_WINDOW)