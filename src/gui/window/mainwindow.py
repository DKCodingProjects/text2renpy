from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar
import os

class MainWindow(QMainWindow):
    def __init__(self, app, icon: QIcon, name: str):
        super().__init__()
        self.setWindowTitle(name+' - Main')
        self.setMinimumSize(QSize(680, 320))
        self.setWindowIcon(icon)
        self.app = app

        #Menubar and menus
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        new_menu = file_menu.addMenu('New...')
        new_menu.setToolTipsVisible(True)
        new_script = new_menu.addAction('Run')
        new_script.setToolTip('Start a new run of the Text2Ren\'Py program')
        new_project = new_menu.addAction('Project')
        new_project.setToolTip('Create a new Ren\'Py project to work in')
        edit_menu = file_menu.addMenu('Edit...')
        edit_menu.setToolTipsVisible(True)
        edit_project = edit_menu.addAction('Project')
        edit_project.setToolTip('Edit program variables for existing Ren\'Py projects')
        edit_settings = edit_menu.addAction('Settings')
        edit_settings.setToolTip('Edit Text2Ren\'Py program settings and default behaviors')

        help_menu = menu_bar.addMenu('Help')
        help_menu.setToolTipsVisible(True)
        gstarted_menu = help_menu.addAction('Getting Started')
        gstarted_menu.setToolTip('Learn the basics of Text2Ren\'Py to help you get started!')
        doc_menu = help_menu.addAction('Documentation')
        doc_menu.setToolTip('Look at the offical documentation for more information')
        contact_menu = help_menu.addAction('Contact')
        contact_menu.setToolTip('Contact infomation if you have any questions or experience bugs')
        
        settings_menu = menu_bar.addMenu('Settings')
        settings_menu.addAction('Defaults')

        quit_action = file_menu.addAction('Quit')
        quit_action.triggered.connect(self.quit_app)

        '''
        action2 = QAction('Some other action', self)
        action2.setToolTip('Status message for some other action')
        action2.triggered.connect(self.toolbar_button_click)
        #action2.setCheckable(True)
        menu_bar.addAction(action2)

        #Working with toolbars
        toolbar = QToolBar('My main toolbar')
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        #Add the quit action to the toolbar
        toolbar.addAction(quit_action)

        action1 = QAction('Some Action', self)
        action1.setToolTip('Status message for some action')
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)

        action2 = QAction(QIcon('start.png'), 'Some other action', self)
        action2.setToolTip('Status message for some other action')
        action2.triggered.connect(self.toolbar_button_click)
        #action2.setCheckable(True)
        toolbar.addAction(action2)

        toolbar.addSeparator()
        toolbar.addWidget(QPushButton('Click here'))


        # Working with status bars
        self.setStatusBar(QStatusBar(self))

        button1 = QPushButton('BUTTON1')
        button1.clicked.connect(self.button1_clicked)
        self.setCentralWidget(button1)
        '''


    def button1_clicked(self):
        print('Clicked on the button')
    def quit_app(self):
        self.app.quit()

    def toolbar_button_click(self):
        self.statusBar().showMessage('Message from my app',3000)