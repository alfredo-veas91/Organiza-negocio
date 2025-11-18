from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QTableWidget, 
    QTableWidgetItem, QSizePolicy, QHeaderView, QWidgetItem, QFrame
)
from PyQt6.QtCore import Qt, pyqtSignal

from Views.supplierEditWindow import SupplierEditWindow


class SupplierView(QWidget):
    delete_requested = pyqtSignal(int)  # Señal para solicitar eliminación de proveedor por ID
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        title = QLabel("Gestión de Proveedores")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("""
            font-size: 18px;
            font-weight: bold;
            color: white;
            margin: 10px;
        """)
        layout.addWidget(title)

        # Botones principales
        button_layout = QHBoxLayout()
        self.btn_add_supplier = QPushButton("Agregar proveedor")  # 🔸 Aquí va icono
        self.btn_add_purchase = QPushButton("Agregar compra")     # 🔸 Aquí va icono

        for btn in [self.btn_add_supplier, self.btn_add_purchase]:
            btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #3498db;
                    color: white;
                    border-radius: 8px;
                    padding: 10px;
                    font-weight: bold;
                }
                QPushButton:hover { background-color: #2980b9; }
            """)
            button_layout.addWidget(btn)

        layout.addLayout(button_layout)

        # Tabla
        self.table = QTableWidget()
        self.table.setColumnCount(9)
        self.table.setHorizontalHeaderLabels([
            "ID", "RUT", "Nombre", "Email", "Encargado", "Teléfono", 
            "Categoría", "Estado", "Acciones"
        ])
        self.table.setColumnHidden(0, True)  # Ocultar ID
        layout.addWidget(self.table)

        self.setLayout(layout)

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)


    def load_table_data(self, suppliers):
        self.table.setRowCount(len(suppliers))
        for row, supplier in enumerate(suppliers):
            for col, value in enumerate(supplier):
                item = QTableWidgetItem(str(value))
                item.setFlags(Qt.ItemFlag.ItemIsEnabled)
                self.table.setItem(row, col, item)

            actions_widget = QWidget()
            actions_layout = QHBoxLayout()
            actions_layout.setContentsMargins(0, 0, 0, 0)
            actions_layout.setSpacing(5)

            btn_edit = QPushButton("✏️")
            btn_delete = QPushButton("🗑️")
            btn_history = QPushButton("📜")

            for btn in [btn_edit, btn_delete, btn_history]:
                btn.setFixedSize(30, 30)
                actions_layout.addWidget(btn)

             # conectar botón editar para abrir ventana de edición y rellenar campos
            def _make_edit(row_index):
                def _on_edit():
                    # construir dict del proveedor desde la fila (columnas: id, rut, name, email, encargado, phone, category, status)
                    cols = ["id", "rut", "name", "email", "encargado", "phone", "category", "status"]
                    supplier = {}
                    for i, key in enumerate(cols):
                        item = self.table.item(row_index, i)
                        supplier[key] = item.text() if item else ""
                    dialog = SupplierEditWindow(supplier)
                    # actualizar la fila en la tabla si se emite supplier_updated
                    def _on_updated(updated):
                        mapping = {"rut":1, "name":2, "email":3, "encargado":4, "phone":5, "category":6, "status":7}
                        for key, col_idx in mapping.items():
                            val = updated.get(key, "")
                            itm = QTableWidgetItem(str(val))
                            itm.setFlags(Qt.ItemFlag.ItemIsEnabled)
                            self.table.setItem(row_index, col_idx, itm)
                    dialog.supplier_updated.connect(_on_updated)
                    dialog.exec()
                return _on_edit

            btn_edit.clicked.connect(_make_edit(row))

            # conectar botón eliminar para emitir el id del proveedor (col 0)
            def _make_delete(row_index):
                def _on_delete():
                    id_item = self.table.item(row_index, 0)
                    if not id_item:
                        return
                    try:
                        supplier_id = int(id_item.text())
                    except ValueError:
                        return
                    self.delete_requested.emit(supplier_id)
                return _on_delete

            btn_delete.clicked.connect(_make_delete(row))

            actions_widget.setLayout(actions_layout)
            self.table.setCellWidget(row, 8, actions_widget)
