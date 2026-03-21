"""A client program written to verify correctness of the activity 
classes.
"""

from contact_list.contact_list import ContactList
from PySide6.QtWidgets import QApplication
import sys

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

def main() -> None:
    """The main function of the program."""

    app = QApplication(sys.argv)
    window = ContactList()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
