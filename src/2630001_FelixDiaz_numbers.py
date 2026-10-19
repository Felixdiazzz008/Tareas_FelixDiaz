
# PORTADA

# Nombre: Felix Everardo Diaz Berlanga
# Matrícula: 2630001
# Grupo: 1-1
# Carrera: Ingeniería en Mecatrónica - Universidad Politécnica de Cd Victoria
# Tarea: Números (int y float) y booleanos en Python
# GitHub: https://github.com/Felixdiazzz008/Tareas_FelixDiaz.git

# RESUMEN 
# ============================================================
# En Python, int es el tipo para números enteros (edad, cantidad de piezas) y
# float es el tipo para números con decimales (temperatura, salario). La
# diferencia es que el int no tiene parte decimal y el float sí, y al dividir
# con / el resultado siempre es float.
# Un booleano (bool) solo puede ser True o False. Se obtiene al comparar
# valores con operadores como <, >, <=, >=, == y !=, por ejemplo
# is_high_temperature = temp_c >= 30.0. Con and, or y not se pueden combinar
# varias condiciones.
# Es importante validar los rangos (por ejemplo que las horas no sean
# negativas) y evitar la división entre cero, porque si no el programa se cae
# o da resultados que no tienen sentido.
# En esta tarea hago 6 problemas: convertidor de temperatura, pago con horas
# extra, descuento, estadísticas de tres enteros, préstamo y BMI. Cada uno
# tiene descripción, entradas, salidas, validaciones y 3 casos de prueba.

# ============================================================
# BUENAS PRÁCTICAS
# ============================================================
# - Usar el tipo correcto: int para contadores y float para decimales.
# - Guardar los resultados intermedios en variables para no repetir cuentas.
# - Validar los datos antes de operar (que horas y salarios no sean negativos).
# - Usar nombres de variables claros y mensajes que el usuario entienda.
# - Documentar qué significa true y false en cada problema.

# Constantes que uso en el programa
HIGH_TEMPERATURE_C = 30.0
REGULAR_HOURS_LIMIT = 40
OVERTIME_MULTIPLIER = 1.5
DISCOUNT_FACTOR = 0.9        # 10% de descuento = pagar el 90%
BIG_PURCHASE_LIMIT = 1000.0
MIN_LOAN_INCOME = 8000.0
MAX_DEBT_RATIO = 0.4
MIN_CREDIT_SCORE = 650
UNDERWEIGHT_LIMIT = 18.5
OVERWEIGHT_LIMIT = 25.0


# ============================================================
# Problem 1: Temperature converter and range flag
# ============================================================
# Descripción: convierte una temperatura de Celsius a Fahrenheit y Kelvin, y
# dice si es una temperatura alta (is_high_temperature es true si temp_c >= 30).
# Entradas: temp_c (float)
# Salidas: "Fahrenheit:", "Kelvin:" y "High temperature: true/false"
# Validaciones: que temp_c se pueda convertir a float y que temp_k no sea
# menor que 0.0 (no existe temperatura menor al cero absoluto).
# Casos de prueba:
#   1) Normal: 35 -> Fahrenheit 95.0, Kelvin 308.15, High temperature: true
#   2) Borde: 30 -> Fahrenheit 86.0, Kelvin 303.15, High temperature: true
#   3) Error: "abc" -> Error: invalid input (con -300 también da error
#      porque temp_k queda negativa)
print("--- Problem 1: Temperature converter ---")
input_ok = True
try:
    # float() convierte el texto a número; si no se puede, da ValueError
    temp_c = float(input("Enter temperature in Celsius: "))
except ValueError:
    input_ok = False

if input_ok == False:
    print("Error: invalid input")
else:
    temp_f = temp_c * 9 / 5 + 32
    temp_k = temp_c + 273.15
    if temp_k < 0.0:
        print("Error: invalid input")
    else:
        is_high_temperature = temp_c >= HIGH_TEMPERATURE_C
        print("Fahrenheit:", round(temp_f, 2))
        print("Kelvin:", round(temp_k, 2))
        # str(True).lower() convierte True en el texto "true"
        print("High temperature:", str(is_high_temperature).lower())


# ============================================================
# Problem 2: Work hours and overtime payment
# ============================================================
# Descripción: calcula el pago semanal de un trabajador. Hasta 40 horas se
# pagan normal y las horas extra (más de 40) se pagan al 150%. También dice
# si hubo horas extra (has_overtime).
# Entradas: hours_worked (float) y hourly_rate (float)
# Salidas: "Regular pay:", "Overtime pay:", "Total pay:", "Has overtime:"
# Validaciones: hours_worked >= 0 y hourly_rate > 0
# Casos de prueba:
#   1) Normal: 45 horas, tarifa 100 -> Regular 4000.0, Overtime 750.0,
#      Total 4750.0, Has overtime: true
#   2) Borde: 40 horas, tarifa 100 -> Regular 4000.0, Overtime 0.0,
#      Total 4000.0, Has overtime: false
#   3) Error: -5 horas, tarifa 100 -> Error: invalid input
print("")
print("--- Problem 2: Overtime payment ---")
input_ok = True
try:
    hours_worked = float(input("Enter hours worked: "))
    hourly_rate = float(input("Enter hourly rate: "))
