from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt

class PasswordsPage(QWidget):
    def __init__(self):
        super().__init__()

        label = QLabel("Secure Data Vault - Passwords")
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter)  # Center horizontally only
        label.setStyleSheet("font-size: 24px;")

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addStretch(1)  # Push everything else down

        self.setLayout(layout)