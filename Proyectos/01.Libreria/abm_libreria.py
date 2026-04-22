import functools

# Decorador personalizado para loguear las operaciones
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


class Libro:
    """Clase principal para representar un Libro en el sistema."""
    
    def __init__(self, id_libro, titulo, autor, precio):
        self._id = id_libro
        self.titulo = titulo
        self.autor = autor
        self.precio = precio  # Llama al setter con validación

    # Ejemplo de uso del decorador @property para encapsulamiento
    @property
    def id(self):
        return self._id

    @property
    def precio(self):
        return self._precio

    # Validamos que el precio no pueda ser negativo usando el setter
    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = valor

    def __str__(self):
        return f"[ID: {self._id}] {self.titulo} - {self.autor} | ${self.precio:.2f}"


class GestorLibros:
    """Clase para manejar el ABM (Alta, Baja, Modificación) de los libros."""
    
    def __init__(self):
        # Usamos un diccionario para simular una pequeña base de datos en memoria (id -> Libro)
        self.libros = {}

    @log_operacion("Alta de Libro")
    def agregar_libro(self, id_libro, titulo, autor, precio):
        if id_libro in self.libros:
            print(f"Error: Ya existe un libro con el ID {id_libro}.")
            return False
        
        try:
            nuevo_libro = Libro(id_libro, titulo, autor, precio)
            self.libros[id_libro] = nuevo_libro
            print(f"Libro agregado al gestor: {nuevo_libro.titulo}")
            return True
        except ValueError as e:
            print(f"Error de validación: {e}")
            return False

    @log_operacion("Lectura / Listado de Libros")
    def listar_libros(self):
        if not self.libros:
            print("No hay libros registrados en el sistema en este momento.")
            return
        
        print("\n--- Lista de Libros ---")
        for libro in self.libros.values():
            print(libro)
        print("-----------------------")

    @log_operacion("Modificación de Libro")
    def actualizar_libro(self, id_libro, nuevo_titulo=None, nuevo_autor=None, nuevo_precio=None):
        if id_libro not in self.libros:
            print(f"Error: No se encontró un libro con el ID {id_libro}.")
            return False

        libro = self.libros[id_libro]
        
        try:
            if nuevo_titulo:
                libro.titulo = nuevo_titulo
            if nuevo_autor:
                libro.autor = nuevo_autor
            if nuevo_precio is not None:
                libro.precio = nuevo_precio  # Esto pasa por la validación del setter
            print(f"Libro ID {id_libro} actualizado correctamente.")
            return True
        except ValueError as e:
            print(f"Error de validación al actualizar: {e}")
            return False

    @log_operacion("Baja de Libro")
    def eliminar_libro(self, id_libro):
        if id_libro in self.libros:
            libro = self.libros.pop(id_libro)
            print(f"Libro eliminado del sistema: {libro.titulo}")
            return True
        else:
            print(f"Error: No se encontró un libro con el ID {id_libro}.")
            return False


def mostrar_menu():
    print("\n" + "="*35)
    print(" 📚 SISTEMA ABM DE LIBRERÍA 📚 ")
    print("="*35)
    print("[1] Agregar Libro (Alta)")
    print("[2] Mostrar Libros (Lectura)")
    print("[3] Actualizar Libro (Modificación)")
    print("[4] Eliminar Libro (Baja)")
    print("[5] Salir")
    print("="*35)


def main():
    gestor = GestorLibros()
    
    # Cargamos un par de datos de prueba al iniciar
    gestor.agregar_libro(1, "El Aleph", "Jorge Luis Borges", 15000.0)
    gestor.agregar_libro(2, "Ficciones", "Jorge Luis Borges", 12500.0)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            try:
                id_libro = int(input("Ingrese ID numérico del libro: "))
                if id_libro in gestor.libros:
                    print(f"Error: Ya existe un libro con el ID {id_libro}.")
                    continue
                titulo = input("Ingrese Título: ").strip()
                autor = input("Ingrese Autor: ").strip()
                precio = float(input("Ingrese Precio: "))
                gestor.agregar_libro(id_libro, titulo, autor, precio)
            except ValueError:
                print("Error: El ID debe ser entero y el precio debe ser un número válido.")

        elif opcion == "2":
            gestor.listar_libros()

        elif opcion == "3":
            try:
                id_libro = int(input("Ingrese ID del libro a modificar: "))
                if id_libro not in gestor.libros:
                    print(f"Error: No se encontró un libro con el ID {id_libro}.")
                    continue
                titulo = input("Nuevo Título (presione Enter para dejar sin cambios): ").strip()
                autor = input("Nuevo Autor (presione Enter para dejar sin cambios): ").strip()
                precio_str = input("Nuevo Precio (presione Enter para dejar sin cambios): ").strip()
                
                titulo = titulo if titulo else None
                autor = autor if autor else None
                precio = float(precio_str) if precio_str else None
                
                gestor.actualizar_libro(id_libro, titulo, autor, precio)
            except ValueError:
                print("Error: El ID y Precio ingresados deben ser valores numéricos válidos.")

        elif opcion == "4":
            try:
                id_libro = int(input("Ingrese ID del libro a eliminar: "))
                gestor.eliminar_libro(id_libro)
            except ValueError:
                print("Error: El ID debe ser un número entero.")

        elif opcion == "5":
            print("Saliendo del sistema... ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione un número del 1 al 5.")


if __name__ == "__main__":
    main()
