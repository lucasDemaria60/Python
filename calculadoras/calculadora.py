"""crear en un nuevo archivo .py todas las funciones pertinentes al funcionamiento de una calculadora. Entre ellas puedo mencionarles rápidamente : 
sumar
restar
multiplicar
dividir
potencia
radicación"""

"""_________________________________________________"""

def suma (num1 , num2):
    
    suma= num1 + num2
    print ("El resultado de " + str(num1) + " + " + str(num2) + " = " + str(suma))
    
    suma(num1 = int(input("Ingrese se primer numero:  ")) , num2 = int(input("Ingrese su segundo numero:  ")))

"""_________________________________________________"""

def resta (num1 , num2):
    resta = num1 - num2
    print ("El resultado de " + str(num1) + " - " + str(num2) + " = "+ str(resta))

    resta(num1 = int(input("Ingrese se primer numero:  ")) , num2 = int(input("Ingrese su segundo numero:  ")))

"""_________________________________________________"""

def multiplicacion (num1 , num2):
    
    multiplicacion = num1 * num2
    print ("El resultado de " + str(num1) + " * " + str(num2) + " = " + str(multiplicacion))


multiplicacion(num1 = int(input("Ingrese se primer numero:  ")) , num2 = int(input("Ingrese su segundo numero:  ")))

"""_________________________________________________"""

def divicion (num1 , num2):
    
    divicion = num1 / num2
    print ("El resultado de " + str(num1) + " / " + str(num2) + " = " + str(divicion))


divicion(num1 = int(input("Ingrese se primer numero:  ")) , num2 = int(input("Ingrese su segundo numero:  ")))

"""_________________________________________________"""

def potenciacion (num1 , elevacion):
    
    potenciacion = num1 ** elevacion
    print (" El numero: " + str(num1) + " Elevado a: " + str(elevacion) + " Es igual a: " + str(potenciacion))

potenciacion(num1 = int(input(" Ingrese el numero a elevar:  ")) , elevacion = int(input(" Ingrese a que potencia desea elevar su numero: ")))

"""_________________________________________________"""

def raiz (num1 , num2):
    
    raiz = num1 ** (1/num2)
    print ("El resultado de " + str(num1) + "  √  " + str(num2) + " = " + str(raiz))


raiz(num1 = int(input("Ingrese se primer numero:  ")) , num2 = int(input("Ingrese su segundo numero:  ")))

"""_________________________________________________"""