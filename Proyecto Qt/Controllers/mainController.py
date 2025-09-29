from PyQt6.QtWidgets import QDialog
from Controllers.cashController import CashController
from Models.cashModel import CashModel


class MainController:
    def __init__(self, main_window):
        self.main_window = main_window

        # Modelo de caja
        self.cash_model = CashModel()

        # Controlador de caja
        self.cash_controller = CashController(self.cash_model, self.main_window)

        # Conectar eventos de botones
        self._connect_events()

    def _connect_events(self):
        self.main_window.btn_cash.clicked.connect(self.open_cash_view)
        self.main_window.btn_sales.clicked.connect(self.open_sales_view)
        self.main_window.btn_inventory.clicked.connect(self.open_inventory_view)
        self.main_window.btn_suppliers.clicked.connect(self.open_suppliers_view)
        self.main_window.btn_exit.clicked.connect(self.main_window.close)

    # ---- Métodos para cada botón ----
    def open_cash_view(self):
        """Muestra la vista de Caja y abre el diálogo para ingresar/quitar dinero"""
        self.main_window.stack.setCurrentIndex(0)
        self.cash_controller.open_cash_window()  # el CashController maneja la lógica

    def open_sales_view(self):
        self.main_window.stack.setCurrentIndex(1)

    def open_inventory_view(self):
        print("Abrir ventana de inventario - Por implementar")

    def open_suppliers_view(self):
        print("Abrir ventana de proveedores - Por implementar")
