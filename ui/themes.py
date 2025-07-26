from PyQt6.QtWidgets import QApplication

def apply_theme(theme_name):
    try:
        with open(f"resources/styles/{theme_name}.qss", "r") as file:
            style = file.read()
            QApplication.instance().setStyleSheet(style)
    except FileNotFoundError:
        print(f"Theme '{theme_name}' not found.")