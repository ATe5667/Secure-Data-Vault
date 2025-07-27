import sys
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow
from ui.pages.login_window import LoginWindow

def main():
    app = QApplication(sys.argv)

    # Keep references in outer scope
    windows = {}

    def show_login():
        windows["login"] = LoginWindow(switch_to_main_callback=show_main)
        windows["login"].show()

    def show_main():
        windows["main"] = MainWindow(logout_callback=show_login)
        windows["main"].show()
        windows["login"].close()

    show_login()  # Start with login
    sys.exit(app.exec())

if __name__ == '__main__':
    main()