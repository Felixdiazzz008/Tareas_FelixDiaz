# ============================================================
# PORTADA
# ============================================================
# Nombre: Felix Everardo Diaz Berlanga
# Matrícula: 2630001
# Grupo: 1-1
# Carrera: Ingeniería en Mecatrónica - Universidad Politécnica de Cd Victoria
# Tarea: Colecciones en Python (listas y tuplas)
# GitHub: https://github.com/Felixdiazzz008/Tareas_FelixDiaz.git

# ============================================================
# RESUMEN 
# ============================================================
# Una lista (list) guarda varios valores en orden y es mutable, o sea que se
# le pueden agregar, quitar o cambiar elementos (append, remove, pop, etc.).
# Una tupla (tuple) también guarda valores en orden, pero es inmutable: una
# vez creada ya no se puede modificar, por eso sirve para datos fijos como
# las coordenadas de un punto.
# Un diccionario (dict) guarda parejas clave-valor, pero en clase todavía no lo
# hemos visto, así que en esta tarea NO lo uso. En los problemas que lo
# pedían, lo resolví con listas paralelas (dos listas donde la posición i de
# una corresponde a la posición i de la otra) y con listas de listas o de
# tuplas.
# Es importante validar los datos: que el texto no esté vacío, que los
# índices existan y que las listas no estén vacías antes de calcular promedios,
# para que el programa no se caiga.
# En este documento hago 6 problemas: lista de compras, puntos con tuplas,
# catálogo de productos, calificaciones, frecuencia de palabras y libreta de
# contactos, cada uno con descripción, entradas, salidas, validaciones y
# 3 casos de prueba.

# ============================================================
# BUENAS PRÁCTICAS
# ============================================================
# - Usar listas cuando se necesite agregar o quitar elementos seguido.
# - Usar tuplas para datos que no deben cambiar (coordenadas, pares fijos).
# - Con listas paralelas, siempre agregar o quitar en las dos listas al mismo
#   tiempo para que no se desacomoden.
# - No modificar una lista mientras la recorro con un for.
# - Revisar que la lista no esté vacía antes de usar sum()/len() para
#   promedios, y que el índice exista antes de usarlo.
# - Escribir código legible y mensajes claros para el usuario.

# Constantes que uso en el programa
PASSING_GRADE = 70.0
PUNCTUATION_MARKS = ".,;:!?"


# ============================================================
# Problem 1: Shopping list basics (list operations)
# ============================================================
# Descripción: pide una lista de productos separados por comas, agrega un
# producto nuevo al final, muestra cuántos elementos hay y dice si un
# producto buscado está en la lista (found_item).
# Entradas: initial_items_text (string), new_item (string), search_item (string)
# Salidas: "Items list:", "Total items:" y "Found item: true/false"
# Validaciones: los tres textos no vacíos con strip(); a cada elemento le
# quito espacios y lo paso a minúsculas; ignoro los elementos vacíos.
# Mi decisión: si la lista inicial queda vacía (por ejemplo ", ,"), lo tomo
# como entrada inválida.
# Casos de prueba:
#   1) Normal: "apple, banana ,orange", "grape", "banana" ->
#      Items list: ['apple', 'banana', 'orange', 'grape'], Total items: 4,
#      Found item: true
#   2) Borde: "apple", "pear", "kiwi" -> Items list: ['apple', 'pear'],
#      Total items: 2, Found item: false
#   3) Error: "   ", "x", "y" -> Error: invalid input
print("--- Problem 1: Shopping list ---")
initial_items_text = input("Enter items separated by commas: ").strip()
new_item = input("Enter new item: ").strip().lower()
search_item = input("Enter item to search: ").strip().lower()

items_list = []
for raw_item in initial_items_text.split(","):
    clean_item = raw_item.strip().lower()
    if clean_item != "":
        items_list.append(clean_item)

if len(items_list) == 0 or new_item == "" or search_item == "":
    print("Error: invalid input")
