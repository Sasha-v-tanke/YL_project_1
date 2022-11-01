try:
    import sys, os.path, sqlite3
    from PyQt5 import uic, QtCore, QtGui
    from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
    from PyQt5.QtCore import QCoreApplication
    from Exceptions import *
    from Constants import *
    from Enums import WindowName

    from PySide2.QtCore import *
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *
except Exception as exc:
            print(exc)


class Window(QWidget):
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


class AdminWindow(Window):
    def __init__(self, manager):
        super().__init__(manager)
        self.setupUi(self)
        #if self.changeMaket(PATH_UI_ADMIN_WINDOW):
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

    def setupUi(self, AdminWelcome):
        if not AdminWelcome.objectName():
            AdminWelcome.setObjectName(u"AdminWelcome")
        AdminWelcome.resize(800, 600)
        self.centralwidget = QWidget(AdminWelcome)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Password = QLineEdit(self.centralwidget)
        self.Password.setObjectName(u"Password")
        self.Password.setGeometry(QRect(325, 240, 150, 40))
        self.Password.setMaxLength(20)
        self.Password.setFrame(True)
        self.Password.setDragEnabled(False)
        self.Login = QLineEdit(self.centralwidget)
        self.Login.setObjectName(u"Login")
        self.Login.setGeometry(QRect(325, 170, 150, 40))
        self.Login.setMaxLength(20)
        self.Check = QPushButton(self.centralwidget)
        self.Check.setObjectName(u"Check")
        self.Check.setGeometry(QRect(330, 310, 140, 50))
        self.BackToWelcome = QPushButton(self.centralwidget)
        self.BackToWelcome.setObjectName(u"BackToWelcome")
        self.BackToWelcome.setGeometry(QRect(30, 20, 75, 23))
        AdminWelcome.setCentralWidget(self.centralwidget)

        self.retranslateUi(AdminWelcome)

        QMetaObject.connectSlotsByName(AdminWelcome)
    # setupUi

    def retranslateUi(self, AdminWelcome):
        AdminWelcome.setWindowTitle(QCoreApplication.translate("AdminWelcome", u"MainWindow", None))
        self.Password.setText(QCoreApplication.translate("AdminWelcome", u"password", None))
        self.Login.setText(QCoreApplication.translate("AdminWelcome", u"login", None))
        self.Check.setText(QCoreApplication.translate("AdminWelcome", u"\u0412\u041e\u0419\u0422\u0418", None))
        self.BackToWelcome.setText(QCoreApplication.translate("AdminWelcome", u"\u041d\u0410\u0417\u0410\u0414", None))
           

class BasketWindow(Window):
    def __init__(self, manager):
        super().__init__(manager)
        self.setupUi(self)
    
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalScrollBar = QScrollBar(self.centralwidget)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(740, 90, 20, 381))
        self.verticalScrollBar.setOrientation(Qt.Vertical)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(50, 80, 621, 391))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.checkBox = QCheckBox(self.frame)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(30, 50, 200, 25))
        self.checkBox.setChecked(True)
        self.spinBox = QSpinBox(self.frame)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(470, 50, 40, 25))
        self.spinBox.setValue(2)
        self.checkBox_2 = QCheckBox(self.frame)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(30, 110, 200, 25))
        self.checkBox_2.setChecked(True)
        self.spinBox_2 = QSpinBox(self.frame)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setGeometry(QRect(470, 110, 40, 25))
        self.spinBox_2.setValue(1)
        self.checkBox_3 = QCheckBox(self.frame)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(30, 170, 200, 25))
        self.checkBox_3.setChecked(True)
        self.spinBox_3 = QSpinBox(self.frame)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setGeometry(QRect(470, 170, 40, 25))
        self.spinBox_3.setValue(3)
        self.checkBox_4 = QCheckBox(self.frame)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(30, 230, 200, 25))
        self.checkBox_4.setTabletTracking(False)
        self.checkBox_4.setAcceptDrops(False)
        self.checkBox_4.setChecked(True)
        self.spinBox_4 = QSpinBox(self.frame)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setGeometry(QRect(470, 230, 40, 25))
        self.spinBox_4.setValue(1)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(370, 50, 71, 21))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(370, 110, 71, 21))
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(370, 170, 71, 21))
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(370, 230, 71, 21))
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(370, 0, 71, 21))
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 0, 70, 20))
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(460, 0, 71, 21))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(470, 510, 181, 61))
        self.BackToWelcome = QPushButton(self.centralwidget)
        self.BackToWelcome.setObjectName(u"BackToWelcome")
        self.BackToWelcome.setGeometry(QRect(20, 20, 75, 23))
        self.Sum = QLabel(self.centralwidget)
        self.Sum.setObjectName(u"Sum")
        self.Sum.setGeometry(QRect(220, 520, 91, 31))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Dish1", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Dish2", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Dish3", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Dish4", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"150", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"75", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0430", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0430\u0437\u0430\u0442\u044c", None))
        self.BackToWelcome.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0410\u0417\u0410\u0414", None))
        self.Sum.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0442\u043e\u0433\u043e: 825", None))


