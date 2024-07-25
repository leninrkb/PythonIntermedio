# operadores ternarios, en python mas conocidos como operadores 
# condicionales

nombre = "lenin" == "lenin"
estado = "si es lenin" if nombre else "no es lenin"
print(estado)

# otra forma extrana poco usada
to_live = False
estado = ("lenin wants to die", "lenin wants to live")[to_live]
print(estado)


# en la segunda forma las dos opciones son evaludas
try:
    print((1/0, 10)[True])
except Exception as e:
    print(e)

# a diferencia de la primera
print(1/0 if False else 10)


# abrevacion ternaria
print(not True or True)
print("Hayase" or False)
print(False or "Hayase")
print(None or False)
print(None or "I love Sana Sunomiya")


def saludar(nombre, apodo=None):
    print(f"hola !!! {apodo or nombre}")

saludar("lenin")

saludar("lenin", "turtlebytes")