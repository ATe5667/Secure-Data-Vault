from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from functools import partial

class Sidebar(QWidget):
    def __init__(self, stack_widget):
        super().__init__()

        self.stack = stack_widget

        layout = QVBoxLayout()
        self.setFixedWidth(150)
        layout.setSpacing(10)
        layout.setContentsMargins(10, 10, 10, 10)

        pages = {"Home": 0, "Notes": 1, "Passwords": 2, "Settings": 3}

        for name, index in pages.items():
            button = QPushButton(name)
            button.clicked.connect(partial(self.stack.setCurrentIndex, index))
            layout.addWidget(button)

        self.setLayout(layout)