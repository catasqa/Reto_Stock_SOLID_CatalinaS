from typing import List, Optional
from src.entities import Product
from src.interfaces import StockRepositoryInterface

class InMemoryStockRepository(StockRepositoryInterface):
    """Implementación específica para manejar el stock en memoria (Listas)."""
    
    def __init__(self):
        self._products: List[Product] = []

    def save(self, product: Product) -> None:
        self._products.append(product)

    def get_all(self) -> List[Product]:
        return self._products

    def delete(self, id_product: int) -> bool:
        product = self.find_by_id(id_product)
        if product:
            self._products.remove(product)
            return True
        return False

    def find_by_id(self, id_product: int) -> Optional[Product]:
        for product in self._products:
            if product.id_product == id_product:
                return product
        return None