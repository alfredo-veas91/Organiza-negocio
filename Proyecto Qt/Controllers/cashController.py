from PyQt6.QtWidgets import QMessageBox
from Views.cashWindow import CashWindow


class CashController:
    def __init__(self, model, main_window):
        self.model = model
        self.main_window = main_window

    def open_cash_window(self):
        dialog = CashWindow(self.model.get_total(), self.main_window)

        # Conectar señales
        dialog.btn_add.clicked.connect(lambda: self._handle_add(dialog))
        dialog.btn_remove.clicked.connect(lambda: self._handle_remove(dialog))
        dialog.btn_exit.clicked.connect(dialog.reject)
        dialog.amount_input.returnPressed.connect(lambda: self._handle_add(dialog))

        dialog.exec()

    def _handle_add(self, dialog: CashWindow):
        amount = self._get_amount(dialog)
        if amount is None:
            return
        try:
            self.model.add_money(amount)
            QMessageBox.information(dialog, "Éxito", f"Se han agregado ${amount:.2f} a la caja.")
            self._update_view(dialog)
            dialog.accept()
        except ValueError as e:
            QMessageBox.warning(dialog, "Error", str(e))

    def _handle_remove(self, dialog: CashWindow):
        amount = self._get_amount(dialog)
        if amount is None:
            return
        try:
            self.model.remove_money(amount)
            QMessageBox.information(dialog, "Éxito", f"Se han quitado ${amount:.2f} de la caja.")
            self._update_view(dialog)
            dialog.accept()
        except ValueError as e:
            QMessageBox.warning(dialog, "Error", str(e))

    def _get_amount(self, dialog: CashWindow):
        text = dialog.amount_input.text().strip()
        if not text:
            QMessageBox.warning(dialog, "Error", "Por favor, ingrese un monto válido.")
            dialog.amount_input.setFocus()
            return None
        try:
            return float(text)
        except ValueError:
            QMessageBox.warning(dialog, "Error", "Entrada inválida. Por favor, ingrese un número.")
            dialog.amount_input.setFocus()
            return None

    def _update_view(self, dialog: CashWindow):
        """Actualiza tanto la ventana de caja como la vista principal"""
        dialog.cash_label.setText(f"Dinero en caja: ${self.model.get_total():.2f}")
        self.main_window.update_cash_display(self.model.get_total())
