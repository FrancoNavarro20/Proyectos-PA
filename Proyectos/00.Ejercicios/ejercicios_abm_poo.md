# Ejercicios Prácticos: Sistemas ABM con POO en Python

Estos ejercicios están diseñados para practicar los mismos conceptos vistos en `abm_libreria.py` (Clases, Encapsulamiento con `@property`, Diccionarios, y Manejo de Excepciones). 

El objetivo es construir un programa de consola con un menú interactivo (Alta, Baja, Modificación y Lectura) para cada uno de los siguientes escenarios.

---

## Ejercicio 1: Sistema de Gestión Escolar (ABM de Alumnos)

**Objetivo:** Crear un sistema para registrar alumnos de un colegio.

1. **Clase `Alumno`**:
   - Atributos: `id_alumno`, `nombre`, `curso`, y `promedio`.
   - **Validación (Encapsulamiento)**: Utiliza `@property` y un setter para el atributo `promedio`. Asegúrate de que el promedio ingresado no pueda ser menor a 0 ni mayor a 10. Si el usuario intenta poner un promedio fuera de rango, debe lanzar un `ValueError`.

2. **Clase `GestorAlumnos`**:
   - Debe tener un diccionario vacío al inicio.
   - Implementar métodos para: `agregar_alumno`, `listar_alumnos`, `actualizar_alumno`, y `eliminar_alumno`.
   - *Opcional*: Crea un decorador `@registro_actividad` que imprima un mensaje cada vez que se agregue o elimine un alumno.

3. **Menú Interactivo**:
   - Crea un menú (while True) con opciones del 1 al 5.
   - Aplica bloques `try...except` para evitar que el programa falle si el usuario ingresa letras en el "ID" o en el "promedio".

---

## Ejercicio 2: Inventario de un Kiosco (ABM de Productos)

**Objetivo:** Desarrollar un pequeño sistema para controlar el stock de los productos de un negocio.

1. **Clase `Producto`**:
   - Atributos: `codigo_barras` (actuará como ID), `nombre`, `precio`, y `stock_disponible`.
   - **Validación (Encapsulamiento)**: Utiliza `@property` y un setter para el `stock_disponible`. El stock nunca puede ser un número negativo (pero sí puede ser 0). Si es negativo, lanza un `ValueError`.
   - *Extra*: Valida también que el `precio` no sea negativo de la misma manera.

2. **Clase `Inventario` (El Gestor)**:
   - Debe tener un diccionario `self.productos = {}`.
   - Métodos: `alta_producto`, `mostrar_inventario`, `modificar_stock_o_precio`, y `baja_producto`.

3. **Menú Interactivo**:
   - Antes de pedir los datos para agregar un producto, pídele solo el "Código de Barras". Si el código ya existe en el diccionario, avísale al usuario y vuelve al menú (exactamente como hicimos en la librería).

---

## Ejercicio 3: Clínica Veterinaria (ABM de Mascotas)

**Objetivo:** Un registro de pacientes para un veterinario.

1. **Clase `Mascota`**:
   - Atributos: `numero_ficha`, `nombre`, `especie` (ej: Perro, Gato, Loro), y `peso_kg`.
   - **Validación (Encapsulamiento)**: Utiliza `@property` para el `peso_kg`. Una mascota no puede pesar 0 ni tener peso negativo. Lanza un error apropiado.

2. **Clase `Veterinaria`**:
   - Crea el diccionario para guardar las mascotas.
   - Crea los 4 métodos clásicos de ABM.
   - *Desafío*: Agrega un método extra llamado `listar_por_especie(especie_buscada)` que reciba la palabra "Perro" o "Gato" e imprima solo los pacientes que coincidan con esa especie. Agrega esta opción nueva en el menú principal.

---

### Tips y Consejos para resolverlos:
*   **Aprovechen el código de la librería:** Úsenlo como plantilla. La estructura del `while True`, los `input()` y la clase Gestora es casi idéntica, solo cambian los nombres de las variables y el contexto.
*   **Prueben romper su programa:** Cuando terminen, intenten ingresar letras donde van números, o dejen campos vacíos para ver si el programa explota. Si no explota, ¡hicieron un buen trabajo con el `try/except`!
