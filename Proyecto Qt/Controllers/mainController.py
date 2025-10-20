from Controllers.cashController import CashController
from Controllers.supplierController import SupplierController
from Models.cashModel import CashModel


class MainController:
    def __init__(self, main_window):
        self.main_window = main_window

        # Modelos
        self.cash_model = CashModel()

        # Controladores
        self.cash_controller = CashController(self.cash_model, self.main_window)
        self.supplier_controller = SupplierController(self.main_window.supplierView)

        # Conectar eventos de los botones principales
        self._connect_events()

    def _connect_events(self):
        self.main_window.btn_cash.clicked.connect(self.open_cash_view)
        self.main_window.btn_sales.clicked.connect(self.open_sales_view)
        self.main_window.btn_inventory.clicked.connect(self.open_inventory_view)
        self.main_window.btn_suppliers.clicked.connect(self.open_suppliers_window)
        self.main_window.btn_exit.clicked.connect(self.main_window.close)

    # ---- Métodos para cada botón ----
    def open_cash_view(self):
        """Muestra la vista de Caja y abre el diálogo para ingresar/quitar dinero"""
        self.main_window.stack.setCurrentWidget(self.main_window.cashView)
        self.cash_controller.open_cash_window()

    def open_sales_view(self):
        self.main_window.stack.setCurrentWidget(self.main_window.saleView)

    def open_inventory_view(self):
        print("Abrir vista de inventario - (Por implementar)")

    def open_suppliers_window(self):
        """Abre la vista de proveedores"""
        self.main_window.stack.setCurrentWidget(self.main_window.supplierView)
        # Puedes actualizar datos si fuera necesario:
        self.supplier_controller.load_suppliers()
