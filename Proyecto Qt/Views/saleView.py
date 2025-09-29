from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem,
    QHeaderView, QHBoxLayout, QLineEdit
)
from Views.addSaleWindow import AddSaleWindow

class SaleView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        # Crear tabla de ventas
        self.table_sales = QTableWidget()
        self.table_sales.setColumnCount(4)
        self.table_sales.setHorizontalHeaderLabels(["Código", "Producto", "Cantidad", "Precio"])
        self.table_sales.setRowCount(0)  # Sin filas por ahora
        self.table_sales.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        

        layout.addWidget(self.table_sales)  # Agregar tabla
        self.createButtons(layout)          # Botones
        self.createProductCodeInput(layout) # Campo de entrada
        self.setLayout(layout)
        self.connect_sale_events()

    def createButtons(self, layout):
        buttons_layout = QHBoxLayout()  # Cambiado a horizontal

        self.btn_addSale = QPushButton("Cobrar Venta")
        self.btn_addSale.setStyleSheet(
            "background-color: #4CAF50; color: white; padding: 10px; font-size: 16px;"
        )
        self.btn_dropSale = QPushButton("Eliminar Venta")
        self.btn_dropSale.setStyleSheet(
            "background-color: #f44336; color: white; padding: 10px; font-size: 16px;"
        )

        buttons_layout.addWidget(self.btn_addSale)
        buttons_layout.addWidget(self.btn_dropSale)

        layout.addLayout(buttons_layout)

    def createProductCodeInput(self, layout):
        self.input_productCode = QLineEdit()
        self.input_productCode.setPlaceholderText("Ingrese código de producto")
        self.input_productCode.setStyleSheet("padding: 8px; font-size: 14px;")
        layout.addWidget(self.input_productCode)

    def connect_sale_events(self):
        self.btn_addSale.clicked.connect(self.open_add_sale)
        # self.btn_dropSale.clicked.connect(self.remove_sale)  # Cuando lo implementes

    def open_add_sale(self):
        self.add_sale_window = AddSaleWindow()
        self.add_sale_window.exec()
