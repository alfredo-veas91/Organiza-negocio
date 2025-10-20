from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel

class SupplierHistoryWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Historial de Compras del Proveedor")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Historial de compras (por implementar)"))
        self.setLayout(layout)
