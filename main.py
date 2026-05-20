import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.repositories import InMemoryStockRepository
from src.manager import StockManager

def run_challenge_demo():
    print("==================================================")
    print("  INICIANDO DEMOSTRACIÓN DE GESTIÓN DE STOCK  ")
    print("==================================================\n")

    # 1. Configuración de infraestructura (Instancias e Inyección)
    repo_en_memoria = InMemoryStockRepository()
    manager = StockManager(repo_en_memoria)

    # 2. Guardar Productos
    print("--- 1. Guardando productos en el Stock ---")
    manager.add_item(101, "Monitor 24''", 150.00, "Monitor LED FHD IPS", 10)
    manager.add_item(102, "Teclado Mecánico", 45.50, "Teclado RGB Switch Blue", 25)
    manager.add_item(103, "Mouse Óptico", 20.00, "Mouse ergonómico inalámbrico", 50)

    # 3. Visualizar productos guardados
    manager.show_stock()

    # 4. Actualizar un producto existente
    print("--- 2. Actualizando un producto (ID 102) ---")
    manager.update_item(102, "Teclado Mecánico Pro", 55.00, "Teclado RGB Switch Red", 15)
    
    # Visualizar cambios
    manager.show_stock()

    # 5. Eliminar un producto
    print("--- 3. Eliminando un producto (ID 101) ---")
    manager.remove_item(101)

    # 6. Visualizar stock final
    manager.show_stock()
    
    print("==================================================")
    print("         FIN DE LA PRUEBA DE ACEPTACIÓN           ")
    print("==================================================")

if __name__ == "__main__":
    run_challenge_demo()