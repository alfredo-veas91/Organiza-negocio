from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QLabel, QSizePolicy, QStackedLayout
)
from PyQt6.QtCore import Qt

from Views.cashView import CashView
from Views.saleView import SaleView

from Views.supplierView import SupplierView
from Controllers.supplierController import SupplierController


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Organiza negocio")
        self.setGeometry(100, 100, 700, 500)

        main_layout = QVBoxLayout()
        self.setStyleSheet("background-color: #262626;")

        self.create_title(main_layout)
        self.create_main_buttons(main_layout)
        self.create_work_area(main_layout)
        self.create_bottom_bar(main_layout)

        self.setLayout(main_layout)

    def create_title(self, layout):
        self.title_label = QLabel("Organiza negocio")
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
        self.stack = QStackedLayout()

        self.cashView = CashView()
        self.saleView = SaleView()
        self.supplierView = SupplierView()
        
        self.stack.addWidget(self.cashView)  # 0
        self.stack.addWidget(self.saleView)  # 1
        self.stack.addWidget(self.supplierView)  # 2


        from PyQt6.QtWidgets import QWidget
        container = QWidget()
        container.setLayout(self.stack)
        layout.addWidget(container)

    def create_bottom_bar(self, layout):
        bottom_layout = QHBoxLayout()

        self.status_label = QLabel("Dinero en caja: $0.00")
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

    # 🔹 Método público para que CashController actualice la vista
    def update_cash_display(self, new_total: float):
        self.status_label.setText(f"Dinero en caja: ${new_total:.2f}")

        if new_total < 0:
            color = "#e74c3c"
        elif new_total == 0:
            color = "#f39c12"
        else:
            color = "#27ae60"

        self.status_label.setStyleSheet(f"""
            color: {color};
            font-size: 14px;
            font-weight: bold;
        """)
