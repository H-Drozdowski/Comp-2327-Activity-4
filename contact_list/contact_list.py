"""The module defines the ContactList class."""

from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QLineEdit
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QTableWidget
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtCore import Slot

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

class ContactList(QMainWindow):
    """Represents a window that provides the UI to manage contacts."""

    def __init__(self):
        """Initializes a new instance of the ContactList class."""

        super().__init__()
        self.__initialize_widgets()     
        self.add_button.clicked.connect(self.__on_add_contact) 

    def __initialize_widgets(self):
        """Initializes the widgets on this Window.
        
        DO NOT EDIT.
        """
        
        self.setWindowTitle("Contact List")

        self.contact_name_input = QLineEdit(self)
        self.contact_name_input.setPlaceholderText("Contact Name")

        self.phone_input = QLineEdit(self)
        self.phone_input.setPlaceholderText("Phone Number")

        self.add_button = QPushButton("Add Contact", self)
        self.remove_button = QPushButton("Remove Contact", self)
        
        self.contact_table = QTableWidget(self)
        self.contact_table.setColumnCount(2)
        self.contact_table.setHorizontalHeaderLabels(["Name", "Phone"])

        self.status_label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(self.contact_name_input)
        layout.addWidget(self.phone_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.remove_button)
        layout.addWidget(self.contact_table)
        layout.addWidget(self.status_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    @Slot()
    def __on_add_contact(self) -> None:
        """Validates and adds a contact to the contact list if the 
        contact is valid. Connected to the click event of a QPushButton.
        """

        name_text = self.contact_name_input.text()
        phone_number = self.phone_input.text()

        if name_text.strip() != "" and phone_number.strip() != "":
            num_of_rows = self.contact_table.rowCount()
            self.contact_table.insertRow(num_of_rows)

            name_item = QTableWidgetItem(name_text)
            phone_number_item = QTableWidgetItem(phone_number)

            self.contact_table.setItem(num_of_rows, 0, name_item)
            self.contact_table.setItem(num_of_rows, 1, phone_number_item)