def suma(a,b=5):
    resultado = 0
    resultado = a + b
    print(resultado)

suma(10)


############


def resta(a,b=14):
    resultado = 0
    resultado = a - b
    print(resultado)
resta(13)


#############


def semana(dia = "lunes"):
    lunes = "10°"
    martes = "18°"
    miercoles = "28°"
    jueves = "52°, ayudaaa!!!"
    viernes = "5°"
    sabado = "6°"
    domingo = "32°"
    if dia == "lunes":
        print ("el lunes haran " + lunes)
    if dia == "martes":
        print ("el martes haran " + martes)
    if dia == "miercoles":
        print ("el miercoles haran " + miercoles)
    if dia == "jueves":
        print ("el jueves haran " + jueves)
    if dia == "viernes":
        print ("el viernes haran " + viernes)
    if dia == "sabado":
        print ("el sabado haran " + sabado)
    if dia == "domingo":
        print ("el domingo haran " + domingo)
semana()


#######


def eleccionGenero( genero = "indefinido"):
    print ("su genero es: " + genero)

eleccionGenero(input("Ingrese su genero: "))


########


def preferenciaColor(color = "rojo"):
    rojo="a mi tambien me gusta "
    
    if color=="rojo":
        print (rojo)
    else:
        print("es un lindo color ")
preferenciaColor(input("que color te gusta? "))