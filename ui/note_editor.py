from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton

class NoteEditor(QDialog):
    def __init__(self, parent=None, existing_note=None):
        super().__init__(parent)
        self.setWindowTitle("New Note" if not existing_note else "Edit Note")
        self.resize(400, 400)

        self.existing_note = existing_note
        self.saved = False

        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Note Title")

        self.content_input = QTextEdit()
        self.content_input.setPlaceholderText("Write your note here...")

        if existing_note:
            self.title_input.setText(existing_note["title"])
            self.content_input.setPlainText(existing_note["content"])

        save_btn = QPushButton("Save")
        cancel_btn = QPushButton("Cancel")
        save_btn.clicked.connect(self.save_note)
        cancel_btn.clicked.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Title:"))
        layout.addWidget(self.title_input)
        layout.addWidget(QLabel("Content:"))
        layout.addWidget(self.content_input)

        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(cancel_btn)
        btn_layout.addWidget(save_btn)

        layout.addLayout(btn_layout)
        self.setLayout(layout)

    def save_note(self):
        self.saved = True
        self.title = self.title_input.text().strip()
        self.content = self.content_input.toPlainText().strip()
        self.accept()