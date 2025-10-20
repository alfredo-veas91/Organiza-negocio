from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QTableWidget, 
    QTableWidgetItem, QSizePolicy, QHeaderView, QWidgetItem, QFrame
)
from PyQt6.QtCore import Qt

class SupplierView(QWidget):
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


            # 🔹 Botones de acción (aquí van los iconos después)
            btn_edit = QPushButton("✏️")     # → Icono de editar
            btn_delete = QPushButton("🗑️")   # → Icono de eliminar
            btn_history = QPushButton("📜")  # → Icono de historial

            for btn in [btn_edit, btn_delete, btn_history]:
                btn.setFixedSize(30, 30)
                actions_layout.addWidget(btn)
            
            actions_widget.setLayout(actions_layout)

            self.table.setCellWidget(row, 8, actions_widget)