else:
    items_list.append(new_item)
    is_in_list = search_item in items_list
    print("Items list:", items_list)
    print("Total items:", len(items_list))
    print("Found item:", str(is_in_list).lower())


# ============================================================
# Problem 2: Points and distances with tuples
# ============================================================
# Descripción: crea dos puntos del plano como tuplas (x, y), calcula la
# distancia entre ellos y crea otra tupla con el punto medio.
# Entradas: x1, y1, x2, y2 (float)
# Salidas: "Point A:", "Point B:", "Distance:" y "Midpoint:"
# Validaciones: que las 4 entradas se puedan convertir a float.
# Casos de prueba:
#   1) Normal: 0, 0, 3, 4 -> Point A: (0.0, 0.0), Point B: (3.0, 4.0),
#      Distance: 5.0, Midpoint: (1.5, 2.0)
#   2) Borde: 2, 2, 2, 2 (mismo punto) -> Distance: 0.0, Midpoint: (2.0, 2.0)
#   3) Error: "abc" -> Error: invalid input
print("")
print("--- Problem 2: Points and distances ---")
input_ok = True
try:
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
except ValueError:
    input_ok = False

if input_ok == False:
    print("Error: invalid input")
else:
    point_a = (x1, y1)
    point_b = (x2, y2)
    # point_a[0] es la x del punto A y point_a[1] es la y
    distance = ((point_b[0] - point_a[0]) ** 2 + (point_b[1] - point_a[1]) ** 2) ** 0.5
    midpoint = (round((x1 + x2) / 2, 2), round((y1 + y2) / 2, 2))
    print("Point A:", point_a)
    print("Point B:", point_b)
    print("Distance:", round(distance, 2))
    print("Midpoint:", midpoint)


# ============================================================
# Problem 3: Product catalog (listas paralelas en lugar de diccionario)
# ============================================================
# Descripción: tengo un catálogo con dos listas paralelas: product_names y
# product_prices (el precio en la posición i es del producto en la posición
# i). El programa pide un producto y una cantidad, y calcula el total si el
# producto existe.
# Entradas: product_name (string), quantity (int)
# Salidas: si existe: "Unit price:", "Quantity:" y "Total:"; si no existe:
# "Error: product not found"
# Validaciones: quantity > 0 y que sea int; product_name no vacío con
# strip(); revisar si el producto está en la lista.
# Casos de prueba:
#   1) Normal: "banana", 3 -> Unit price: 5.5, Quantity: 3, Total: 16.5
#   2) Borde: "apple", 1 -> Unit price: 10.0, Quantity: 1, Total: 10.0
#   3) Error: "pizza", 2 -> Error: product not found
#      (con cantidad 0 o -1 da Error: invalid input)
print("")
print("--- Problem 3: Product catalog ---")
product_names = ["apple", "banana", "orange", "milk"]
product_prices = [10.0, 5.5, 8.0, 22.0]

product_name = input("Enter product name: ").strip().lower()
input_ok = True
try:
    quantity = int(input("Enter quantity: "))
except ValueError:
    input_ok = False

if input_ok == False:
    print("Error: invalid input")
elif product_name == "" or quantity <= 0:
    print("Error: invalid input")
else:
    found = False
    unit_price = 0.0
    # Recorro las posiciones de la lista para buscar el producto
    for i in range(len(product_names)):
        if product_names[i] == product_name:
            found = True
            unit_price = product_prices[i]  # mismo índice en la otra lista
    if found:
        total_price = unit_price * quantity
        print("Unit price:", unit_price)
        print("Quantity:", quantity)
        print("Total:", round(total_price, 2))
    else:
        print("Error: product not found")


