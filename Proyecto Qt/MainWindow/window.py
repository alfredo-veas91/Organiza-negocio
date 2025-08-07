from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
                             QLabel, QFormLayout, QSizePolicy, QDialog)
from PyQt6.QtCore import Qt

from Cash.cashWindow import CashWindow  # Renombrado
from Cash.cashView import CashView  # Renombrado

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.cash_total = 0.0
        self.setup_ui()
        self.connect_events()

    def setup_ui(self):
        self.setWindowTitle("Mi Aplicación Funcional")
        self.setGeometry(100, 100, 700, 500)

        main_layout = QVBoxLayout()
        self.setStyleSheet("background-color: #262626;")

        self.create_title(main_layout)
        self.create_main_buttons(main_layout)
        self.create_work_area(main_layout)
        self.create_bottom_bar(main_layout)

        self.setLayout(main_layout)

    def create_title(self, layout):
        self.title_label = QLabel("Mi Aplicación")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setStyleSheet("""
            font-size: 18px; 
            font-weight: bold; 
            padding: 10px;
            color: white;
        """)
        layout.addWidget(self.title_label)

    def create_main_buttons(self, layout):
        buttons_layout = QHBoxLayout()

        self.btn_cash = QPushButton("Caja")
        self.btn_sales = QPushButton("Venta")
        self.btn_inventory = QPushButton("Inventario")
        self.btn_suppliers = QPushButton("Proveedores")

        buttons = [self.btn_cash, self.btn_sales, self.btn_inventory, self.btn_suppliers]

        for btn in buttons:
            buttons_layout.addWidget(btn)

        self.configure_main_buttons(buttons)
        layout.addLayout(buttons_layout)

    def configure_main_buttons(self, buttons):
        for btn in buttons:
            btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #3498db;
                    color: white;
                    border: 4px solid #413e3e;
                    border-radius: 8px;
                    font-weight: bold;
                    font-size: 14px;
                    padding: 5px 15px;           
                    min-height: 30px;            
                    max-height: 80px;            
                }
                QPushButton:hover { background-color: #2980b9; }
                QPushButton:pressed { background-color: #1f618d; }
            """)

    def create_work_area(self, layout):
        self.center_layout = QFormLayout()
        layout.addLayout(self.center_layout)

    def create_bottom_bar(self, layout):
        bottom_layout = QHBoxLayout()

        self.status_label = QLabel(f"Dinero en caja: ${self.cash_total:.2f}")
        self.status_label.setStyleSheet("""
            color: #27ae60;
            font-size: 14px;
            font-weight: bold;
        """)

        self.btn_exit = QPushButton("Salir")
        self.btn_exit.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border: none;
                padding: 8px 15px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #c0392b; }
        """)

        bottom_layout.addWidget(self.status_label)
        bottom_layout.addStretch()
        bottom_layout.addWidget(self.btn_exit)

        layout.addLayout(bottom_layout)

    def connect_events(self):
        self.btn_cash.clicked.connect(self.open_cash_window)
        self.btn_sales.clicked.connect(self.open_sales_window)
        self.btn_inventory.clicked.connect(self.open_inventory_window)
        self.btn_suppliers.clicked.connect(self.open_suppliers_window)
        self.btn_exit.clicked.connect(self.close)

    def open_cash_window(self):
        dialog = CashWindow(self.cash_total, self)

        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.cash_total += dialog.entered_amount
            self.update_cash_display()

    def open_sales_window(self):
        print("Abrir ventana de ventas - Por implementar")

    def open_inventory_window(self):
        print("Abrir ventana de inventario - Por implementar")

    def open_suppliers_window(self):
        print("Abrir ventana de proveedores - Por implementar")

    def update_cash_display(self):
        self.status_label.setText(f"Dinero en caja: ${self.cash_total:.2f}")

        if self.cash_total < 0:
            color = "#e74c3c"
        elif self.cash_total == 0:
            color = "#f39c12"
        else:
            color = "#27ae60"

        self.status_label.setStyleSheet(f"""
            color: {color};
            font-size: 14px;
            font-weight: bold;
        """)
