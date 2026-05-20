# 📦 Reto de Gestión de Stock - Arquitectura SOLID

Este proyecto implementa un sistema modular y escalable para la gestión de inventarios (CRUD de productos), diseñado bajo los **Principios S.O.L.I.D.** de la programación orientada a objetos y utilizando una arquitectura desacoplada en **Python**.

---

## Estructura del Proyecto

El código está organizado de manera modular siguiendo las mejores prácticas de Clean Code:

* **`main.py` (Punto de Entrada):** Inicializa la aplicación, realiza la *Inyección de Dependencias* y ejecuta la demostración del flujo del sistema.
* **`src/__init__.py`:** Archivo de inicialización que transforma el directorio en un paquete ejecutable reconocido por Python.
* **`src/entities.py`:** Contiene la clase `Product`, modelando el núcleo del negocio y encapsulando sus atributos esenciales (ID, nombre, precio, descripción, cantidad).
* **`src/interfaces.py`:** Define `StockRepositoryInterface`, el contrato abstracto que desacopla la lógica comercial de la tecnología de persistencia.
* **`src/manager.py`:** Contiene la clase `StockManager`, encargada de coordinar y orquestar las reglas del negocio y el CRUD de stock.
* **`src/repositories.py`:** Implementa `InMemoryStockRepository`, manejando el almacenamiento y la manipulación segura de los datos en memoria.

---

## Principios S.O.L.I.D. Aplicados

1. **SRP (Responsabilidad Única):** Cada clase tiene una única razón para cambiar. `Product` solo modela datos, `InMemoryStockRepository` solo maneja persistencia, y `StockManager` solo coordina la lógica.
2. **OCP (Abierto/Cerrado):** El sistema está abierto a la extensión pero cerrado a la modificación. Se pueden añadir nuevos tipos de repositorios sin alterar la lógica de negocio.
3. **LSP (Sustitución de Liskov):** `InMemoryStockRepository` hereda e implementa fielmente el contrato de su interfaz, garantizando que puede sustituir a la abstracción sin romper el programa.
4. **ISP (Segregación de Interfaces):** La interfaz de almacenamiento es específica y compacta; define únicamente los métodos requeridos para cumplir con el CRUD del negocio.
5. **DIP (Inversión de Dependencias):** El componente de alto nivel (`StockManager`) no depende del componente de bajo nivel (`InMemoryStockRepository`). Ambos dependen de la abstracción (`StockRepositoryInterface`) mediante *Inyección de Dependencias* en el constructor.

---

## Instrucciones de Ejecución

Debido a posibles restricciones de seguridad, políticas de red o falta de permisos de administrador locales, el entorno está preparado para ejecutarse utilizando una versión portable o el entorno configurado en Visual Studio Code.

### 1. Preparación del Entorno
Asegúrese de abrir la terminal de comandos integrada en VS-Code y situarse dentro de la carpeta del proyecto ejecutable:
```powershell
cd proyecto