"""listadetuplas = [("termo", 600, 4, "bigstar"), ("vaso", 300, 8, "bigstar"), ("mate", 1200, 10, "posadas"), ("mate", 100, 20, "posadas"), ("termo", 30000, 2, "apple")]

while (1):
    listaresultado = [ ]
    precio = int(input("ingrese un precio: "))
    marca = (input("ingrese una marca: "))
    for i in range(0, len(listadetuplas)):
        if (listadetuplas[i][1] <= precio) and (listadetuplas [i][3] == marca):
            listaresultado.append(listadetuplas [i])

    print(listaresultado)



meses=("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
num=int(input("ingrese un numero: "))

if (num>=1 or num <13):
    print(meses[num-1])
if (num<1 or num>12):
    print ("error")


numeros=(1,2,1,2,1,2,1,1,2,1,1,2,)
num=int(input("ingrese un numero: "))
if (num == 1 or num == 2):
    print(numeros.count(num))
else:
    print ("error")

"""

"""numeros2 = (12, 43, 12, 45, 2)

mayor = numeros2[0]
menor = numeros2[0]
for i in numeros2:
    if mayor < i:
        mayor = i
    if i < menor:
        menor = i
print ("El mayor es: " + str(mayor))
print ("El menor es: " + str(menor))"""


numeros3=(1,2,3,4,5,6,7,8,9,10)
indice=int(input("ingrese un indice "))
if indice > 9 or indice < 0:
    print("Indice inexistente")
else:
    print ("el valor de su indice es: " + str(numeros3[indice]))