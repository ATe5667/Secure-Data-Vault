from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt

class HomePage(QWidget):
    def __init__(self):
        super().__init__()

        label = QLabel("Welcome to Secure Data Vault")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 24px;")  # Optional styling

        layout = QVBoxLayout()
        layout.addStretch(1)
        layout.addWidget(label)
        layout.addStretch(1)

        self.setLayout(layout)