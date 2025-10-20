import sqlite3
import os

DB_NAME = "data.db"
DB_PATH = os.path.join(os.path.dirname(__file__), DB_NAME)

def get_connection():
    """Crea y devuelve la conexión a la base de datos."""
    return sqlite3.connect(DB_PATH)

def init_db():
    """Crea las tablas si no existen."""
    conn = get_connection()
    cursor = conn.cursor()

    # Productos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            barcode TEXT UNIQUE,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
    """)

    # Proveedores
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS suppliers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rut TEXT,
            name TEXT NOT NULL,
            email TEXT,
            encargado TEXT,
            phone TEXT,
            category TEXT,
            status TEXT
        )
    """)

    conn.commit()
    conn.close()
