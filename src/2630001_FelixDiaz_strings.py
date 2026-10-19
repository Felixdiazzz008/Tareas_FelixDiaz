# ============================================================
# PORTADA
# ============================================================
# Nombre: Felix Everardo Diaz Berlanga
# Matrícula: 2630001
# Grupo: 1-1
# Carrera: Ingeniería en Mecatrónica - Universidad Politécnica de Cd Victoria
# Tarea: Strings en Python (t_strings)
# GitHub: https://github.com/Felixdiazzz008/Tareas_FelixDiaz.git

# ============================================================
# RESUMEN 
# ============================================================
# Un string en Python es el tipo de dato "str", que sirve para guardar texto
# (letras, números, símbolos y espacios). Los strings son inmutables, o sea
# que no se pueden cambiar directamente: si uso lower() o replace() Python
# crea otra cadena nueva y la original se queda igual.
# Con strings se puede concatenar (+), sacar la longitud (len()), sacar partes
# con slicing, buscar texto (in, find(), count()) y reemplazar texto (replace()).
# Es importante validar y normalizar lo que escribe el usuario porque puede
# poner espacios de más o mayúsculas y minúsculas mezcladas, y así "Ana" y
# "ana " serían datos diferentes.
# En esta tarea hago 6 problemas con strings: nombre e iniciales, correo,
# palíndromo, estadísticas de una oración, contraseña y etiqueta de producto.
# Cada uno tiene su descripción, entradas, salidas, validaciones y 3 casos
# de prueba.

# ============================================================
# BUENAS PRÁCTICAS
# ============================================================
# - Los strings son inmutables, cada cambio genera una cadena nueva.
# - Es bueno usar strip() y lower() antes de comparar texto.
# - Explicar qué saca cada slice para no usar números sin sentido.
# - Usar los métodos que ya trae Python en lugar de hacerlo todo a mano.
# - Primero revisar que no esté vacío y luego revisar el formato.
# - Poner nombres de variables claros y mensajes de error que se entiendan.

# Constantes que uso en el programa
MIN_PALINDROME_LENGTH = 3
MIN_PASSWORD_LENGTH = 8
LABEL_LENGTH = 30


# ============================================================
# Problem 1: Full name formatter (name + initials)
# ============================================================
# Descripción: el programa pide un nombre completo, le quita los espacios de
# más, lo pone en Title Case y muestra las iniciales (por ejemplo J.C.T.).
# Entradas: full_name (string)
# Salidas: "Formatted name: ..." y "Initials: ..."
# Validaciones: que no esté vacío después de strip() y que tenga al menos
# dos palabras.
# Casos de prueba:
#   1) Normal: "  juan   carlos TOVAR " -> Juan Carlos Tovar / J.C.T.
#   2) Borde: "ana lopez" -> Ana Lopez / A.L.
#   3) Error: "Madonna" -> Error: invalid input
print("--- Problem 1: Full name formatter ---")
full_name = input("Enter full name: ")
words = full_name.strip().split()  # split() ya quita los espacios de más

if len(words) < 2:
    print("Error: invalid input")
else:
    formatted_name = " ".join(words).title()
    initials = ""
    for word in formatted_name.split():
        initials = initials + word[0] + "."  # word[0] es la primera letra
    print("Formatted name:", formatted_name)
    print("Initials:", initials)


# ============================================================
# Problem 2: Simple email validator (structure + domain)
# ============================================================
# Descripción: revisa si un correo tiene formato básico correcto: un solo '@',
# un '.' después del '@' y sin espacios. Si es válido muestra el dominio.
# Entradas: email_text (string)
# Salidas: "Valid email: true/false" y "Domain: ..." si es válido
# Validaciones: no vacío con strip(), count('@') igual a 1, sin espacios y
# con '.' en el dominio.
# Casos de prueba:
#   1) Normal: "2630001@upv.edu.mx" -> true, Domain: upv.edu.mx
#   2) Borde: "a@b.c" -> true, Domain: b.c
#   3) Error: "user@@mail.com" -> Valid email: false
print("")
print("--- Problem 2: Email validator ---")
email_text = input("Enter email: ").strip()

