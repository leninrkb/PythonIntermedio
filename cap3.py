# generadores

# iterable
# es ub ojeto que implementa __iter__ o __getitem__ 
# y proporciona un iterador

# iterador
# cualquier objeto en python que tenga los metodos next o __next__

# iteracion
# proceso en el que vamos recorriendo cada elemento de un iterable


# generador
# es un iterador que permite recorrerlo una unica vez, dado que no
# almacenan los valores en memoria si no que los generan al vuelo

def mi_generador():
    for i in range(10):
        yield i

for i in mi_generador():
    print(i)

def fibonacci(n):
    a = 0
    b = c = 1
    for _ in range(n):
        yield a
        a = b
        b = c
        c = a + b

for i in fibonacci(10):
    # print(i)
    pass

generado = fibonacci(10)
print(generado)
print(next(generado))
print(next(generado))
print(next(generado))

cadena = "Sekai"
cadena_iterable = iter(cadena)
print(cadena_iterable)
print(next(cadena_iterable))
