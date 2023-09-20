import random
def chistemalo1 ():
    print ("¿Qué le dijo Batman a Robin antes de subir al coche? Robin, sube al coche")
chistemalo1()


#########


def bienvenida ():
    print("hola mundo")
bienvenida()


##########


def cancion ():
    print(" 2 y 2 son 4, 4 y dos son 6, 6 y 2 son 8 y 8 16!!!")
cancion()


########


def presentacion():
    nombre=""
    nombre = input("hola como estas, como te llamas? ")
    print (" que tengas un lindo dia " + nombre)
presentacion()


########


def dado ():
    print("lanza un dado!! ")
    dado = input("presione enter para lanzar! ")
    dado = random.randint(1,6)
    print (dado)
dado()