if email_text == "":
    print("Error: invalid input")
else:
    at_count = email_text.count("@")
    if at_count != 1 or " " in email_text:
        print("Valid email: false")
    else:
        at_position = email_text.find("@")
        local_part = email_text[:at_position]       # lo que está antes del @
        domain_part = email_text[at_position + 1:]  # lo que está después del @
        if local_part == "" or "." not in domain_part:
            print("Valid email: false")
        else:
            print("Valid email: true")
            print("Domain:", domain_part)


# ============================================================
# Problem 3: Palindrome checker (ignoring spaces and case)
# ============================================================
# Descripción: dice si una frase es palíndromo (se lee igual al derecho y al
# revés) sin tomar en cuenta los espacios ni mayúsculas.
# Entradas: phrase (string)
# Salidas: "Normalized: ..." y "Is palindrome: true/false"
# Validaciones: no vacía con strip() y con mínimo 3 caracteres ya limpia.
# Casos de prueba:
#   1) Normal: "Anita lava la tina" -> anitalavalatina, true
#   2) Borde: "aba" -> aba, true
#   3) Error: "   " -> Error: invalid input
print("")
print("--- Problem 3: Palindrome checker ---")
phrase = input("Enter phrase: ")
normalized_text = phrase.strip().lower().replace(" ", "")

if len(normalized_text) < MIN_PALINDROME_LENGTH:
    print("Error: invalid input")
else:
    reversed_text = normalized_text[::-1]  # [::-1] da el texto al revés
    print("Normalized:", normalized_text)
    if normalized_text == reversed_text:
        print("Is palindrome: true")
    else:
        print("Is palindrome: false")


# ============================================================
# Problem 4: Sentence word stats (lengths and first/last word)
# ============================================================
# Descripción: separa una oración en palabras y muestra cuántas son, la
# primera, la última, la más corta y la más larga. Si hay empate se queda la
# primera que salió. Le quito los signos de puntuación a cada palabra.
# Entradas: sentence (string)
# Salidas: "Word count", "First word", "Last word", "Shortest word",
# "Longest word"
# Validaciones: no vacía con strip() y que tenga al menos una palabra.
# Casos de prueba:
#   1) Normal: "The quick brown fox jumps" -> 5, The, jumps, The, quick
#   2) Borde: "Hello" -> 1, Hello, Hello, Hello, Hello
#   3) Error: "   " -> Error: invalid input
print("")
print("--- Problem 4: Sentence word stats ---")
sentence = input("Enter sentence: ")
raw_words = sentence.strip().split()
clean_words = []
for raw_word in raw_words:
    clean_word = raw_word.strip(".,;:!?")  # quita puntuación de las orillas
    if clean_word != "":
        clean_words.append(clean_word)

if len(clean_words) == 0:
    print("Error: invalid input")
else:
    shortest_word = clean_words[0]
    longest_word = clean_words[0]
    for word in clean_words:
        if len(word) < len(shortest_word):
            shortest_word = word
        if len(word) > len(longest_word):
            longest_word = word
    print("Word count:", len(clean_words))
    print("First word:", clean_words[0])
    print("Last word:", clean_words[-1])  # [-1] es el último elemento
    print("Shortest word:", shortest_word)
    print("Longest word:", longest_word)


# ============================================================
# Problem 5: Password strength classifier
# ============================================================
# Descripción: clasifica una contraseña como weak, medium o strong.
# Mis reglas:
#   - weak: menos de 8 caracteres o solo un tipo de carácter
#   - strong: 8 o más caracteres y tiene mayúscula, minúscula, número y símbolo
#   - medium: todo lo demás (8 o más caracteres con 2 o 3 tipos)
# Entradas: password_input (string)
# Salidas: "Password strength: weak/medium/strong"
# Validaciones: que no esté vacía y revisar la longitud con len().
# Casos de prueba:
#   1) Normal: "Secur3#Pass" -> strong
#   2) Borde: "Abcdef12" (8 caracteres, sin símbolo) -> medium
#   3) Error: "" -> Error: invalid input
print("")
print("--- Problem 5: Password strength ---")
password_input = input("Enter password: ")

