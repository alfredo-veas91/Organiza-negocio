from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel

class SupplierAddWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Agregar Proveedor")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Formulario para agregar proveedor (por implementar)"))
        self.setLayout(layout)
