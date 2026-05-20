from src.entities import Product
from src.interfaces import StockRepositoryInterface

class StockManager:
    """Clase de alto nivel que gestiona las operaciones de stock mediante inversión de dependencias."""
    
    def __init__(self, repository: StockRepositoryInterface):
        # Inyección de dependencias por constructor
        self.repository = repository

    def add_item(self, id_product: int, name: str, price: float, description: str, quantity: int = 0):
        # El envío de información se realiza a través de una instancia de Product
        new_product = Product(id_product, name, price, description, quantity)
        self.repository.save(new_product)
        print(f"✓ Producto '{name}' guardado con éxito.")

    def show_stock(self):
        products = self.repository.get_all()
        if not products:
            print("\nEl stock está vacío.")
            return
        
        print("\n=== VISTA DE PRODUCTOS EN STOCK ===")
        for prod in products:
            print(f"ID: {prod.id_product} | Nombre: {prod.name} | Precio: ${prod.price:.2f} | Cantidad: {prod.quantity}")
        print("===================================\n")

    def remove_item(self, id_product: int):
        success = self.repository.delete(id_product)
        if success:
            print(f"✓ Producto con ID {id_product} eliminado correctamente.")
        else:
            print(f"✗ No se encontró ningún producto con el ID {id_product}.")

    def update_item(self, id_product: int, name: str, price: float, description: str, quantity: int):
        product = self.repository.find_by_id(id_product)
        if product:
            product.update_details(name, price, description, quantity)
            print(f"✓ Producto con ID {id_product} actualizado con éxito.")
        else:
            print(f"✗ Error: No se puede actualizar. ID {id_product} no existe.")