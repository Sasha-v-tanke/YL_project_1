# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ShopEisCGl.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
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
    # retranslateUi

