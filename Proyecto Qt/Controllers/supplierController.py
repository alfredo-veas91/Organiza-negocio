from Models import supplierModel
from Views.supplierAddWindow import SupplierAddWindow
from Views.supplierEditWindow import SupplierEditWindow
from Views.supplierHistoryWindow import SupplierHistoryWindow
from PyQt6.QtWidgets import QDialog, QMessageBox

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
        self.view.delete_requested.connect(self.delete_supplier)

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
            # obtener id del proveedor desde la primera columna (suponiendo que está ahí)
            id_item = self.view.table.item(row, 0)
            if not id_item:
                return
            try:
                supplier_id = int(id_item.text())
            except ValueError:
                return
            self.delete_supplier(supplier_id)
        elif col == self.view.col_history:
            dialog = SupplierHistoryWindow()
            dialog.exec()

    def delete_supplier(self, supplier_id: int):
        resp = QMessageBox.question(
            self.view,
            "Confirmar eliminación",
            "¿Eliminar este proveedor?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if resp == QMessageBox.StandardButton.Yes:
            deleted = supplierModel.delete_supplier(supplier_id)
            if deleted:
                QMessageBox.information(self.view, "Eliminado", "Proveedor eliminado correctamente.")
                self.load_suppliers()
            else:
                QMessageBox.warning(self.view, "No encontrado", "No se encontró el proveedor para eliminar.")