# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AdminZqvFKM.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AdminWelcome(object):
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
    # retranslateUi

