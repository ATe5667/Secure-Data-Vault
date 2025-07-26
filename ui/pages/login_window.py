from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QHBoxLayout
import json
import hashlib
import os

class LoginWindow(QWidget):
    def __init__(self, switch_to_main_callback):
        super().__init__()
        self.switch_to_main = switch_to_main_callback
        self.setWindowTitle("Login - Secure Data Vault")
        self.setFixedSize(400, 200)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)

        self.signup_button = QPushButton("Sign Up")
        self.signup_button.clicked.connect(self.open_signup)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.login_button)
        button_layout.addWidget(self.signup_button)

        layout = QVBoxLayout()
        layout.addStretch(1)
        layout.addWidget(QLabel("Login"))
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addLayout(button_layout)
        layout.addStretch(1)

        self.setLayout(layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        users = load_users()

        if username in users and users[username] == hash_password(password):
            QMessageBox.information(self, "Login Successful", f"Welcome {username}!")
            self.switch_to_main()
            self.close()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid credentials.")

    def open_signup(self):
        self.signup_window = SignupWindow(switch_to_login_callback=self.show)
        self.signup_window.show()
        self.hide()

class SignupWindow(QWidget):
    def __init__(self, switch_to_login_callback):
        super().__init__()
        self.switch_to_login = switch_to_login_callback
        self.setWindowTitle("Sign Up - Secure Data Vault")
        self.setFixedSize(400, 200)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("New Username")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("New Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.signup_button = QPushButton("Sign Up")
        self.signup_button.clicked.connect(self.signup)

        layout = QVBoxLayout()
        layout.addStretch(1)
        layout.addWidget(QLabel("Create a new account"))
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.signup_button)
        layout.addStretch(1)

        self.setLayout(layout)

    def signup(self):
        username = self.username_input.text()
        password = self.password_input.text()

        users = load_users()

        if username in users:
            QMessageBox.warning(self, "Signup Failed", "Username already exists.")
        elif not username or not password:
            QMessageBox.warning(self, "Signup Failed", "Please enter both username and password.")
        else:
            users[username] = hash_password(password)
            save_users(users)
            QMessageBox.information(self, "Signup Successful", "Account created successfully!")
            self.switch_to_login()
            self.close()


USER_FILE = "users.json"

def load_users():
    if not os.path.exists(USER_FILE):
        return {}
    with open(USER_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()