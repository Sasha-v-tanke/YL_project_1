# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OrdersPrsXWp.ui'
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
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(40, 40, 701, 511))
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setTabletTracking(False)
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setDocumentMode(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-10, 20, 621, 391))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 50, 100, 25))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 110, 100, 25))
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 170, 100, 25))
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 230, 100, 25))
        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(455, 50, 47, 13))
        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(455, 110, 47, 13))
        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(455, 170, 47, 13))
        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(455, 230, 47, 13))
        self.verticalScrollBar = QScrollBar(self.tab)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(670, 20, 16, 451))
        self.verticalScrollBar.setOrientation(Qt.Vertical)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.frame_2 = QFrame(self.tab_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 20, 661, 431))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 201, 151))
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 20, 171, 16))
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 50, 171, 16))
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 80, 171, 16))
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 110, 171, 16))
        self.groupBox_2 = QGroupBox(self.frame_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 180, 201, 151))
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 20, 171, 16))
        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 50, 171, 16))
        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 80, 171, 16))
        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 110, 171, 16))
        self.verticalScrollBar_2 = QScrollBar(self.tab_2)
        self.verticalScrollBar_2.setObjectName(u"verticalScrollBar_2")
        self.verticalScrollBar_2.setGeometry(QRect(680, 10, 16, 461))
        self.verticalScrollBar_2.setOrientation(Qt.Vertical)
        self.tabWidget.addTab(self.tab_2, "")
        self.BackToWelcome = QPushButton(self.centralwidget)
        self.BackToWelcome.setObjectName(u"BackToWelcome")
        self.BackToWelcome.setGeometry(QRect(20, 10, 75, 23))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Dish1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Dish4", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Dish3", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Dish6", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"x5", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"x5", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"x5", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"x5", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0430\u0437 1", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0411\u043b\u044e\u0434\u043e1 \u04452", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0411\u043b\u044e\u0434\u043e2 \u04453", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0411\u043b\u044e\u0434\u043e3 \u04451", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0411\u043b\u044e\u0434\u043e5 x4", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0430\u0437 2", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0411\u043b\u044e\u0434\u043e1 \u04451", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0411\u043b\u044e\u0434\u043e2 \u04452", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0411\u043b\u044e\u0434\u043e3 \u04453", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0411\u043b\u044e\u0434\u043e4 \u04451", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.BackToWelcome.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0410\u0417\u0410\u0414", None))
    # retranslateUi
