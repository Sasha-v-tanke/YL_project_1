from Windows import Window

import os.path, sqlite3

from PyQt5.QtWidgets import QPushButton, QLineEdit
from PyQt5.QtCore import QRect

from Enums import WindowName
from Constants import ACCOUNTS_DB, SIZE_W


class AdminW(Window):
    def setupUI(self):
        self.setWindowTitle("Вход в аккаунт")

        maxLength = 20
        size = (150, 40)

        self.Login = QLineEdit(self)
        self.Login.setGeometry(QRect((SIZE_W[0] - size[0]) / 2, SIZE_W[1] / 2 - size[1] * 0.7, *size))
        self.Login.setMaxLength(maxLength)
        self.Login.setText("login")

        self.Password = QLineEdit(self)
        self.Password.setGeometry(QRect((SIZE_W[0] - size[0]) / 2, SIZE_W[1] / 2 + size[1] * 0.7, *size))
        self.Password.setMaxLength(maxLength)
        self.Password.setText("12345")
            
        self.Check = QPushButton(self)
        self.Check.setGeometry(QRect((SIZE_W[0] - size[0]) / 2, SIZE_W[1] / 2 + 2.2 * size[1], *size))
        self.Check.setText("Войти")
        self.Check.clicked.connect(self.check)
        
        size = (80, 30)
        self.BackToWelcome = QPushButton(self)
        self.BackToWelcome.setGeometry(QRect(size[0] * 0.7, size[1] * 0.7, *size))
        self.BackToWelcome.setText("Назад")
        self.BackToWelcome.clicked.connect(self.back)
        
    def back(self):
        self.manager.changeMaket(WindowName.WELCOME_WINDOW)

    def check(self):
        login = self.Login.text()
        password = self.Password.text()
        
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

