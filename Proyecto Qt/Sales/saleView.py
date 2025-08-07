from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout

from Sales.addSaleWindow import AddSaleWindow

class SaleView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Vista de Venta"))
        self.createButtons(layout)
        self.setLayout(layout)
        self.connect_sale_events()

    def createButtons(self, layout):
        buttons_layout = QVBoxLayout()

        # Crear los botones como atributos de la clase (self.btn_...)
        self.btn_addSale = QPushButton("Agregar Venta")
        self.btn_addSale.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px; font-size: 16px;")
        self.btn_dropSale = QPushButton("Eliminar Venta")
        self.btn_dropSale.setStyleSheet("background-color: #f44336; color: white; padding: 10px; font-size: 16px;")
        
        buttons = [self.btn_addSale, self.btn_dropSale]

        for btn in buttons:
            buttons_layout.addWidget(btn)

        layout.addLayout(buttons_layout)

    def connect_sale_events(self):
        self.btn_addSale.clicked.connect(self.open_add_sale)
        #self.btn_dropSale.clicked.connect(self.remove_sale)  # Descomenta cuando tengas el método remove_sale

    def open_add_sale(self):
        self.add_sale_window = AddSaleWindow()
        self.add_sale_window.exec()