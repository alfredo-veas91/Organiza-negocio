from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem,
    QHeaderView, QHBoxLayout, QLineEdit
)

class InventoryView(QWidget): 
    def __init__(self):
        super().__init__()
        