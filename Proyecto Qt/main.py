import sys
from PyQt6.QtWidgets import QApplication
from Views.mainwindow import MainWindow
from Controllers.mainController import MainController
from Database.database import init_db

def main():
    app = QApplication(sys.argv)

    main_window = MainWindow()

    init_db()
    controller = MainController(main_window)

    main_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
