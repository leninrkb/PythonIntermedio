# decoradores
def saludar(nombre="Hayase"):
    return f"hola {nombre}, como estas ?"

print(saludar())

saludo = saludar()
print(saludo)

nuevo_saludo = saludar
print(nuevo_saludo())

# del saludar

print(saludo)
print(saludar())

# funciones dentrp de funciones

def hola():
    def saludar():
        print("saludando")
    def despedir():
        print("despidiendose")
    def terminar():
        print("programa terminado")

    saludar()
    despedir()
    terminar()

hola()

# devolviendo funciones desde funciones

def operacion(op):
    def suma():
        return "estas en suma"
    def resta():
        return "estas en resta"
    return suma if op == "suma" else resta

print(operacion("suma")())

# funciones como argumento
def primero():
    print("primero")

def segundo(myfunc):
    print("segundo")
    myfunc()

segundo(primero)

# decorador
def decorador(myfunc):
    def envoltura():
        print("proceso antes de ejecutar la funcion argumento")
        myfunc()
        print("proceso posterior a la ejecucion de la funcion argumento")
    return envoltura

def funcion_normal():
    print("esta es la funcion normal")

funcion_normal = decorador(funcion_normal)

funcion_normal()
print(funcion_normal.__name__)


@decorador
def otra_funcion_normal():
    print("soy otra funcion normal")

otra_funcion_normal()
print(otra_funcion_normal.__name__)

# nuestro decorador sobrescribe el docstring de nuestra funcion normal
# solucionamos esto con wraps de functools

from functools import wraps
from typing import Any

def nuevo_decorador(myfunc):
    @wraps(myfunc)
    def decorador():
        print("decorando")
        myfunc()
        print("termino decorar")
    return decorador

@nuevo_decorador
def lenin():
    print("soy lenin")

lenin()
print(lenin.__name__)


def decorador2(func):
    @wraps(func)
    def decorador(*args, **kwargs):
        if run:
            return func(*args, **kwargs)
        else:
            print("la funcion no se ejecuta")
    return decorador

@decorador2
def destroy(d):
    print("lenin destroys de universe" if d else "lenin is sleeping")
run = True

destroy(True)
destroy(False)

# decoradores con argumentos

def funcion_que_toma_el_parametro(nombre="archivo.txt"):
    def funcion_que_toma_funcion(func):
        @wraps(func)
        def decorador(*args, **kwargs):
            log = func.__name__ + " ha sido llamado"
            print(log)
            print(f"se creo un log en {nombre}")
            return func(*args, **kwargs)
        return decorador
    return funcion_que_toma_funcion


@funcion_que_toma_el_parametro("mis_logs.txt")
def auth(user, password):
    print(f"user: {user} --> password: {password}")

auth("lenin", "123")

# clases decoradoras
# definimos un decorador a partir de una clase

class logit(object):
    nombre = "mis_logs.txt"
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, *args, **kwargs):
        log = self.func.__name__ + " fue llamada...."
        print(log)
        print(f"se creo un log en {self.nombre}")
        return self.func(*args, **kwargs)
    
logit.nombre = "otros_logs.txt"
@logit
def sumatoria(*args):
    print(sum(args))

sumatoria(1,2,3,4,5,6)


# subclase de logit

class notify_admin(logit):
    def __init__(self,  func) -> None:
        super(notify_admin, self).__init__(func)

    def __call__(self, *args, **kwargs):
        self.send_email()
        return super().__call__(*args, **kwargs)

    def send_email(self):
        print("sending email to admin....")


notify_admin.nombre = "logs_admin.txt"
@notify_admin
def modificar_db():
    print("modificando la base de datos")

modificar_db()