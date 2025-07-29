from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit,
    QPushButton, QFileDialog, QListWidget, QListWidgetItem, QMenu, QMessageBox
)

import os
import subprocess

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

        self.attached_files = existing_note.get("files", []) if existing_note else []
        self.file_list = QListWidget()
        self.file_list.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.file_list.customContextMenuRequested.connect(self.show_file_context_menu)
        for f in self.attached_files:
            self.file_list.addItem(QListWidgetItem(f))

        self.attach_button = QPushButton("Attach File")
        self.attach_button.clicked.connect(self.attach_file)

        self.file_list.itemDoubleClicked.connect(self.open_file)

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

        layout.addWidget(QLabel("Attached Files:"))
        layout.addWidget(self.file_list)
        layout.addWidget(self.attach_button)

        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(cancel_btn)
        btn_layout.addWidget(save_btn)

        layout.addLayout(btn_layout)
        self.setLayout(layout)

    def save_note(self):
        self.title = self.title_input.text()
        self.content = self.content_input.toPlainText()
        self.saved = True
        self.note_data = {
            "title": self.title,
            "content": self.content,
            "files": self.attached_files.copy()
        }
        self.accept()

    def attach_file(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Select files to attach")
        for file in files:
            if file not in self.attached_files:
                self.attached_files.append(file)
                self.file_list.addItem(QListWidgetItem(file))

    def open_file(self, item):
        filepath = item.text()
        if os.path.exists(filepath):
            try:
                if os.name == 'nt':  # Windows
                    os.startfile(filepath)
                elif os.name == 'posix':  # Linux
                    subprocess.call(['xdg-open', filepath])
                else:  # macOS
                    subprocess.call(['open', filepath])
            except Exception as e:
                print(f"Could not open file: {e}")
        else:
            print("File not found.")

    def show_file_context_menu(self, position):
        item = self.file_list.itemAt(position)
        if not item:
            return

        menu = QMenu()
        remove_action = menu.addAction("Remove File")

        action = menu.exec(self.file_list.viewport().mapToGlobal(position))
        if action == remove_action:
            reply = QMessageBox.question(
                self,
                "Confirm Removal",
                f"Remove '{item.text()}' from this note?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            if reply == QMessageBox.StandardButton.Yes:
                filepath = item.text()
                self.attached_files.remove(filepath)
                self.file_list.takeItem(self.file_list.row(item))