# ============================================================
# Problem 4: Student grades (lista de nombres + lista de listas)
# ============================================================
# Descripción: guardo los nombres en una lista (student_names) y las
# calificaciones de cada uno en otra lista de listas (grades_list), donde
# grades_list[i] son las calificaciones del estudiante student_names[i].
# Se pide un nombre, se calcula su promedio y se dice si está aprobado
# (average >= 70.0).
# Entradas: student_name (string)
# Salidas: si existe: "Grades:", "Average:" y "Passed: true/false"; si no
# existe: "Error: student not found"
# Validaciones: student_name no vacío con strip(); revisar que el nombre
# esté en la lista; revisar que sus calificaciones no sean una lista vacía
# (Diego no tiene calificaciones y da "Error: no grades available").
# Casos de prueba:
#   1) Normal: "alice" -> Grades: [90.0, 85.0, 100.0], Average: 91.67,
#      Passed: true
#   2) Borde: "Carla" -> Grades: [70.0, 70.0], Average: 70.0, Passed: true
#      (justo en el límite de 70.0)
#   3) Error: "Zoe" -> Error: student not found
print("")
print("--- Problem 4: Student grades ---")
student_names = ["Alice", "Bob", "Carla", "Diego"]
grades_list = [[90.0, 85.0, 100.0], [60.0, 70.0, 65.0], [70.0, 70.0], []]

student_name = input("Enter student name: ").strip().lower()

if student_name == "":
    print("Error: invalid input")
else:
    position = -1  # -1 significa "todavía no lo encuentro"
    for i in range(len(student_names)):
        if student_names[i].lower() == student_name:
            position = i
    if position == -1:
        print("Error: student not found")
    else:
        student_grades = grades_list[position]
        if len(student_grades) == 0:
            print("Error: no grades available")
        else:
            average = sum(student_grades) / len(student_grades)
            is_passed = average >= PASSING_GRADE
            print("Grades:", student_grades)
            print("Average:", round(average, 2))
            print("Passed:", str(is_passed).lower())


# ============================================================
# Problem 5: Word frequency counter (lista de palabras + lista de tuplas)
# ============================================================
# Descripción: cuenta cuántas veces aparece cada palabra de una oración. Sin
# diccionarios, saco una lista de palabras únicas y para cada una guardo una
# tupla (palabra, veces) usando count().
# Mi decisión sobre la puntuación: reemplazo los signos . , ; : ! ? por un
# espacio antes de separar las palabras.
# Entradas: sentence (string)
# Salidas: "Words list:", "Frequencies:" y "Most common word:" (si hay
# empate, se queda la primera que apareció)
# Validaciones: sentence no vacía con strip() y que la lista de palabras no
# quede vacía (por ejemplo, si solo escriben "...").
# Casos de prueba:
#   1) Normal: "the cat and the dog and the bird" ->
#      Words list: ['the', 'cat', 'and', 'the', 'dog', 'and', 'the', 'bird']
#      Frequencies: [('the', 3), ('cat', 1), ('and', 2), ('dog', 1),
#      ('bird', 1)]  Most common word: the
#   2) Borde: "Hello" -> Words list: ['hello'], Frequencies: [('hello', 1)],
#      Most common word: hello
#   3) Error: "   " -> Error: invalid input
print("")
print("--- Problem 5: Word frequency counter ---")
sentence = input("Enter sentence: ")
text = sentence.strip().lower()
for mark in PUNCTUATION_MARKS:
    text = text.replace(mark, " ")
words_list = text.split()

if len(words_list) == 0:
    print("Error: invalid input")
else:
    unique_words = []
    for word in words_list:
        if word not in unique_words:
            unique_words.append(word)

    frequencies_list = []
    for word in unique_words:
        frequencies_list.append((word, words_list.count(word)))

    # Busco la palabra con más repeticiones
    most_common_word = frequencies_list[0][0]
    max_count = frequencies_list[0][1]
    for pair in frequencies_list:
        if pair[1] > max_count:
            most_common_word = pair[0]
            max_count = pair[1]

    print("Words list:", words_list)
    print("Frequencies:", frequencies_list)
    print("Most common word:", most_common_word)