class CreatorWindow(Window):
    def __init__(self, manager):
        super().__init__(manager)
        self.setupUi(self)
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
                        pushButton.move(20, 110 + 70 * i)
                        pushButton.resize(150, 50)
                        pushButton.setText(QCoreApplication.translate("MainWindow", dishes[i][0] + "\t\t" + str(dishes[i][1]), None))
                
                    pushButton = QPushButton(NewCategory)
                    pushButton.setObjectName("NewDish")
                    pushButton.move(20, 40)
                    pushButton.resize(150, 50)
                    pushButton.setText(QCoreApplication.translate("MainWindow", "Новое блюдо", None))
                con.close()
        except Exception as exc:
            print(exc)

    def newTab(self):
        pass

    def newDish(self):
        pass

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Categories = QTabWidget(self.centralwidget)
        self.Categories.setObjectName(u"Categories")
        self.Categories.setGeometry(QRect(20, 30, 731, 560))
        self.Categories.setTabPosition(QTabWidget.North)
        self.Categories.setTabShape(QTabWidget.Triangular)
        self.Categories.setDocumentMode(False)
        self.Categories.setMovable(False)
        self.Categories.setTabBarAutoHide(True)
        self.BackToWelcome = QPushButton(self.centralwidget)
        self.BackToWelcome.setObjectName(u"BackToWelcome")
        self.BackToWelcome.setGeometry(QRect(10, 0, 75, 23))
        self.NewTab = QPushButton(self.centralwidget)
        self.NewTab.setObjectName(u"NewTab")
        self.NewTab.setGeometry(QRect(753, 30, 25, 25))
        self.ScrollBar = QScrollBar(self.centralwidget)
        self.ScrollBar.setObjectName(u"ScrollBar")
        self.ScrollBar.setGeometry(QRect(753, 60, 25, 525))
        self.ScrollBar.setOrientation(Qt.Vertical)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Categories.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.BackToWelcome.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0410\u0417\u0410\u0414", None))
        self.NewTab.setText(QCoreApplication.translate("MainWindow", u"+", None))


class ShopWindow(Window):
    def __init__(self, manager):
        super().__init__(manager)
        self.setupUi(self)
        self.BackToWelcome.clicked.connect(self.back)
        self.GoToBasket.clicked.connect(self.basket)
        self.load()

    def basket(self):
        self.manager.changeMaket(WindowName.BASKET_WINDOW)

    def back(self):
        self.manager.changeMaket(WindowName.WELCOME_WINDOW)

    def load(self):
        try:
            if not os.path.exists(MENU_DB):
                raise DirectoryFileException
            else:
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

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Categories = QTabWidget(self.centralwidget)
        self.Categories.setObjectName(u"Categories")
        self.Categories.setGeometry(QRect(0, 50, 800, 501))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Categories.sizePolicy().hasHeightForWidth())
        self.Categories.setSizePolicy(sizePolicy)
        self.Categories.setLayoutDirection(Qt.LeftToRight)
        self.Categories.setAutoFillBackground(False)
        self.Categories.setTabPosition(QTabWidget.North)
        self.Categories.setTabShape(QTabWidget.Triangular)
        self.Categories.setElideMode(Qt.ElideMiddle)
        self.Categories.setUsesScrollButtons(True)
        self.Categories.setDocumentMode(False)
        self.Categories.setTabsClosable(False)
        self.Categories.setMovable(True)
        self.Categories.setTabBarAutoHide(False)
        self.GoToBasket = QPushButton(self.centralwidget)
        self.GoToBasket.setObjectName(u"GoToBasket")
        self.GoToBasket.setGeometry(QRect(670, 560, 120, 30))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.GoToBasket.sizePolicy().hasHeightForWidth())
        self.GoToBasket.setSizePolicy(sizePolicy1)
        self.BackToWelcome = QPushButton(self.centralwidget)
        self.BackToWelcome.setObjectName(u"BackToWelcome")
        self.BackToWelcome.setGeometry(QRect(10, 10, 75, 23))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Categories.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.GoToBasket.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0415\u0420\u0415\u0419\u0422\u0418 \u0412 \u041a\u041e\u0420\u0417\u0418\u041d\u0423", None))
        self.BackToWelcome.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0410\u0417\u0410\u0414", None))



def start():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
