import sys
from PyQt6.QtWidgets import QApplication
from MainWindow.window import MainWindow  # Renombrado

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
