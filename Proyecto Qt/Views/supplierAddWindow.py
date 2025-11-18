from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QFormLayout, QLineEdit,
    QPushButton, QMessageBox, QHBoxLayout, QComboBox
)
from Models import supplierModel
from PyQt6.QtCore import pyqtSignal


class SupplierAddWindow(QDialog):
    supplier_saved = pyqtSignal(dict)
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Agregar Proveedor")
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout(self)

        main_layout.addWidget(QLabel("Formulario para agregar proveedor"))

        form = QFormLayout()
        self.rut_edit = QLineEdit()
        self.name_edit = QLineEdit()
        self.encargado_edit = QLineEdit()
        self.email_edit = QLineEdit()
        self.phone_edit = QLineEdit()
        self.category_edit = QLineEdit()
        self.status_edit = QComboBox()
        self.status_edit.addItems(["Activo", "Proximamente activo"])

        form.addRow("RUT:", self.rut_edit)
        form.addRow("Nombre *:", self.name_edit)
        form.addRow("Encargado:", self.encargado_edit)
        form.addRow("Email:", self.email_edit)
        form.addRow("Teléfono:", self.phone_edit)
        form.addRow("Categoría:", self.category_edit)
        form.addRow("Estado:", self.status_edit)
        main_layout.addLayout(form)

        btn_layout = QHBoxLayout()
        save_btn = QPushButton("Guardar")
        cancel_btn = QPushButton("Cancelar")
        btn_layout.addWidget(save_btn)
        btn_layout.addWidget(cancel_btn)
        main_layout.addLayout(btn_layout)

        save_btn.clicked.connect(self._on_save)
        cancel_btn.clicked.connect(self.reject)

    def _on_save(self):
        rut = self.rut_edit.text().strip()
        if len(rut) != 10 or rut[8] != '-':
            QMessageBox.warning(self, "Validación", "El RUT debe incluir guion.")
            return

        name = self.name_edit.text().strip()
        if not name:
            QMessageBox.warning(self, "Validación", "El nombre del proveedor es obligatorio.")
            return

        supplier_data = {
            "rut": rut,
            "name": name,
            "email": self.email_edit.text().strip(),
            "encargado": self.encargado_edit.text().strip(),            
            "phone": self.phone_edit.text().strip(),
            "category": self.category_edit.text().strip(),
            "status": self.status_edit.currentText().strip(),
        }

        print(supplier_data)

        # Try to persist using common method names if available; otherwise just emit the data
        try:
            if hasattr(supplierModel, "add_supplier"):
                supplierModel.add_supplier(
                    supplier_data["rut"],
                    supplier_data["name"],
                    supplier_data["email"],
                    supplier_data["encargado"],
                    supplier_data["phone"],
                    supplier_data["category"],
                    supplier_data["status"],
                )
            # emit signal so callers can react regardless of model implementation
            self.supplier_saved.emit(supplier_data)
            QMessageBox.information(self, "Proveedor", "Proveedor guardado correctamente.")
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo guardar el proveedor:\n{e}")
# ...existing code...   
        