# ============================================================
# Problem 6: Simple contact book (listas paralelas: agregar, buscar, borrar)
# ============================================================
# Descripción: libreta de contactos con dos listas paralelas, contact_names
# y contact_phones. Según la acción ADD, SEARCH o DELETE, agrega o actualiza
# un contacto, busca su teléfono o lo elimina (con pop() en las dos listas).
# Entradas: action_text (string), name (string) y phone (string, solo en ADD)
# Salidas:
#   ADD: "Contact saved:" name, phone
#   SEARCH: "Phone:" <phone> o "Error: contact not found"
#   DELETE: "Contact deleted:" name o "Error: contact not found"
# Validaciones: action_text se pasa a mayúsculas y debe ser ADD, SEARCH o
# DELETE; name no vacío con strip(); en ADD, phone no vacío con strip().
# Casos de prueba:
#   1) Normal: SEARCH, "alice" -> Phone: 1234567890
#   2) Borde: "add" (minúsculas), "Alice", "999" -> Contact saved: Alice 999
#      (como Alice ya existe, solo se actualiza su teléfono)
#   3) Error: DELETE, "Zoe" -> Error: contact not found
#      (con una acción como "UPDATE" da Error: invalid input)
print("")
print("--- Problem 6: Contact book ---")
contact_names = ["Alice", "Bob", "Carla"]
contact_phones = ["1234567890", "5551234567", "8341112233"]

action_text = input("Enter action (ADD, SEARCH or DELETE): ").strip().upper()

if action_text != "ADD" and action_text != "SEARCH" and action_text != "DELETE":
    print("Error: invalid input")
else:
    name = input("Enter contact name: ").strip()
    if name == "":
        print("Error: invalid input")
    else:
        # Busco la posición del contacto en la lista (-1 si no existe)
        position = -1
        for i in range(len(contact_names)):
            if contact_names[i].lower() == name.lower():
                position = i

        if action_text == "ADD":
            phone = input("Enter phone: ").strip()
            if phone == "":
                print("Error: invalid input")
            else:
                if position == -1:
                    contact_names.append(name)    # contacto nuevo
                    contact_phones.append(phone)
                else:
                    contact_phones[position] = phone  # solo actualizo teléfono
                print("Contact saved:", name, phone)
        elif action_text == "SEARCH":
            if position == -1:
                print("Error: contact not found")
            else:
                print("Phone:", contact_phones[position])
        else:  # DELETE
            if position == -1:
                print("Error: contact not found")
            else:
                contact_names.pop(position)   # quito de las dos listas
                contact_phones.pop(position)
                print("Contact deleted:", name)


# ============================================================
# CONCLUSIONES
# ============================================================
# Aprendí que las listas conviene usarlas cuando los datos cambian, porque
# con append(), pop() y remove() se agregan o se quitan elementos con
# facilidad. Las tuplas me sirvieron para datos que no deben cambiar, como las
# coordenadas de un punto o los pares (palabra, veces). Como todavía no vemos
# diccionarios, para buscar por nombre usé listas paralelas y recorrí las
# posiciones con for, y me di cuenta de que un diccionario haría estas
# búsquedas más directas. También vi patrones que se repiten: buscar la
# posición de un elemento, usar -1 cuando no se encuentra y revisar que una
# lista no esté vacía antes de calcular un promedio.

# ============================================================
# REFERENCIAS
# ============================================================
# References:
#    https://docs.python.org/es/3/library/stdtypes.html
# 1) Python Software Foundation. Tutorial de Python - Estructuras de datos
#    (listas y tuplas). https://docs.python.org/es/3/tutorial/datastructures.html
# 2) Python Software Foundation. Tutorial de Python - Una introducción
#    informal a Python (listas). https://docs.python.org/es/3/tutorial/introduction.html
# 3) van Rossum, G., Warsaw, B. y Coghlan, A. PEP 8 - Style Guide for Python
#    Code. https://peps.python.org/pep-0008/