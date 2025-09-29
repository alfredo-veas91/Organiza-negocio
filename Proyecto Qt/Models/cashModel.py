class CashModel:
    def __init__(self):
        self.total = 0.0

    def get_total(self) -> float:
        return self.total

    def add_money(self, amount: float):
        if amount <= 0:
            raise ValueError("El monto debe ser positivo.")
        self.total += amount

    def remove_money(self, amount: float):
        if amount <= 0:
            raise ValueError("El monto debe ser positivo.")
        if amount > self.total:
            raise ValueError("No hay suficiente dinero en caja.")
        self.total -= amount
