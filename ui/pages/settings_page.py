from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox
from PyQt6.QtCore import Qt, pyqtSignal
from ui.themes import apply_theme

class SettingsPage(QWidget):
    timeout_changed = pyqtSignal(int)

    def __init__(self):
        super().__init__()

        self.current_theme = "dark"  # Track current theme

        label = QLabel("Secure Data Vault - Settings")
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        label.setStyleSheet("font-size: 24px;")

        self.theme_button = QPushButton("Switch to Light Theme")
        self.theme_button.clicked.connect(self.toggle_theme)

        self.timeout_box = QComboBox()
        self.timeout_box.addItems(["30 seconds", "1 minute", "2 minutes", "5 minutes"])

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(QLabel("Auto-lock timeout:"))
        layout.addWidget(self.timeout_box)
        layout.addWidget(self.theme_button)
        layout.addStretch(1)

        self.timeout_box.currentIndexChanged.connect(self._on_timeout_changed)

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

    def _on_timeout_changed(self, index):
        values = [30_000, 60_000, 120_000, 300_000]  # in milliseconds
        self.timeout_changed.emit(values[index])