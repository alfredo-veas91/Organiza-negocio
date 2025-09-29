from database import init_db, add_product, get_all_products, get_product_by_barcode, get_product_by_name, delete_all_products

# Inicializar la BD (solo una vez al inicio del programa)
init_db()

delete_all_products()

# Agregar productos
add_product("1234567890123", "Coca Cola 1L", 50, 1200.0)  # con código
add_product(None, "Pan Amasado", 100, 300.0)       
add_product(None, "Pan batido", 100, 300.0)       # sin código

# Listar

for p in get_all_products():
    print(p)

# Buscar por código
print(get_product_by_barcode("1234567890123"))
results = get_product_by_name("Pan")

for r in results:
    print(r)