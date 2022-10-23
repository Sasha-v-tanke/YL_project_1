import sys, os.path, sqlite3
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication
from Exceptions import *
from Constants import *
from Enums import WindowName


class Window(QMainWindow):
    def __init__(self, manager):
        self.manager = manager
        super().__init__()

    def changeMaket(self,  maket: str):
        try:
            if '.ui' not in maket:
                raise NameFileException
            elif not os.path.exists(maket):
                raise DirectoryFileException
            else:
                uic.loadUi(maket, self)
                return True
        except Exception as exc:
            print(exc)
            return False


class WelcomeWindow(Window):
    def __init__(self, manager):
        super().__init__(manager)
        if self.changeMaket(PATH_UI_WELCOME_WINDOW):
            self.GoToAdminAccount.clicked.connect(self.goToAdminMenu)
            self.NewOrder.clicked.connect(self.openUserWindow)

    def goToAdminMenu(self):
        #self.manager.changeMaket(WindowName.ADMIN_WINDOW)
        self.manager.changeMaket(WindowName.CREATOR_WINDOW)

    def openUserWindow(self):
        self.manager.changeMaket(WindowName.SHOP_WINDOW)


class AdminWindow(Window):
    def __init__(self, manager):
        super().__init__(manager)
        if self.changeMaket(PATH_UI_ADMIN_WINDOW):
            self.Check.clicked.connect(self.check)
            self.BackToWelcome.clicked.connect(self.back)

    def back(self):
        self.manager.changeMaket(WindowName.WELCOME_WINDOW)

    def check(self):
        login = self.Login.text()
        password = self.Password.text()
        try:
            if not os.path.exists(ACCOUNTS_DB):
                raise DirectoryFileException
            else:
                con = sqlite3.connect(ACCOUNTS_DB)
                cur = con.cursor()
                res = cur.execute("""SELECT password FROM accounts
                    WHERE login = ?""", (login,)).fetchall()
                if len(res) == 0:
                    self.Check.setText("Wrong login or password.\n Please try again")
                elif password == res[0][0]:
                    self.manager.changeMaket(WindowName.CREATOR_WINDOW)
                else:
                    self.Check.setText("Wrong login or password.\n Please try again")
                con.close()
        except Exception as exc:
            print(exc)
            

class UserWindow(Window):
    def __init__(self, manager):
        super().__init__(manager)
        if self.changeMaket(PATH_UI_SHOP_WINDOW):
            self.BackToWelcome.clicked.connect(self.back)
            #self.load()

    def back(self):
        self.manager.changeMaket(WindowName.WELCOME_WINDOW)


class CreatorWindow(Window):
    def __init__(self, manager):
        super().__init__(manager)
        if self.changeMaket(PATH_UI_CREATOR_WINDOW):
            self.BackToWelcome.clicked.connect(self.back)
            self.load()

    def back(self):
        self.manager.changeMaket(WindowName.WELCOME_WINDOW)

    def load(self):
        try:
            if not os.path.exists(MENU_DB):
                raise DirectoryFileException
            else:
                self.NewTab.clicked.connect(self.newTab)
                con = sqlite3.connect(MENU_DB)
                cur = con.cursor()
                res = cur.execute("""SELECT title FROM categories""").fetchall()
                self.Categories.setTabBarAutoHide(True)
                self.Categories_ = []
                for title in res:
                    NewCategory = QWidget()
                    NewCategory.setObjectName(title[0][0])
                    self.Categories_.append(NewCategory)
                    self.Categories.addTab(NewCategory, "")
                    self.Categories.setTabText(self.Categories.indexOf(NewCategory), QCoreApplication.translate("MainWindow", title[0], None))
                    dishes = cur.execute("""SELECT 
                                                dishes.title, 
                                                dishes.price
                                            FROM Dishes
                                            INNER JOIN Categories
                                            ON Categories.CategoryId = dishes.CategoryId
                                            WHERE Categories.title = ?""", (title[0],)).fetchall()
                    for i in range(len(dishes)):
                        pushButton = QPushButton(NewCategory)
                        pushButton.setObjectName("Btn" + str(i))
                        pushButton.move(20, 40 + 70 * i)
                        pushButton.resize(150, 50)
                        pushButton.setText(QCoreApplication.translate("MainWindow", dishes[i][0] + "\t\t" + str(dishes[i][1]), None))
                con.close()
        except Exception as exc:
            print(exc)

    def newTab(self):
        pass

    def newDish(self):
        pass



def start():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())




"""
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Categories = QTabWidget(self.centralwidget)
        self.Categories.setObjectName(u"Categories")
        self.Categories.setGeometry(QRect(20, 30, 760, 560))
        self.Categories.setTabPosition(QTabWidget.North)
        self.Categories.setTabShape(QTabWidget.Triangular)
        self.Categories.setDocumentMode(False)
        self.Categories.setMovable(False)
        self.Categories.setTabBarAutoHide(True)
        self.Category1 = QWidget()
        self.Category1.setObjectName(u"Category1")
        self.pushButton = QPushButton(self.Category1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 20, 101, 101))
        self.Categories.addTab(self.Category1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.Categories.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Categories.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0411\u041b\u042e\u0414\u041e 1", None))
        self.Categories.setTabText(self.Categories.indexOf(self.Category1), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.Categories.setTabText(self.Categories.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.BackToWelcome.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0410\u0417\u0410\u0414", None))
    # retranslateUi

"""