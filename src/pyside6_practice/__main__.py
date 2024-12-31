import os
import sys
import signal

from PySide6 import QtGui, QtWidgets, QtCore
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtQml import QQmlApplicationEngine

from ui.ui_main import Ui_Wizard


class MainWizard(QWizard):

    def __init__(self, parent=None, flags=...):
        super().__init__(parent)

        self.ui: Ui_Wizard = Ui_Wizard()

        self.setup_ui()

    def setup_ui(self):
        self.ui.setupUi(self)


def main(debug=False):
    app = QApplication()
    app.setStyle('fusion')

    wizard = MainWizard()

    wizard.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main(debug=True)
