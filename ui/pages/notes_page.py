from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QScrollArea, QFrame, QHBoxLayout, QTextEdit, QMessageBox
from ui.note_editor import NoteEditor
from ui.notes_manager import save_notes, load_notes

class NotesPage(QWidget):
    def __init__(self):
        super().__init__()

        self.notes = load_notes()

        header = QHBoxLayout()
        label = QLabel("Secure Data Vault - Notes")
        label.setStyleSheet("font-size: 24px; font-weight: bold;")
        new_note_btn = QPushButton("New Note")
        new_note_btn.clicked.connect(self.create_note)

        header.addWidget(label)
        header.addStretch()
        header.addWidget(new_note_btn)

        self.note_container = QVBoxLayout()
        self.note_container.setSpacing(10)

        scroll_content = QWidget()
        scroll_content.setLayout(self.note_container)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(scroll_content)

        layout = QVBoxLayout()
        layout.addLayout(header)
        layout.addWidget(scroll_area)

        self.setLayout(layout)

        self.refresh_notes()

    def add_note(self, title, content):
        note = {"title": title, "content": content}
        self.notes.append(note)
        save_notes(self.notes)

        card = QFrame()
        card.setFrameShape(QFrame.Shape.StyledPanel)
        card.setStyleSheet("background-color: #f0f0f0; padding: 10px; border-radius: 8px;")
        card_layout = QVBoxLayout()

        title_label = QLabel(title)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        title_label.mousePressEvent = lambda e, n=note: self.view_note(n)

        card_layout.addWidget(title_label)
        card.setLayout(card_layout)
        self.note_container.addWidget(card)

    def create_note(self):
        dialog = NoteEditor(self)
        if dialog.exec() and dialog.saved:
            self.add_note(dialog.title, dialog.content)

    def view_note(self, note):
        dialog = NoteEditor(self, existing_note=note)
        if dialog.exec() and dialog.saved:
            note["title"] = dialog.title
            note["content"] = dialog.content
            self.refresh_notes()

    def refresh_notes(self):
        # Clear layout
        while self.note_container.count():
            child = self.note_container.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        # Redraw all notes without modifying self.notes
        for note in self.notes:
            card = QFrame()
            card.setFrameShape(QFrame.Shape.StyledPanel)
            card.setStyleSheet("background-color: #f0f0f0; padding: 10px; border-radius: 8px;")
            card_layout = QVBoxLayout()

            title_label = QLabel(note["title"])
            title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
            title_label.mousePressEvent = lambda e, n=note: self.view_note(n)

            card_layout.addWidget(title_label)
            card.setLayout(card_layout)
            self.note_container.addWidget(card)