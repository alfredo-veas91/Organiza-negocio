from Models import supplierModel
from Views.supplierAddWindow import SupplierAddWindow
from Views.supplierEditWindow import SupplierEditWindow
from Views.supplierHistoryWindow import SupplierHistoryWindow
from PyQt6.QtWidgets import QDialog

class SupplierController:
    def __init__(self, view):
        self.view = view
        supplierModel.create_table()
        supplierModel.seed_sample_data()
        self.load_suppliers()
        self.connect_signals()

    def connect_signals(self):
        self.view.btn_add_supplier.clicked.connect(self.add_supplier)
        self.view.btn_add_purchase.clicked.connect(self.add_purchase)
        self.view.table.cellClicked.connect(self.handle_table_click)

    def load_suppliers(self):
        suppliers = supplierModel.get_all_suppliers()
        self.view.load_table_data(suppliers)

    def add_supplier(self):
        dialog = SupplierAddWindow()
        dialog.exec()
        self.load_suppliers()

    def add_purchase(self):
        # Más adelante abrirá el módulo de compras
        print("Abrir ventana de agregar compra (por implementar)")

    def handle_table_click(self, row, col):
        if col == self.view.col_edit:
            dialog = SupplierEditWindow()
            dialog.exec()
        elif col == self.view.col_delete:
            print("Eliminar proveedor (por implementar)")
        elif col == self.view.col_history:
            dialog = SupplierHistoryWindow()
            dialog.exec()