except ValueError:
    input_ok = False

if input_ok == False:
    print("Error: invalid input")
elif hours_worked < 0 or hourly_rate <= 0:
    print("Error: invalid input")
else:
    # min() me da las horas normales (máximo 40) y max() las horas extra
    regular_hours = min(hours_worked, REGULAR_HOURS_LIMIT)
    overtime_hours = max(hours_worked - REGULAR_HOURS_LIMIT, 0)
    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * OVERTIME_MULTIPLIER
    total_pay = regular_pay + overtime_pay
    has_overtime = hours_worked > REGULAR_HOURS_LIMIT
    print("Regular pay:", round(regular_pay, 2))
    print("Overtime pay:", round(overtime_pay, 2))
    print("Total pay:", round(total_pay, 2))
    print("Has overtime:", str(has_overtime).lower())


# ============================================================
# Problem 3: Discount eligibility with booleans
# ============================================================
# Descripción: dice si un cliente tiene descuento. Lo tiene si es estudiante,
# o es de la tercera edad, o su compra es de 1000 o más. Si tiene descuento
# se le aplica el 10%.
# Entradas: purchase_total (float), is_student_text y is_senior_text
# (strings "YES" o "NO")
# Salidas: "Discount eligible: true/false" y "Final total:"
# Validaciones: purchase_total >= 0; los textos se pasan a mayúsculas y
# solo se aceptan "YES" o "NO".
# Casos de prueba:
#   1) Normal: 500, "yes", "no" -> Discount eligible: true, Final total: 450.0
#   2) Borde: 1000, "no", "no" -> Discount eligible: true, Final total: 900.0
#   3) Error: 500, "maybe", "no" -> Error: invalid input
print("")
print("--- Problem 3: Discount eligibility ---")
input_ok = True
try:
    purchase_total = float(input("Enter purchase total: "))
except ValueError:
    input_ok = False
is_student_text = input("Is student? (YES/NO): ").strip().upper()
is_senior_text = input("Is senior? (YES/NO): ").strip().upper()

if input_ok == False:
    print("Error: invalid input")
elif purchase_total < 0.0:
    print("Error: invalid input")
elif is_student_text != "YES" and is_student_text != "NO":
    print("Error: invalid input")
elif is_senior_text != "YES" and is_senior_text != "NO":
    print("Error: invalid input")
else:
    # Convierto el texto "YES"/"NO" a booleano comparando
    is_student = is_student_text == "YES"
    is_senior = is_senior_text == "YES"
    discount_eligible = is_student or is_senior or (purchase_total >= BIG_PURCHASE_LIMIT)
    if discount_eligible:
        final_total = purchase_total * DISCOUNT_FACTOR
    else:
        final_total = purchase_total
    print("Discount eligible:", str(discount_eligible).lower())
    print("Final total:", round(final_total, 2))


# ============================================================
# Problem 4: Basic statistics of three integers
# ============================================================
# Descripción: lee tres enteros y calcula la suma, el promedio (float), el
# máximo, el mínimo y si los tres son pares (all_even).
# Entradas: n1, n2, n3 (int)
# Salidas: "Sum:", "Average:", "Max:", "Min:", "All even:"
# Validaciones: que los valores se puedan convertir a int (se permiten
# negativos).
# Casos de prueba:
#   1) Normal: 4, 7, 10 -> Sum 21, Average 7.0, Max 10, Min 4, All even: false
#   2) Borde: -2, -4, -6 -> Sum -12, Average -4.0, Max -2, Min -6,
#      All even: true
#   3) Error: "3.5" -> Error: invalid input (int() no acepta decimales)
print("")
print("--- Problem 4: Statistics of three integers ---")
input_ok = True
try:
    n1 = int(input("Enter first integer: "))
    n2 = int(input("Enter second integer: "))
    n3 = int(input("Enter third integer: "))
except ValueError:
    input_ok = False

if input_ok == False:
    print("Error: invalid input")
else:
    sum_value = n1 + n2 + n3
    average_value = sum_value / 3   # con / el resultado es float
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    # un número es par si al dividirlo entre 2 el residuo (%) es 0
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)
    print("Sum:", sum_value)
    print("Average:", round(average_value, 2))
    print("Max:", max_value)
    print("Min:", min_value)
    print("All even:", str(all_even).lower())


