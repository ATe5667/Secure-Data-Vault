from PyQt6.QtWidgets import QMainWindow, QStackedWidget, QWidget, QHBoxLayout, QMessageBox
from PyQt6.QtCore import QTimer, QEvent
from ui.sidebar import Sidebar
from ui.pages.notes_page import NotesPage
from ui.pages.passwords_page import PasswordsPage
from ui.pages.settings_page import SettingsPage
from ui.pages.home_page import HomePage
from ui.themes import apply_theme

class InactivityTimer:
    def __init__(self, timeout_ms, timeout_callback):
        self.timer = QTimer()
        self.timer.setInterval(timeout_ms)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(timeout_callback)

    def reset(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()

class MainWindow(QMainWindow):
    def __init__(self, logout_callback):
        super().__init__()
        self.logout_callback = logout_callback
        self.setWindowTitle("Secure Data Vault")
        self.resize(1000, 600)

        self.inactivity = InactivityTimer(int(0.5 * 60 * 1000), self.auto_logout)

        central_widget = QWidget()
        layout = QHBoxLayout()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.stack = QStackedWidget()
        self.stack.addWidget(HomePage())
        self.stack.addWidget(NotesPage())
        self.stack.addWidget(PasswordsPage())

        self.settings_page = SettingsPage()
        self.settings_page.timeout_changed.connect(self.update_timeout)
        self.stack.addWidget(self.settings_page)

        self.sidebar = Sidebar(self.stack)
        self.sidebar.setFixedWidth(150)

        layout.addWidget(self.sidebar)
        layout.addWidget(self.stack, 1)

        apply_theme("dark")

        self.installEventFilter(self)
        self.inactivity.reset()

    def auto_logout(self):
        QMessageBox.information(self, "Auto-Lock", "You were inactive. Please log in again.")
        self.close()
        self.logout_callback()

        print("Auto-logout triggered")

    def eventFilter(self, obj, event):
        if event.type() in (QEvent.Type.MouseMove, QEvent.Type.KeyPress):
            self.inactivity.reset()
        return super().eventFilter(obj, event)

    def update_timeout(self, new_timeout_ms):
        self.inactivity.timer.setInterval(new_timeout_ms)
        self.inactivity.reset()