from Windows import Window

import sys, os.path, sqlite3

from PyQt5.QtWidgets import QPushButton, QLineEdit, QTabWidget, QFormLayout, QScrollArea, QTableWidget, QAbstractItemView, QTableWidgetItem, QGroupBox, QCheckBox, QLabel
from PyQt5.QtCore import QRect
from Enums import WindowName
from Constants import SIZE_W, MENU_DB


class ShopW(Window):
    def setupUI(self):
        self.lst = []
        self.boxes = {}
        self.titles = ["Title", "Price"]

        self.con = sqlite3.connect(MENU_DB)
        self.cur = self.con.cursor()
        self.setWindowTitle("Меню")

        self.Basket = QPushButton(self)
        self.Basket.setGeometry(QRect(SIZE_W[0] - 100, SIZE_W[1] - 25, 100, 25))
        self.Basket.setText("Корзина")
        self.Basket.clicked.connect(self.basket)

        self.BackToWelcome = QPushButton(self)
        self.BackToWelcome.setGeometry(QRect(10, 0, 75, 25))
        self.BackToWelcome.setText("Назад")
        self.BackToWelcome.clicked.connect(self.back)

        self.Categories = QTabWidget(self)
        self.Categories.setGeometry(QRect(10, 25, 780, 550))
        
        self.loadMenu()

    def loadMenu(self):
        res = self.cur.execute("""SELECT Title, CategoryId FROM Categories""").fetchall()
        for number, category in enumerate(res):
            scroll = QScrollArea()
            form = QFormLayout(scroll)
            form.setHorizontalSpacing(200)
            dishes = self.cur.execute("""SELECT 
                            Dishes.Title, Dishes.Price, Dishes.DishId
                            FROM Dishes
                            INNER JOIN Categories
                            ON Categories.CategoryId = Dishes.CategoryId
                            WHERE Categories.Title = ?""", (category[0],)).fetchall()
            for number, dish in enumerate(dishes):
                ch = QCheckBox(dish[0])
                self.boxes[ch] = dish[2]
                ch.stateChanged.connect(self.change)
                form.addRow(ch, QLabel(str(dish[1])))
            self.Categories.addTab(scroll, category[0])

    def change(self, state):
        if state:
            self.add(self.boxes[self.sender()])
        else:
            self.remove(self.boxes[self.sender()])

    def remove(self, id):
        self.lst.remove(id)

    def add(self, id):
        self.lst.append(id)

    def basket(self):
        self.manager.setOffer(self.lst)

    def __del__(self):
        self.con.close()

    def addOffer(self, lst):
        self.lst = lst
        for elem in lst:
            ind = list(self.boxes.values()).index(elem)
            key = list(self.boxes.keys())[ind].setCheckState(True)

    def back(self):
        self.manager.changeMaket(WindowName.WELCOME_WINDOW)