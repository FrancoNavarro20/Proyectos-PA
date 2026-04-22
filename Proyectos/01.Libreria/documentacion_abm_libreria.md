# Documentación del Proyecto: ABM de Librería

Este documento explica paso a paso el funcionamiento del script `abm_libreria.py`. Se trata de una aplicación de consola en Python que implementa un sistema básico de ABM (Alta, Baja, Modificación y Lectura) para gestionar libros, simulando una pequeña base de datos en memoria.

El programa destaca por aplicar buenas prácticas de **Programación Orientada a Objetos (POO)** y conceptos avanzados de Python como **decoradores**, **encapsulamiento** y **manejo de excepciones**.

---

## 1. El Decorador Personalizado (`log_operacion`)

El archivo comienza importando el módulo `functools`. 

```python
import functools

def log_operacion(operacion):
    def decorador(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"\n>>> Iniciando operación: {operacion}")
            resultado = func(*args, **kwargs)
            print(f">>> Operación '{operacion}' finalizada exitosamente.")
            return resultado
        return wrapper
    return decorador
```

**¿Qué hace?**
Un decorador en Python permite extender o modificar el comportamiento de una función sin alterar su código interno. En este caso, `log_operacion` recibe un texto (el nombre de la operación) e imprime un mensaje de "Inicio" y otro de "Finalización" cada vez que la función envuelta (`wrapper`) se ejecuta. Se utiliza la librería `functools.wraps` para no perder el nombre original de la función que estamos decorando.

---

## 2. La Clase `Libro` (El Modelo de Datos)

Esta clase representa la entidad principal de nuestro sistema.

```python
class Libro:
    def __init__(self, id_libro, titulo, autor, precio):
        self._id = id_libro
        self.titulo = titulo
        self.autor = autor
        self.precio = precio 
```

### Encapsulamiento y Validaciones
Se utiliza el concepto de propiedades (`@property` y `@setter`) para proteger los datos:

*   **Atributos Privados:** El `_id` y `_precio` (implícito) están pensados para no ser modificados directamente.
*   **Getters (`@property`)**: Permiten acceder al `id` y al `precio` de forma segura.
*   **Setters (`@precio.setter`)**: Se intercepta la asignación del precio. Si alguien intenta asignarle al libro un precio negativo (`libro.precio = -500`), el setter lanzará un error (`ValueError`), protegiendo la consistencia de los datos.

Por último, incluye el método **`__str__`**, el cual le indica a Python cómo debe imprimirse un objeto `Libro` por consola de forma amigable.

---

## 3. La Clase `GestorLibros` (La Lógica de Negocio)

Esta clase se encarga de administrar todos los libros. Funciona como un controlador.

*   **Base de datos en memoria (`__init__`)**: Utiliza un diccionario `self.libros = {}` donde la "clave" es el ID del libro y el "valor" es el objeto `Libro` completo.
*   **Alta (`agregar_libro`)**: Crea un objeto `Libro` nuevo y lo guarda en el diccionario. Si el precio era negativo, captura el error gracias a un bloque `try...except`.
*   **Lectura (`listar_libros`)**: Recorre el diccionario de libros usando `.values()` e imprime cada uno.
*   **Modificación (`actualizar_libro`)**: Busca el libro por ID y modifica sus atributos solo si el usuario envió valores nuevos.
*   **Baja (`eliminar_libro`)**: Saca el libro del diccionario utilizando el método `.pop()`.

> **Nota:** Todos los métodos del Gestor que realizan acciones importantes tienen el decorador `@log_operacion` arriba, lo que significa que cada vez que se ejecuten, se imprimirá la traza automáticamente.

---

## 4. El Menú Interactivo (`mostrar_menu` y `main`)

La función `main()` es el punto de entrada del programa.

1.  **Instanciación**: Primero crea un objeto `GestorLibros()` y carga dos libros de prueba para que la base de datos no empiece vacía.
2.  **Bucle Principal (`while True`)**: Mantiene el programa corriendo infinitamente hasta que el usuario decida presionar la opción 5 ("Salir").
3.  **Captura de Errores (Robustez)**: Todos los ingresos del usuario están dentro de bloques `try...except ValueError`. Si el sistema pide un número (como el ID o el precio) y el usuario ingresa letras, el programa no se "romperá" (no lanzará una excepción fatal que cierre la app), sino que le mostrará un aviso amigable y volverá a mostrar el menú.
4.  **Validación Temprana (Mejora de UX)**: En las opciones de Agregar (Opción 1) y Modificar (Opción 3), el programa primero pide el ID. **Inmediatamente verifica** si ese ID ya existe (al agregar) o no existe (al modificar). Si hay un problema, detiene la operación usando la palabra reservada `continue`, retornando al menú antes de pedirle al usuario que escriba innecesariamente el resto de los datos (título, autor, precio).

---

## ¿Cómo ejecutar el programa?

Para correr el programa, basta con abrir una terminal en la misma carpeta del archivo y ejecutar:

```bash
python abm_libreria.py
```