if password_input.strip() == "":
    print("Error: invalid input")
else:
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False
    for character in password_input:
        if character.isupper():
            has_upper = True
        elif character.islower():
            has_lower = True
        elif character.isdigit():
            has_digit = True
        elif not character.isalnum() and character != " ":
            has_symbol = True

    # Cuento cuántos tipos de carácter tiene (True vale 1 y False vale 0)
    kinds_count = has_upper + has_lower + has_digit + has_symbol

    if len(password_input) < MIN_PASSWORD_LENGTH or kinds_count <= 1:
        print("Password strength: weak")
    elif kinds_count == 4:
        print("Password strength: strong")
    else:
        print("Password strength: medium")


# ============================================================
# Problem 6: Product label formatter (fixed-width text)
# ============================================================
# Descripción: arma la etiqueta "Product: <NAME> | Price: $<PRICE>" y la deja
# de exactamente 30 caracteres. Si es más corta le pongo espacios al final y
# si es más larga la recorto con label[:30].
# Entradas: product_name (string) y price_text (string, se convierte a número)
# Salidas: Label: "<30 caracteres>" (con comillas para ver los espacios)
# Validaciones: nombre no vacío con strip() y precio que sea un número mayor
# que 0.
# Casos de prueba:
#   1) Normal: "Pen", "5.5" -> "Product: Pen | Price: $5.50   "
#   2) Borde: "Pencil", "1" -> "Product: Pencil | Price: $1.00" (mide 30)
#   3) Error: "Pen", "-3" -> Error: invalid input
print("")
print("--- Problem 6: Product label ---")
product_name = input("Enter product name: ").strip()
price_text = input("Enter price: ").strip()

# replace(".", "", 1) quita un punto para poder revisar con isdigit()
if product_name == "" or not price_text.replace(".", "", 1).isdigit():
    print("Error: invalid input")
else:
    price_number = float(price_text)
    if price_number <= 0:
        print("Error: invalid input")
    else:
        label = "Product: " + product_name + " | Price: $" + f"{price_number:.2f}"
        if len(label) < LABEL_LENGTH:
            label = label + " " * (LABEL_LENGTH - len(label))  # relleno
        label = label[:LABEL_LENGTH]  # recorte a 30 caracteres
        print('Label: "' + label + '"')


# ============================================================
# CONCLUSIONES
# ============================================================
# Los strings son muy importantes para recibir y mostrar datos, porque casi
# siempre el usuario escribe texto. Aprendí que strip() y lower() conviene
# usarlos al inicio para limpiar lo que escribe el usuario, que split() sirve
# para separar palabras y que join() sirve para unirlas otra vez.
# Normalizar el texto antes de compararlo evita errores, por ejemplo que "Ana"
# y "ana " se tomen como diferentes. Las validaciones ayudan a que no entren
# datos basura al programa y a mostrar mensajes de error claros.
# También aprendí que los strings son inmutables, o sea que los métodos
# regresan una cadena nueva que hay que guardar en una variable, y que los
# slices como [::-1] y [:30] sirven para dar vuelta o recortar texto.

# ============================================================
# REFERENCIAS
# ============================================================
# References:
# 1) Python Software Foundation. Documentación de Python - Tipos integrados:
#    Tipos de secuencia de texto (str). https://docs.python.org/es/3/library/stdtypes.html
# 2) Python Software Foundation. Tutorial de Python - Cadenas de caracteres.
#    https://docs.python.org/es/3/tutorial/introduction.html
# 3) van Rossum, G., Warsaw, B. y Coghlan, A. PEP 8 - Style Guide for Python
#    Code. https://peps.python.org/pep-0008/