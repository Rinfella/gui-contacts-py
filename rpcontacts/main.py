# -*- coding: utf-8 -*- 
# rpcontacts/main.property

"""This module provides the rpcontacts application."""

import sys

from PyQt5.QtWidgets import QApplication

from .views import Window

def main():
    """RP Contacts main function"""
    # Create application
    app = QApplication(sys.argv)
    # Create and show main window
    win = Window()
    win.show()
    # Run the event loop
    sys.exit(app.exec_())
    

