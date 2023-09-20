#funciones
import random
from fractions import Fraction
from math import sqrt

def esNumero(a):
    try:
        float(a)
        return True
    except ValueError:
        return False


def rectaParalela(a,b):
    cont = 0
    num_Independientes = []
    while cont < 3:
        num_random = random.randint(-20,20)
        if num_random != num_Independientes and num_random != b:
           num_Independientes.append(num_random)
           cont +=1     
    for i in num_Independientes:
        print('y = ' + str(a)+'x + ' + str(i))
        

def rectaPerpendicular (a,b):
    cont = 0 
    num_CoeficienteP= []
    
    while cont < 3: 
        num_random = random.randint(-20,20)
        if num_random != num_CoeficienteP and num_random != a and num_random != 0 :
            num_CoeficienteP.append(num_random)
            cont += 1
        
    for i in num_CoeficienteP:
        pendiente = Fraction(i,random.randint(-20,20))
        print('Pendiento original : y = ' + str(pendiente) + ' X + ' + str(b))
        cambiando_pendiente = -1 / pendiente
        print('Cambiando la pendiente: y = ' + str(cambiando_pendiente) + ' X + ' + str(b) )



def recta(a,b):
    # y = mx + b
    # 0 = mx + b
    # x = -b/m
    
    if a > 0:
        pendiente = 'Creciente'
    else:
        pendiente = 'Decreciente'

    raiz = (a * -1 ) / b
    print('Corte en X = ' + str(raiz))
    print('Corte en Y = ' + str(a))
    print('Pendiente = ' + str(pendiente))


def parabola(a,b,c):
    
    if (b*b - 4*a*c) < 0:
        print("La parábola no tiene soluciones reales.")
    elif (b*b - 4*a*c) == 0:
        x = -b / (2*a)
        print("La parábola toca el eje x en un solo punto: " + str(x)) #Como el discriminante es 0 se reduce la expresion para calcular la raiz
    else:
        x1 = (-b+sqrt(b*b-4*a*c))/(2*a)  # Fórmula de Bhaskara parte positiva
        x2 = (-b-sqrt(b*b-4*a*c))/(2*a)  # Fórmula de Bhaskara parte negativa
        print('Las soluciones de la ecuación son: \n x1= ' + "{0:.2f}".format(x1), ' \n x2= ' + "{0:.2f}".format(x2))
        
    if a>0:
        print ("La parabola es concava hacia arriba")
        print(f"El intervalo de decrecimiento del infinito hacia {-b/(2*a)},y crecimiento desde {-b/(2*a)} al Infinito ")
    elif a<0:
            print ("La parabola en concava hacia abajo")
            print(f"El intervalo de crecimiento desde el infinito hasta {(-b/2*a)}, y decrecimiento desde {(-b/2*a)} al Infinito")      
    else:
        print("Si a es igual a 0 la funcion no es cuadratica")            
        print("El corte con el eje y es: ",c )
    