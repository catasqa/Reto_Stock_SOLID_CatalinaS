
class Product:
    """Representa la entidad de un Producto con sus atributos."""
    def __init__(self, id_product: int, name: str, price: float, description: str, quantity: int = 0):
        self.id_product = id_product
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity  # Criterio opcional incluido
        
    def update_details(self, name: str, price: float, description: str, quantity: int):
        """Modifica el estado interno del producto."""
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity