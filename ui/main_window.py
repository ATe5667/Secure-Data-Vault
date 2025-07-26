from PyQt6.QtWidgets import QMainWindow, QStackedWidget, QVBoxLayout, QWidget, QHBoxLayout
from ui.sidebar import Sidebar
from ui.pages.notes_page import NotesPage
from ui.pages.passwords_page import PasswordsPage
from ui.pages.settings_page import SettingsPage
from ui.pages.home_page import HomePage
from ui.themes import apply_theme

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Secure Data Vault")
        self.resize(1000, 600)

        central_widget = QWidget()
        layout = QHBoxLayout()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.stack = QStackedWidget()
        self.stack.addWidget(HomePage())
        self.stack.addWidget(NotesPage())
        self.stack.addWidget(PasswordsPage())
        self.stack.addWidget(SettingsPage())

        self.sidebar = Sidebar(self.stack)
        self.sidebar.setFixedWidth(150)

        layout.addWidget(self.sidebar)
        layout.addWidget(self.stack, 1)

        apply_theme("dark")