from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QDoubleValidator



class AddSaleWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Agregar Venta")
        self.setFixedSize(400, 300)
        self.create_form()
    def create_form(self):
        self.setFixedSize(300,200)
        self.setModal(True)

        layout = QVBoxLayout()

        title = QLabel("Ingrese producto para venta")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("""
                            font-size: 16px;
                            font-weight: bold;
                            color: #2c3e50;
                            margin: 10px;
                            """)
        layout.addWidget(title)

        self.productId = QLineEdit()
        self.productId.setPlaceholderText("ID del producto")
        validator = QDoubleValidator(0.0, 1000000.0, 2)
        validator.setNotation(QDoubleValidator.Notation.StandardNotation)
        self.productId.setValidator(validator)
        layout.addWidget(self.productId)
        self.setLayout(layout)



