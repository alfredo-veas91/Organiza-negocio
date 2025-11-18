from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QFormLayout, QLineEdit,
    QPushButton, QMessageBox, QHBoxLayout, QComboBox
)
from PyQt6.QtCore import pyqtSignal


class SupplierEditWindow(QDialog):
    supplier_updated = pyqtSignal(dict)

    def __init__(self, supplier: dict | None = None):
        super().__init__()
        self.setWindowTitle("Editar Proveedor")
        self.supplier = supplier or {}
        self.setup_ui()
        if supplier:
            self.populate_fields(supplier)

    def setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(QLabel("Formulario para editar proveedor"))

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

    def populate_fields(self, supplier: dict):
        self.rut_edit.setText(str(supplier.get("rut", "")))
        self.name_edit.setText(str(supplier.get("name", "")))
        self.encargado_edit.setText(str(supplier.get("encargado", "")))
        self.email_edit.setText(str(supplier.get("email", "")))
        self.phone_edit.setText(str(supplier.get("phone", "")))
        self.category_edit.setText(str(supplier.get("category", "")))
        status = str(supplier.get("status", ""))
        idx = self.status_edit.findText(status)
        if idx >= 0:
            self.status_edit.setCurrentIndex(idx)

    def _on_save(self):
        rut = self.rut_edit.text().strip()
        if rut and (len(rut) != 10 or rut[8] != '-'):
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

        self.supplier_updated.emit(supplier_data)
        QMessageBox.information(self, "Proveedor", "Proveedor actualizado correctamente.")
        self.accept()
