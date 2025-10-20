from Database.database import get_connection

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
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


def add_supplier(rut, name, email, encargado, phone, category, status):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO suppliers (rut, name, email, encargado, phone, category, status)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (rut, name, email, encargado, phone, category, status))
    conn.commit()
    conn.close()


def get_all_suppliers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, rut, name, email, encargado, phone, category, status
        FROM suppliers
    """)
    data = cursor.fetchall()
    conn.close()
    return data


def seed_sample_data():
    """Agrega un proveedor de prueba si la tabla está vacía."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM suppliers")
    count = cursor.fetchone()[0]
    if count == 0:
        add_supplier(
            rut="76.543.210-9",
            name="Distribuidora San Pedro",
            email="contacto@sanpedro.cl",
            encargado="María López",
            phone="+56 9 8765 4321",
            category="Alimentos",
            status="Activo"
        )
    conn.close()
