from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox, QSizePolicy
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QDoubleValidator

class CashWindow(QDialog):
    def __init__(self, current_cash, parent=None):
        super().__init__()
        self.current_cash = current_cash
        self.entered_amount = 0.0
        self.setWindowTitle("Caja")
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(300, 200)
        self.setModal(True)

        layout = QVBoxLayout()

        title = QLabel("Gestión de Caja")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("""
            font-size: 16px;
            font-weight: bold;
            color: #2c3e50;
            margin: 10px;
        """)

        self.cash_label = QLabel(f"Dinero en caja: ${self.current_cash:.2f}")
        self.cash_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cash_label.setStyleSheet("""
            font-size: 14px;
            color: #27ae60;
            font-weight: bold;
            padding: 5px;
            background-color: #ecf0f1;
            border-radius: 5px;
            margin: 5px;
        """)

        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Ingrese monto a agregar")

        validator = QDoubleValidator(0.0, 1000000.0, 2)
        validator.setNotation(QDoubleValidator.Notation.StandardNotation)
        self.amount_input.setValidator(validator)

        self.amount_input.setStyleSheet("""
            QLineEdit {
                font-size: 14px;
                color: #27ae60;
                font-weight: bold;
                padding: 5px;
                background-color: #ecf0f1;
                border-radius: 5px;
                margin: 5px;
            }
        """)

        self.buttons_layout = QHBoxLayout()

        self.btn_add = QPushButton("Agregar Dinero")
        self.btn_remove = QPushButton("Quitar Dinero")
        self.btn_exit = QPushButton("Salir")

        for btn in [self.btn_add, self.btn_remove, self.btn_exit]:
            btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #3498db;
                    color: white;
                    border: 2px solid #2980b9;
                    border-radius: 5px;
                    font-weight: bold;
                    padding: 10px;
                }
                QPushButton:hover { background-color: #2980b9; }
                QPushButton:pressed { background-color: #1f618d; }
            """)
            self.buttons_layout.addWidget(btn)

        layout.addWidget(title)
        layout.addWidget(self.cash_label)
        layout.addWidget(self.amount_input)
        layout.addLayout(self.buttons_layout)
        self.setLayout(layout)

        self.connect_events()

    def connect_events(self):
        self.btn_add.clicked.connect(self.add_money)
        self.btn_remove.clicked.connect(self.remove_money)
        self.btn_exit.clicked.connect(self.reject)
        self.amount_input.returnPressed.connect(self.add_money)

    def add_money(self):
        amount = self.get_amount()
        if amount is not None:
            self.entered_amount += amount
            QMessageBox.information(self, "Éxito", f"Se han agregado ${amount:.2f} a la caja.")
            self.accept()

    def remove_money(self):
        amount = self.get_amount()
        if amount is not None:
            if amount > self.current_cash:
                QMessageBox.warning(self, "Error", "No hay suficiente dinero en caja para quitar esa cantidad.")
            else:
                self.entered_amount -= amount
                QMessageBox.information(self, "Éxito", f"Se han quitado ${amount:.2f} de la caja.")
                self.accept()

    def get_amount(self):
        text = self.amount_input.text().strip()
        if not text:
            QMessageBox.warning(self, "Error", "Por favor, ingrese un monto válido.")
            self.amount_input.setFocus()
            return None
        try:
            amount = float(text)
            if amount <= 0:
                raise ValueError("El monto debe ser positivo.")
            return amount
        except ValueError as e:
            QMessageBox.warning(self, "Error", f"Entrada inválida: {e}. Por favor, ingrese un monto válido.")
            self.amount_input.setFocus()
            return None
