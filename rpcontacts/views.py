# -*- coding: utf-8 -*- 

"""This module provides views to manage the contacts table"""

from PyQt5.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QWidget,
)

class Window(QMainWindow):
    """Main Window"""
    def __init__(self, parent=None):
        """Initilaizer"""
        super().__init__(parent)
        self.setWindowTitle("Contacts")
        self.resize(800, 600)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)
