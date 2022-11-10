from Windows import Window

import sqlite3

from PyQt5.QtWidgets import QPushButton, QTabWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QMessageBox, QAbstractItemView, QInputDialog
from PyQt5.QtCore import QRect, Qt

from Enums import WindowName
from Constants import SIZE_W, MENU_DB, ACCOUNTS_DB

class CreatorW(Window):
    def back(self):
        self.manager.changeMaket(WindowName.WELCOME_WINDOW)

    def setupUI(self):
        self.con = sqlite3.connect(MENU_DB)
        self.cur = self.con.cursor()
        self.con2 = sqlite3.connect(ACCOUNTS_DB)
        self.cur2 = self.con2.cursor()
        self.setWindowTitle("Редактор меню")

        self.BackToWelcome = QPushButton(self)
        self.BackToWelcome.setGeometry(QRect(10, 0, 75, 25))
        self.BackToWelcome.setText("Назад")
        self.BackToWelcome.clicked.connect(self.back)

        self.ConfirmDish = QPushButton(self)
        self.ConfirmDish.setGeometry(QRect(SIZE_W[0] - 90, SIZE_W[1] - 25, 25, 25))
        self.ConfirmDish.setText("V")
        self.ConfirmDish.clicked.connect(self.confirmEdit)

        self.CancelDish = QPushButton(self)
        self.CancelDish.setGeometry(QRect(SIZE_W[0] - 50, SIZE_W[1] - 25, 25, 25))
        self.CancelDish.setText("X")
        self.CancelDish.clicked.connect(self.cancelEdit)

        self.NewNameCategory = QLineEdit(self)
        self.NewNameCategory.setMaxLength(44)
        self.NewNameCategory.setGeometry(QRect(120, 0, 270, 25))
        self.NewNameCategory.setText("новая категория")

        self.EditName = QPushButton(self)
        self.EditName.setGeometry(QRect(SIZE_W[0] / 2, 0, 25, 25))
        self.EditName.setText("V")
        self.EditName.clicked.connect(self.editNameCategory)

        self.NewIdCategory = QLineEdit(self)
        self.NewIdCategory.setMaxLength(5)
        self.NewIdCategory.setGeometry(QRect(500, 0, 50, 25))
        self.NewIdCategory.setText("0")

        self.EditId = QPushButton(self)
        self.EditId.setGeometry(QRect(555, 0, 25, 25))
        self.EditId.setText("V")
        self.EditId.clicked.connect(self.editIdCategory)

        self.NewCategory = QPushButton(self)
        self.NewCategory.setGeometry(QRect(600, 0, 100, 25))
        self.NewCategory.setText("новая категория")
        self.NewCategory.clicked.connect(self.newCategory)

        self.DeleteCategory = QPushButton(self)
        self.DeleteCategory.setGeometry(QRect(760, 0, 25, 25))
        self.DeleteCategory.setText("X")
        self.DeleteCategory.clicked.connect(self.deleteCategory)

        self.NewDish = QPushButton(self)
        self.NewDish.setGeometry(QRect(250, SIZE_W[1] - 25, 100, 25))
        self.NewDish.setText("новое блюдо")
        self.NewDish.clicked.connect(self.newDish)

        self.DeleteDish = QPushButton(self)
        self.DeleteDish.setGeometry(QRect(450, SIZE_W[1] - 25, 100, 25))
        self.DeleteDish.setText("удалить блюдо")
        self.DeleteDish.clicked.connect(self.deleteDish)

        self.Categories = QTabWidget(self)
        self.Categories.setGeometry(QRect(10, 25, 780, 550))
        
        self.changes = {}
        self.loadMenu()

    def setSettings(self, tabIndex):
        if tabIndex < len(self.tabs):
            self.Categories.setCurrentIndex(tabIndex)

    def update(self):
        self.manager.updateCreator(self.Categories.currentIndex())

    def newDish(self):
        dishes = [e[0] for e in self.cur.execute("""SELECT Title FROM Dishes""").fetchall()]
        i = 1
        ids = [e[0] for e in self.cur.execute("""SELECT DishId FROM Dishes""").fetchall()]
        id = 0
        while id in ids:
            id += 1
        categoryId = self.cur.execute("""SELECT CategoryId FROM Categories WHERE Title = ?""", 
                              (self.Categories.tabText(self.Categories.currentIndex()).split('_')[0],)).fetchone()[0]
        while ('новое блюдо ' + str(i)) in dishes:
            i += 1
        self.cur.execute("""INSERT INTO dishes(DishId, CategoryId, Title) VALUES(?, ?, ?)""", 
                         (id, categoryId, 'новое блюдо ' + str(i),)).fetchall()
        self.con.commit()
        self.update()

    def deleteDish(self):
        tab = self.tabs[self.Categories.currentIndex()]
        rows = list(set([i.row() for i in tab.selectedItems()]))
        titles = [tab.item(i, 0).text() for i in rows]
        if not titles:
            return
        valid = QMessageBox.question(
            self, '', "Действительно удалить элементы: " + ", ".join(titles),
            QMessageBox.Yes, QMessageBox.No)
        if valid == QMessageBox.Yes:
            for title in titles:
                self.cur.execute("""DELETE from Dishes WHERE Title = ?""", (title,))
            self.con.commit()
            self.update()

    def deleteCategory(self):
        dishesCategoryId = [e[0] for e in self.cur.execute("""SELECT CategoryId FROM Dishes""").fetchall()]
        categoryId = [e[0] for e in self.cur.execute("""SELECT CategoryId FROM Categories WHERE Title = ?""", 
                                                (self.Categories.tabText(self.Categories.currentIndex()).split('_')[0],)).fetchall()][0]
        if categoryId not in dishesCategoryId:
            self.cur.execute("""DELETE from Categories
                            WHERE Title = ?""",    
                            (self.Categories.tabText(self.Categories.currentIndex()).split('_')[0],)).fetchall()
            self.con.commit()
            self.update()

    def newCategory(self):
        categories = [e[0] for e in self.cur.execute("""SELECT Title FROM Categories""").fetchall()]
        ids = [e[0] for e in self.cur.execute("""SELECT CategoryId FROM Categories""").fetchall()]
        id = 0
        i = 1
        while ('новая категория ' + str(i)) in categories:
            i += 1
        while id in ids:
            id += 1
        self.cur.execute("""INSERT INTO Categories(CategoryId, Title) VALUES(?, ?)""", 
                         (str(id), 'новая категория ' + str(i),))
        self.con.commit()
        self.update()

    def editNameCategory(self):
        title = self.NewNameCategory.text()
        categories = [e[0] for e in self.cur.execute("""SELECT Title FROM Categories""").fetchall()]
        if '_' in title:
            return
        if title in categories and title != self.Categories.tabText(self.Categories.currentIndex()):
            return
        if not len(title):
            return
        self.cur.execute("""UPDATE Categories SET Title = ? WHERE Title = ?""",
                    (title, self.Categories.tabText(self.Categories.currentIndex()).split('_')[0]))
        self.con.commit()
        self.update()

    def editIdCategory(self):
        id = self.NewIdCategory.text()
        if '.' in id:
            return
        try:
            id = int(id)
        except:
            pass
        else:
            ids = [e[0] for e in self.cur.execute("""SELECT CategoryId from Categories""").fetchall()]
            if id in ids:
                return
            self.cur.execute("""UPDATE Categories SET CategoryId = ? WHERE Title = ?""",
                    (id, self.Categories.tabText(self.Categories.currentIndex()).split('_')[0]))
            self.con.commit()
            self.update()
        
    def confirmEdit(self):
        if not self.changes.keys():
            return
        que = "UPDATE Dishes\nSET "
        que += ", ".join([f"{self.changes.get(key)[1]} = {self.changes.get(key)[0]}\nWHERE Title = '{key}'"
                          for key in self.changes.keys()])
        try:
            self.cur.execute(que)
        except:
            pass
        else:
            self.con.commit()
            self.update()

    def cancelEdit(self):
        if not self.changes.keys():
            return
        self.changes = {}
        self.update()

    def itemChanged(self, item):
        title = self.tabs[self.Categories.currentIndex()].item(item.row(), 0).text()
        self.changes[title] = (item.text(), self.titles[item.column()])
        
    def __del__(self):
        self.con.close()

    def keyPressEvent(self, event):
        if int(event.modifiers()) == (Qt.AltModifier + Qt.ShiftModifier):
            if event.key() == Qt.Key_N:
                key = QInputDialog.getText(self, "Новый аккаунт", "код активации:")[0]
                if key != "YL_2022":
                    QMessageBox.question(self, '', 
                            "Неверный код", QMessageBox.Yes)
                    return
                login = QInputDialog.getText(self, "Новый аккаунт", "логин:")[0]
                accounts = self.cur2.execute("""SELECT Login, Password FROM Accounts""").fetchall()
                if login in [e[0] for e in accounts]:
                    QMessageBox.question(self, '', 
                            "Такой логин уже существует", QMessageBox.Yes)
                    return
                password = QInputDialog.getText(self, "Новый аккаунт", "пароль:")[0]
                if password in [e[1] for e in accounts]:
                    QMessageBox.question(self, '', 
                            "Такой пароль уже существует", QMessageBox.Yes)
                    return
                self.cur2.execute("""INSERT INTO Accounts VALUES(?, ?)""", (login, password))
                self.con2.commit()
            
            if event.key() == Qt.Key_P:
                newPassword = QInputDialog.getText(self, "Смена пароля", "Новый пароль: ")[0]
                if password in [e[1] for e in accounts]:
                    QMessageBox.question(self, '', 
                            "Такой пароль уже существует", QMessageBox.Yes)
                    return
                self.cur2.execute("""UPDATE Accounts SET Password = ? WHERE Password = ?""",
                    (newPassword, self.manager.getPassword()))
                self.con2.commit()

    def loadMenu(self):
        self.tabs = []
        self.titles = ["Title", "Price", "CategoryId"]
        res = self.cur.execute("""SELECT Title, CategoryId FROM Categories""").fetchall()
        for number, category in enumerate(res):
            table = QTableWidget()
            self.tabs.append(table)
            dishes = self.cur.execute("""SELECT 
                            Dishes.Title, Dishes.Price, Dishes.CategoryId
                            FROM Dishes
                            INNER JOIN Categories
                            ON Categories.CategoryId = Dishes.CategoryId
                            WHERE Categories.Title = ?""", (category[0],)).fetchall()
            if dishes:
                table.setRowCount(len(dishes))
                table.setColumnCount(len(dishes[0]))
                for n_row, row in enumerate(dishes):
                    for n_elem, val in enumerate(row):
                        table.setItem(n_row, n_elem, QTableWidgetItem(str(val)))
            self.Categories.addTab(table, category[0] + "_" + str(res[number][1]))
            table.itemChanged.connect(self.itemChanged)
            table.setHorizontalHeaderLabels(self.titles)