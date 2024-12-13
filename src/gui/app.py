from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from src.gui.window.mainwindow import MainWindow
import sys
import os

class App():
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.name = 'Text2Ren\'Py'
        self.icon = QIcon(os.path.join('src', 'gui', 'assets', 'logo.png'))
        # other code here
        mainwin = MainWindow(self.app, self.icon, self.name)
        
        mainwin.show()

        self.app.exec()