from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt
from ui.themes import apply_theme

class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()

        self.current_theme = "dark"  # Track current theme

        label = QLabel("Secure Data Vault - Settings")
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        label.setStyleSheet("font-size: 24px;")

        self.theme_button = QPushButton("Switch to Light Theme")
        self.theme_button.clicked.connect(self.toggle_theme)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.theme_button)
        layout.addStretch(1)

        self.setLayout(layout)

    def toggle_theme(self):
        if self.current_theme == "dark":
            apply_theme("light")
            self.current_theme = "light"
            self.theme_button.setText("Switch to Dark Theme")
        else:
            apply_theme("dark")
            self.current_theme = "dark"
            self.theme_button.setText("Switch to Light Theme")
