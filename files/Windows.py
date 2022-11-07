import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QSize
from Exceptions import *
from Constants import SIZE_W
from Enums import WindowName


class Window(QWidget):
    def __init__(self, manager):
        self.manager = manager
        super().__init__()
        self.widget = QWidget(self)
        self.setGeometry(0, 0, 0, 0)
        self.setMinimumSize(QSize(*SIZE_W))
        self.setMaximumSize(QSize(*SIZE_W))
        self.setupUI()
        
    def setupUI(self):
        pass


def start():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
