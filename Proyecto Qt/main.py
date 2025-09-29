import sys
from PyQt6.QtWidgets import QApplication
from Views.mainwindow import MainWindow
from Controllers.mainController import MainController


def main():
    app = QApplication(sys.argv)

    main_window = MainWindow()
    controller = MainController(main_window)

    main_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
