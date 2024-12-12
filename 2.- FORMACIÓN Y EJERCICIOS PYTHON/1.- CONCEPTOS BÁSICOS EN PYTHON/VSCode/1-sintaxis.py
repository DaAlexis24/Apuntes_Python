# Definición de un variable tipo string
cad = "El valor de (a+b) es..."
print("1.- Definición de una variable: " + cad)

# Múltiples asignaciones
num1, num2, num3 = 4, 3, 2
print("2.- Podemos realizar múltiples asignaciones:")
# OJO: No puedes imprimir un str con un int, debes de equipararlas al mismo tipo de dato
print("Num1 es: " + str(num1))
print("Num2 es: " + str(num2))
print("Num3 es: " + str(num3))

# Operaciones númericas
sum = (num1+num2) * num3
print("3.- La suma de los elementos anteriores es: " + str(sum))

# Booleanos
bool = False
print("4.- Variables booleanas: " + str(bool))

# Estructura IF
imprimir = True
if imprimir:
    print("5.- Estructura IF: " + str(sum))

# Múltiples líneas

# x = 1 + 2 + 3 + \
#     5 + 6+ 7

# x = (1 + 2 + 3
#      4 + 5 + 6)

# def funcion(a,b,c):
#     return a+b+c
# d = funcion(10,
#             20,
#             30)

