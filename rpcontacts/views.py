# -*- coding: utf-8 -*- 

"""This module provides views to manage the contacts table"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
)

from .model import ContactsModel

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
        
        self.contactsModel = ContactsModel()
        self.setupUI()

    def setupUI(self):
        """Set the main window's GUI"""
        # Create the table view widget
        self.table = QTableView()
        self.table.setModel(self.contactsModel.model)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()
        # Create buttons
        self.addButton = QPushButton("Add")
        self.addButton.clicked.connect(self.openAddDialog)
        self.deleteButton = QPushButton("Delete")
        self.deleteButton.clicked.connect(self.deleteContact)
        self.clearAllButton = QPushButton("Clear All")
        self.clearAllButton.clicked.connect(self.clearContacts)
        # Lay out the GUI
        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addStrech()
        layout.addWidget(self.clearAllButton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)

class AddDialog(QDialog):
    """Add Contact dialog"""
    def __init__(self, parent=None):
        """Initializer"""
        super().__init__(parent=parent)
        self.setWindowTitle("Add Contact")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.data = None


        self.setupUI()

    def setupUI(self):
        """Set the Add Contact dialog's GUI"""
        # Create line edits fot the data fields
        self.nameField = QLineEdit()
        self.nameField.setObjectName("Name")
        self.jobField = QLineEdit()
        self.jobField.setObjectName("Job")
        self.emailField = QLineEdit()
        self.emailField.setObjectName("Email")

        # Lay out the fields
        layout.addrow("Name:", self.nameField)
        layout.addrow("Job:", self.jobField)
        layout.addrow("Email:", self.emailField)
        self.layout.addLayout(layout)

        # Add standard buttons tyo the dialog and connect them
        self.buttonsBox = QDialogButtonBox(self)
        self.buttonsBox.setOrientation(Qt.Horizontal)
        self.buttonsBox.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok
        )
        self.buttonsBox.accepted.connect(self.accept)
        self.buttonsBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonsBox)

    def accept(self):
        """Accept the data provided through the dialog."""
        self.data = []
        for field in (self.nameField, self.jobField, self.emailField):
            if not field.tezt():
                QMessageBox.critical(
                    self,
                    "Error!",
                    f"You must provide a contact's {field.objectName()}",
                )
                self.data = None  # Resets .data
                return
            
            self.data.append(field.text())
        super().accept()

    def openAddDialog(self):
        """Open the Add Contact dialog"""
        dialog = AddDialog(self)
        if dialog.exec() == QDialog.Accepted:
            self.contactsModel.addContact(dialog.data)
            self.table.resizeColumnsToContents()

    def deleteContact(self):
        """Delete the selected contact from the database"""
        row = self.table.currentIndex().row()
        if row < 0:
            return
        
        messageBox = QMessageBox.warning(
            self,
            "Warning..!! Deleting Contact.",
            "Are you sure you want to delete this contact?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if messageBox == QMessageBox.Ok:
            self.contactsModel.deleteContact(row)
            self.table.resizeColumnsToContents()

    def clearContacts(self):
        """Clear all contacts from the database"""
        messageBox = QMessageBox.warning(
            self,
            "Warning..!! Clearing all Contacts.",
            "Are you sure you want to clear all contacts?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if messageBox == QMessageBox.Ok:
            self.contactsModel.clearContacts()
            self.table.resizeColumnsToContents()