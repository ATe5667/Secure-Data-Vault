import sys
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow
from ui.pages.login_window import LoginWindow

def main():
    app = QApplication(sys.argv)

    # Keep references in outer scope
    windows = {}

    def show_main():
        windows["main"] = MainWindow()  # Or just MainWindow() if you don’t use username
        windows["main"].show()
        windows["login"].close()  # Close login window after success

    windows["login"] = LoginWindow(switch_to_main_callback=show_main)
    windows["login"].show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()