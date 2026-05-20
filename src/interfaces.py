from abc import ABC, abstractmethod
from typing import List, Optional
from src.entities import Product

class StockRepositoryInterface(ABC):
    """Interfaz abstracta que define el comportamiento obligatorio para cualquier repositorio de stock."""
    
    @abstractmethod
    def save(self, product: Product) -> None:
        pass

    @abstractmethod
    def get_all(self) -> List[Product]:
        pass

    @abstractmethod
    def delete(self, id_product: int) -> bool:
        pass

    @abstractmethod
    def find_by_id(self, id_product: int) -> Optional[Product]:
        pass