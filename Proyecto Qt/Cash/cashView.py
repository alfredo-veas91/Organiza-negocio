from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

class CashView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Vista de Caja"))
        self.setLayout(layout)
