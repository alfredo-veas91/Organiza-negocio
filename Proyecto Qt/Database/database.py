import sqlite3

DB_NAME = "data.db"

def get_connection():
    """Crea y devuelve la conexión a la base de datos."""
    return sqlite3.connect(DB_NAME)

def init_db():
    """Crea las tablas si no existen."""
    conn = get_connection()
    cursor = conn.cursor()

    # Crear tabla de productos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            barcode TEXT UNIQUE,                -- Puede ser NULL, pero si existe debe ser único
            name TEXT NOT NULL,                 -- Nombre del producto
            quantity INTEGER NOT NULL,          -- Stock
            price REAL NOT NULL                 -- Precio unitario
        )
    """)

    conn.commit()
    conn.close()


# --- Funciones CRUD básicas ---

def add_product(barcode, name, quantity, price):
    """Agrega un producto a la base de datos."""
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO products (barcode, name, quantity, price) VALUES (?, ?, ?, ?)",
            (barcode, name, quantity, price)
        )
        conn.commit()
    except sqlite3.IntegrityError as e:
        print(f"Error al agregar producto: {e}")
    finally:
        conn.close()

def get_all_products():
    """Devuelve todos los productos en una lista de tuplas."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, barcode, name, quantity, price FROM products")
    products = cursor.fetchall()
    conn.close()
    return products

def get_product_by_barcode(barcode):
    """Busca un producto por código de barras."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, barcode, name, quantity, price FROM products WHERE barcode = ?", (barcode,))
    product = cursor.fetchone()
    conn.close()
    return product

def get_product_by_name(name):
    """Busca un producto por nombre."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE LOWER(name) LIKE LOWER(?)", (f"{name}%",))
    product = cursor.fetchall()
    conn.close()
    return product

def delete_product_by_id(product_id):
    """Elimina un producto usando su ID interno."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    conn.close()

def delete_all_products():
    """Elimina todos los productos de la base de datos."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products")
    conn.commit()
    conn.close()

def update_product(product_id, name=None, quantity=None, price=None, barcode=None):
    """Actualiza los datos de un producto según el ID."""
    conn = get_connection()
    cursor = conn.cursor()

    fields = []
    values = []

    if name is not None:
        fields.append("name = ?")
        values.append(name)
    if quantity is not None:
        fields.append("quantity = ?")
        values.append(quantity)
    if price is not None:
        fields.append("price = ?")
        values.append(price)
    if barcode is not None:
        fields.append("barcode = ?")
        values.append(barcode)

    values.append(product_id)

    sql = f"UPDATE products SET {', '.join(fields)} WHERE id = ?"
    cursor.execute(sql, values)

    conn.commit()
    conn.close()
