def suma(a,b):
    return a + b
sum = suma(10,9) #Resultado: 19
print(sum)


def imprimir (cad1, cad2):
    print(cad1, cad2)
imprimir('Me gusta', 'tu hermana')

# Funciones anidadas
def funcion1(a):
    print(a)
    b = 100
    def funcion2(b):
        print(b)
    funcion2(b)
funcion1('Python')

# Recursividad
def factorial(x):
    if x > 1:
        return x*factorial(x-1)
    else:
        return 1

factorial(5)