from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel

class SupplierEditWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editar Proveedor")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Formulario para editar proveedor (por implementar)"))
        self.setLayout(layout)
