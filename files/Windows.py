from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QSize
from Constants import SIZE_W


class Window(QWidget):
    def __init__(self, manager):
        self.manager = manager
        super().__init__()
        self.setGeometry(0, 0, 0, 0)
        self.setMinimumSize(QSize(*SIZE_W))
        self.setMaximumSize(QSize(*SIZE_W))
        self.setupUI()
        
    def setupUI(self):
        pass