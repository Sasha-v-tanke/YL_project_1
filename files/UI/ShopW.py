from Windows import Window

import sqlite3

from PyQt5.QtWidgets import QPushButton, QTabWidget, QFormLayout, QScrollArea, QGroupBox, QCheckBox, QLabel
from PyQt5.QtCore import QRect
from Enums import WindowName
from Constants import SIZE_W, MENU_DB


class ShopW(Window):
    def setupUI(self):
        self.lst = list()
        self.boxes = {}
        self.titles = ["Title", "Price"]

        self.con = sqlite3.connect(MENU_DB)
        self.cur = self.con.cursor()
        self.setWindowTitle("Меню")

        size = (100, 25)
        self.Basket = QPushButton(self)
        self.Basket.setGeometry(QRect(SIZE_W[0] - size[0], SIZE_W[1] - size[1], *size))
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
        categories = self.cur.execute("""SELECT Title, CategoryId FROM Categories""").fetchall()
        for number, category in enumerate(categories):
            Scroll = QScrollArea()
            Form = QFormLayout(Scroll)
            Form.setHorizontalSpacing(200)
            dishes = self.cur.execute("""SELECT 
                            Dishes.Title, Dishes.Price, Dishes.DishId
                            FROM Dishes
                            INNER JOIN Categories
                            ON Categories.CategoryId = Dishes.CategoryId
                            WHERE Categories.Title = ?""", (category[0],)).fetchall()
            for number, dish in enumerate(dishes):
                CheckBox = QCheckBox(dish[0])
                self.boxes[CheckBox] = dish[2]
                CheckBox.stateChanged.connect(self.change)
                Form.addRow(CheckBox, QLabel(str(dish[1])))
            self.Categories.addTab(Scroll, category[0])

    def change(self, state):
        if state:
            self.lst.append(self.boxes[self.sender()])
        else:
            self.lst.remove(self.boxes[self.sender()])

    def basket(self):
        if self.lst:
            self.manager.setOffer(self.lst)

    def __del__(self):
        self.con.close()

    def addOffer(self, lst):
        for elem in lst:
            ind = list(self.boxes.values()).index(elem)
            list(self.boxes.keys())[ind].setCheckState(True)

    def back(self):
        self.manager.changeMaket(WindowName.WELCOME_WINDOW)