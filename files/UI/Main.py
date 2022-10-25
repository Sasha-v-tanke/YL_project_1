# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainHzSByF.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_WelcomeWindow(object):
    def setupUi(self, WelcomeWindow):
        if not WelcomeWindow.objectName():
            WelcomeWindow.setObjectName(u"WelcomeWindow")
        WelcomeWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WelcomeWindow.sizePolicy().hasHeightForWidth())
        WelcomeWindow.setSizePolicy(sizePolicy)
        WelcomeWindow.setMinimumSize(QSize(800, 600))
        WelcomeWindow.setMaximumSize(QSize(800, 600))
        self.centralwidget = QWidget(WelcomeWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.NewOrder = QPushButton(self.centralwidget)
        self.NewOrder.setObjectName(u"NewOrder")
        self.NewOrder.setGeometry(QRect(340, 250, 120, 100))
        self.GoToAdminAccount = QPushButton(self.centralwidget)
        self.GoToAdminAccount.setObjectName(u"GoToAdminAccount")
        self.GoToAdminAccount.setGeometry(QRect(630, 560, 160, 30))
        WelcomeWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(WelcomeWindow)

        QMetaObject.connectSlotsByName(WelcomeWindow)
    # setupUi

    def retranslateUi(self, WelcomeWindow):
        WelcomeWindow.setWindowTitle(QCoreApplication.translate("WelcomeWindow", u"MainWindow", None))
        self.NewOrder.setText(QCoreApplication.translate("WelcomeWindow", u"\u041d\u041e\u0412\u042b\u0419 \u0417\u0410\u041a\u0410\u0417", None))
        self.GoToAdminAccount.setText(QCoreApplication.translate("WelcomeWindow", u"\u0412\u041e\u0419\u0422\u0418 \u041a\u0410\u041a \u0410\u0414\u041c\u0418\u041d\u0418\u0421\u0422\u0420\u0410\u0422\u041e\u0420", None))
    # retranslateUi

