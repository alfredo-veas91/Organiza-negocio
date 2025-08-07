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
        layout = QVBoxLayout()

        self.product_name_input = QLineEdit()
        self.product_name_input.setPlaceholderText("Nombre del Producto")
        layout.addWidget(self.product_name_input)

        self.product_price_input = QLineEdit()
        self.product_price_input.setPlaceholderText("Precio del Producto")
        self.product_price_input.setValidator(QDoubleValidator(0.99, 9999.99, 2))
        layout.addWidget(self.product_price_input)

        self.setLayout(layout)
