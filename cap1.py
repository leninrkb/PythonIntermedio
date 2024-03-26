# uso de *args y **kwargs

# uso de *args
# permiten tomar un numero variable de argumentos en una funcion

def padre_hijos(padre, *hijos):
    print(f"padre: {padre}")
    for hijo in hijos:
        print(f"{hijo} es hijo de {padre}")

padre_hijos("lenin","Johan","Wolfy","Sebas")

# **kwargs adicional a *args, permite pasar argumentos asociados con una llave

def distros_linux(**distros):
    for clave, contenido in distros.items():
        print("{} esta basado en {}".format(contenido, clave))

distros_linux(ubuntu="pop_os", arch_linux="manjaro")

# Usando *args y **kwargs para llamar a una función

def test_args_kwargs(arg1, arg2, arg3):
    print(f"arg 1 : {arg1}")
    print(f"arg 2 : {arg2}")
    print(f"arg 3 : {arg3}")


mis_args = ("hola","que","pasa")
test_args_kwargs(*mis_args)

mis_kwargs = {"arg1":"heeeyyy", "arg2":"quee?", "arg3":"flan"}
test_args_kwargs(**mis_kwargs)

# monkey path con *args

import os 

def get_info(*args):
    print("aqui su info")

os.mkdir = get_info
os.mkdir()