# ============================================================
# Problem 5: Loan eligibility (income and debt ratio)
# ============================================================
# Descripción: dice si una persona puede recibir un préstamo. Calculo
# debt_ratio = monthly_debt / monthly_income y es elegible (eligible = true)
# si el ingreso es >= 8000, debt_ratio <= 0.4 y credit_score >= 650.
# Entradas: monthly_income (float), monthly_debt (float), credit_score (int)
# Salidas: "Debt ratio:" y "Eligible: true/false"
# Validaciones: monthly_income > 0 (para no dividir entre cero),
# monthly_debt >= 0 y credit_score >= 0
# Casos de prueba:
#   1) Normal: 15000, 3000, 700 -> Debt ratio 0.2, Eligible: true
#   2) Borde: 8000, 3200, 650 -> Debt ratio 0.4, Eligible: true
#   3) Error: 0, 100, 700 -> Error: invalid input (ingreso igual a 0)
print("")
print("--- Problem 5: Loan eligibility ---")
input_ok = True
try:
    monthly_income = float(input("Enter monthly income: "))
    monthly_debt = float(input("Enter monthly debt: "))
    credit_score = int(input("Enter credit score: "))
except ValueError:
    input_ok = False

if input_ok == False:
    print("Error: invalid input")
elif monthly_income <= 0.0 or monthly_debt < 0.0 or credit_score < 0:
    print("Error: invalid input")
else:
    debt_ratio = monthly_debt / monthly_income
    eligible = (monthly_income >= MIN_LOAN_INCOME and debt_ratio <= MAX_DEBT_RATIO
                and credit_score >= MIN_CREDIT_SCORE)
    print("Debt ratio:", round(debt_ratio, 2))
    print("Eligible:", str(eligible).lower())


# ============================================================
# Problem 6: Body Mass Index (BMI) and category flag
# ============================================================
# Descripción: calcula el BMI con la fórmula peso / (estatura * estatura) y
# dice en qué categoría está con tres booleanos: is_underweight (bmi < 18.5),
# is_normal (18.5 <= bmi < 25.0) e is_overweight (bmi >= 25.0).
# Entradas: weight_kg (float) y height_m (float)
# Salidas: "BMI:", "Underweight:", "Normal:", "Overweight:"
# Validaciones: weight_kg > 0 y height_m > 0
# Casos de prueba:
#   1) Normal: 70, 1.75 -> BMI 22.86, Underweight: false, Normal: true,
#      Overweight: false
#   2) Borde: 25, 1.0 -> BMI 25.0, Underweight: false, Normal: false,
#      Overweight: true (justo en el límite de 25.0)
#   3) Error: 70, 0 -> Error: invalid input (la estatura 0 daría división
#      entre cero)
print("")
print("--- Problem 6: BMI calculator ---")
input_ok = True
try:
    weight_kg = float(input("Enter weight in kg: "))
    height_m = float(input("Enter height in meters: "))
except ValueError:
    input_ok = False

if input_ok == False:
    print("Error: invalid input")
elif weight_kg <= 0.0 or height_m <= 0.0:
    print("Error: invalid input")
else:
    bmi = weight_kg / (height_m * height_m)
    is_underweight = bmi < UNDERWEIGHT_LIMIT
    is_normal = bmi >= UNDERWEIGHT_LIMIT and bmi < OVERWEIGHT_LIMIT
    is_overweight = bmi >= OVERWEIGHT_LIMIT
    print("BMI:", round(bmi, 2))
    print("Underweight:", str(is_underweight).lower())
    print("Normal:", str(is_normal).lower())
    print("Overweight:", str(is_overweight).lower())


# ============================================================
# CONCLUSIONES
# ============================================================
# Aprendí que los enteros y los flotantes se usan juntos en cálculos reales,
# por ejemplo en la nómina donde las horas y las tarifas llevan decimales y el
# promedio de enteros da un float. Las comparaciones generan booleanos y con
# ellos el programa puede tomar decisiones usando if. Es muy importante validar
# los rangos y evitar la división entre cero, como en el préstamo y el BMI,
# porque si no el programa se cae. También aprendí a combinar condiciones con
# and, or y not, y a convertir texto a número con int() y float() usando
# try/except para atrapar los errores. Estos mismos patrones se repiten en
# problemas de nómina, descuentos, préstamos y muchos más.

# ============================================================
# REFERENCIAS
# ============================================================
# References:
# 1) Python Software Foundation. Documentación de Python - Tipos integrados:
#    Tipos numéricos (int, float, complex).
#    https://docs.python.org/es/3/library/stdtypes.html
#    https://docs.python.org/es/3/library/stdtypes.html
# 2) Python Software Foundation. Tutorial de Python - Una introducción
#    informal a Python (números). https://docs.python.org/es/3/tutorial/introduction.html
# 3) van Rossum, G., Warsaw, B. y Coghlan, A. PEP 8 - Style Guide for Python
#    Code. https://peps.python.org/pep-0008/