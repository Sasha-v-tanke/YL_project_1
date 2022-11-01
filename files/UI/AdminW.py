try:
    from Windows import Window

    import sys, os.path, sqlite3

    from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
    from PyQt5.QtCore import QCoreApplication, QSize, QRect

    from Enums import WindowName
    from Constants import *
except Exception as exc:
    print(exc)


class AdminW(QWidget):    
    def __init__(self, manager):
        self.manager = manager
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setGeometry(0, 0, 0, 0)
        self.setMinimumSize(QSize(*SIZE_W))
        self.setMaximumSize(QSize(*SIZE_W))
        self.setWindowTitle("Вход в аккаунт")

        self.Password = QLineEdit(self)
        self.Password.setGeometry(QRect(325, 240, 150, 40))
        self.Password.setMaxLength(20)
        self.Password.setText("12345")

        self.Login = QLineEdit(self)
        self.Login.setGeometry(QRect(325, 170, 150, 40))
        self.Login.setMaxLength(20)
        self.Login.setText("login")

        self.Check = QPushButton(self)
        self.Check.setGeometry(QRect(330, 310, 140, 50))
        self.Check.setText("ВОЙТИ")
        self.Check.clicked.connect(self.check)

        self.BackToWelcome = QPushButton(self)
        self.BackToWelcome.setGeometry(QRect(30, 20, 75, 23))
        self.BackToWelcome.setText("НАЗАД")
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

