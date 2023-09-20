from tkinter import *
import random

# Primer Ejercicio:
"""
root = Tk()
root.title("ContCreciente")

con = 1

display = Entry(root, font=('ITALIC', 20), justify='right')
display.grid(row=2, column=3, padx=10, pady=10, ipadx=8, ipady=8)
display.insert(0, 1)
display.config(state="readonly")


def contador():
    global con
    con+= 1
    display.config(state="normal")
    display.delete(0, END)
    display.insert(0, con)
    display.config(state="readonly")
    


#Boton
Button(root, text="+", borderwidth=5, font=('italic',25 ), command=contador).grid(row=2, column=2, sticky=W+E)
"""

# Segundo Ejercicio:
"""
root =Tk()
root.title("ContDecreciente")

con = 88

display = Entry(root, font=('ITALIC', 20), justify='right')
display.grid(row=2, column=3, padx=10, pady=10, ipadx=8, ipady=8)
display.insert(0, 88)
display.config(state="readonly")


def contador():
    global con
    con-= 1
    display.config(state="normal")
    display.delete(0, END)
    display.insert(0, con)
    display.config(state="readonly")


#Boton
Button(root, text="-", borderwidth=5, font=('italic',25 ), command=contador).grid(row=2, column=2)
"""
# Tercer Ejercicio
"""
root =Tk()
root.title("Factorial")

num = 1
num2 = 1

#Ventanas

display1 = Entry(root, font=('ITALIC', 20), justify='right')
display1.grid(row=1, column=2, padx=10, pady=10, ipadx=8, ipady=8)
display1.insert(0, num)
display1.config(state="readonly")
#::::::::::
display2 = Entry(root, font=('ITALIC', 20), justify='right')
display2.grid(row=1, column=4, padx=10, pady=10, ipadx=8, ipady=8)
display2.insert(0, num2)
display2.config(state="readonly")
#Textos?
hola = Label(root, text="n",font=('ITALIC', 15)).grid(row=1, column=1, padx=10, pady=10, ipadx=8, ipady=8)
#:::::::::
hola2 = Label(root, text="Factorial (n)",font=('ITALIC', 15)).grid(row=1, column=3, padx=5, pady=5, ipadx=8, ipady=8)

#Funciones

def arriba():
    global num
    global num2      
    display1.config(state="normal")
    display1.delete(0, END)
    num += 1
    display1.insert(0, num)
    display1.config(state="readonly")
    display2.config(state="normal")
    display2.delete(0, END)
    num2 = num2 * num
    display2.insert(0, num2)
    display2.config(state="readonly")

def abajo():
    global num
    global num2      
    display2.config(state = "normal")
    display2.delete(0, END)
    num2 = num2 / num
    num2 = int(num2)
    display2.insert(0, num2)
    display2.config(state = "readonly")
    display1.config(state = "normal")
    display1.delete(0, END)
    if num != 1:
        num -= 1
    display1.insert(0, num)
    display1.config(state = "readonly")


# Botones
Button(root, text="Arriba", borderwidth=5, font=('italic',25 ), command=arriba).grid(row=2, column=2)
Button(root, text="Abajo", borderwidth=5, font=('italic',25 ), command=abajo).grid(row=2, column=3)
"""
# Cuarto Ejercicio 
"""
root = Tk()
root.title("Contador")

con = 0

display = Entry(root, font=('ITALIC', 20), justify='right')
display.grid(row=2, column=3, padx=10, pady=10, ipadx=8, ipady=8)
display.insert(0, 0)
display.config(state="readonly")


def contador():
    global con
    con+= 1
    display.config(state="normal")
    display.delete(0, END)
    display.insert(0, con)
    display.config(state="readonly")
    

def contadorD():
    global con
    con-= 1
    display.config(state="normal")
    display.delete(0, END)
    display.insert(0, con)
    display.config(state="readonly")


def limpiar():
    global con
    con = 0
    display.config(state="normal")
    display.delete(0, END)
    display.insert(0, con)
    display.config(state="readonly")


#Boton
Button(root, text="+", borderwidth=5, font=('italic',25 ), command=contador).grid(row=2, column=2, sticky=W+E)
Button(root, text="-", borderwidth=5, font=('italic',25 ), command=contadorD).grid(row=3, column=2, sticky=W+E)
Button(root, text="Reset", borderwidth=5, font=('italic',25 ), command=lambda:limpiar()).grid(row=3, column=3, sticky=W+E)
"""
# Quinto Ejercicio
"""
root = Tk()
root.title("Calculadora")

num1 = 0
num2 = 0
num3 = 0

a = Label(root, text="Primer Numero",font=('ITALIC', 15)).grid(row=1, column=1, padx=5, pady=5, ipadx=8, ipady=8)
b = Label(root, text="Segundo Numero",font=('ITALIC', 15)).grid(row=2, column=1, padx=5, pady=5, ipadx=8, ipady=8)
c = Label(root, text="Resultado",font=('ITALIC', 15)).grid(row=3, column=1, padx=5, pady=5, ipadx=8, ipady=8)

display1 = Entry(root, font=('ITALIC', 20), justify='right')
display1.grid(row=1, column=2, padx=10, pady=10, ipadx=8, ipady=8)
display1.config(state="normal")
display2 = Entry(root, font=('ITALIC', 20), justify='right')
display2.grid(row=2, column=2, padx=10, pady=10, ipadx=8, ipady=8)
display2.config(state="normal")
display3 = Entry(root, font=('ITALIC', 20), justify='right')
display3.grid(row=3, column=2, padx=10, pady=10, ipadx=8, ipady=8)
display3.config(state="readonly")


def suma():
    global num1
    global num2
    global num3
    num1 = display1.get()
    num2 = display2.get()
    num1 = int(num1)
    num2 = int(num2)
    display3.config(state="normal")
    num3 = num1 + num2
    display3.delete(0, END)
    display3.insert(0, num3)
    display3.config(state="readonly")
    
def multiplicacion():
    global num1
    global num2
    global num3
    num1 = display1.get()
    num2 = display2.get()
    num1 = int(num1)
    num2 = int(num2)
    display3.config(state="normal")
    num3 = num1 * num2
    display3.delete(0, END)
    display3.insert(0, num3)
    display3.config(state="readonly")

def resta():
    global num1
    global num2
    global num3
    num1 = display1.get()
    num2 = display2.get()
    num1 = int(num1)
    num2 = int(num2)
    display3.config(state="normal")
    num3 = num1 - num2
    display3.delete(0, END)
    display3.insert(0, num3)
    display3.config(state="readonly")
    
def divicion():
    global num1
    global num2
    global num3
    num1 = display1.get()
    num2 = display2.get()
    num1 = int(num1)
    num2 = int(num2)
    display3.config(state="normal")
    num3 = num1 / num2
    display3.delete(0, END)
    display3.insert(0, num3)
    display3.config(state="readonly")

def porcentaje():
    global num1
    global num2
    global num3
    num1 = display1.get()
    num2 = display2.get()
    num1 = int(num1)
    num2 = int(num2)
    display3.config(state="normal")
    num3 = num1 * num2
    num3 = num3 / 100

    display3.delete(0, END)
    display3.insert(0, num3)
    display3.config(state="readonly")
    
def limpiar():
    display1.delete(0, END)
    display2.delete(0, END)
    display3.delete(0, END)
    display3.config(state="normal")
    display3.delete(0, END)
    display3.config(state="readonly")
    
#Botones
Button(root, text="+",borderwidth=5, font=('italic',25 ), command=lambda:suma()).grid(row=4, column=1, sticky=W+E)
Button(root, text="-",borderwidth=5, font=('italic',25 ), command=lambda:resta()).grid(row=4, column=3, sticky=W+E)
Button(root, text="X",borderwidth=5, font=('italic',25 ), command=lambda:multiplicacion()).grid(row=5, column=1, sticky=W+E)
Button(root, text="/",borderwidth=5, font=('italic',25 ), command=lambda:divicion()).grid(row=5, column=2, sticky=W+E)
Button(root, text="%", borderwidth=5, font=('italic',25 ), command=lambda:porcentaje()).grid(row=6, column=1, sticky=W+E)
Button(root, text="Clear",borderwidth=5, fg='red' , font=('arial', 25, "bold" ),command=lambda:limpiar()).grid(row=1, column=3, sticky=W+E) #BorrAR todo
"""
# Sexto Ejercico
"""
root = Tk()
root.title("Peliculas")
pelicula = ""
a = Label(root, text="Ingrese la Pelicula:",font=('ITALIC', 20)).grid(row=1, column=1, padx=5, pady=5, ipadx=8, ipady=8)
b = Label(root, text="Peliculas:",font=('ITALIC', 20)).grid(row=1, column=3, padx=5, pady=5, ipadx=8, ipady=8)

display1 = Entry(root, font=('ITALIC', 20), justify='center')
display1.grid(row=2, column=1, padx=10, pady=10, ipadx=8, ipady=8)
display1.config(state="normal")

display2 = Listbox(root, font=('ITALIC', 20), justify='center')
display2.grid(row=2, column=3, padx=10, pady=10, ipadx=8, ipady=8)

def pelis():
    global pelicula
    pelicula = display1.get()
    display2.insert(END, pelicula)

Button(root, text="Añadir",borderwidth=5, font=('italic',20 ), command=lambda:pelis()).grid(row=2, column=2)
"""
# Septimo Ejercicio
"""
root = Tk()
root.title("Generador de números")

aleatorio = 0
aleatorio2 = 0

a = Label(root, text="Número 1",font=('ITALIC', 20)).grid(row=1, column=1, padx=5, pady=5, ipadx=8, ipady=8)
b = Label(root, text="Número 2",font=('ITALIC', 20)).grid(row=2, column=1, padx=5, pady=5, ipadx=8, ipady=8)
b = Label(root, text="Número Generado",font=('ITALIC', 20)).grid(row=3, column=1, padx=5, pady=5, ipadx=8, ipady=8)

display1 = Spinbox(root, font=('ITALIC', 20), justify='center',from_=0, to=10)
display1.grid(row=1, column=2, padx=10, pady=10, ipadx=8, ipady=8)
display1.config(state="readonly")

display2 = Spinbox(root, font=('ITALIC', 20), justify='center',from_=11, to=30)
display2.grid(row=2, column=2, padx=10, pady=10, ipadx=8, ipady=8)
display2.config(state="readonly")

display3 = Entry(root, font=('ITALIC', 20), justify='center')
display3.grid(row=3, column=2, padx=10, pady=10, ipadx=8, ipady=8)
display3.config(state="readonly")

def generar():
    global aleatorio
    global aleatorio2
    aleatorio = display1.get()
    aleatorio2 = display2.get()
    aleatorio = int(aleatorio)
    aleatorio2 = int(aleatorio2)
    aleatorios=random.randint(aleatorio, aleatorio2)
    display3.config(state="normal")
    display3.delete(0, END)
    display3.insert(END, aleatorios)
    display3.config(state="readonly")

        

Button(root, text="Generar",borderwidth=5, font=('italic',20 ), command=lambda:generar()).grid(row=5, column=2)

"""

# Octavo Ejercicio

root = Tk()
root.title("Calculadora Dos")

num1 = 0
num2 = 0
num3 = 0

a = Label(root, text="Primer Valor",font=('ITALIC', 15, "bold")).grid(row=2, column=1, padx=5, pady=5, ipadx=8, ipady=8)
b = Label(root, text="Segundo Valor",font=('ITALIC', 15, "bold")).grid(row=3, column=1, padx=5, pady=5, ipadx=8, ipady=8)
c = Label(root, text="Resultado",font=('ITALIC', 15, "bold")).grid(row=4, column=1, padx=5, pady=5, ipadx=8, ipady=8)
d = Label(root, text="Operaciones",font=('ITALIC', 15, "bold")).grid(row=1, column=3, padx=5, pady=5, ipadx=8, ipady=8)

display1 = Entry(root, font=('ITALIC', 20), justify='center')
display1.grid(row=2, column=2, padx=10, pady=10, ipadx=8, ipady=8)
display1.config(state="normal")
display2 = Entry(root, font=('ITALIC', 20), justify='center')
display2.grid(row=3, column=2, padx=10, pady=10, ipadx=8, ipady=8)
display2.config(state="normal")
display3 = Entry(root, font=('ITALIC', 20), justify='center')
display3.grid(row=4, column=2, padx=10, pady=10, ipadx=8, ipady=8)
display3.config(state="readonly")
lista = [0]
op = IntVar()
op.set(1)

def suma():
    global num1
    global num2
    global num3
    num1 = display1.get()
    num2 = display2.get()
    num1 = int(num1)
    num2 = int(num2)
    display3.config(state="normal")
    num3 = num1 + num2
    display3.delete(0, END)
    display3.insert(0, num3)
    display3.config(state="readonly")
    
def multiplicacion():
    global num1
    global num2
    global num3
    num1 = display1.get()
    num2 = display2.get()
    num1 = int(num1)
    num2 = int(num2)
    display3.config(state="normal")
    num3 = num1 * num2
    display3.delete(0, END)
    display3.insert(0, num3)
    display3.config(state="readonly")

def resta():
    global num1
    global num2
    global num3
    num1 = display1.get()
    num2 = display2.get()
    num1 = int(num1)
    num2 = int(num2)
    display3.config(state="normal")
    num3 = num1 - num2
    display3.delete(0, END)
    display3.insert(0, num3)
    display3.config(state="readonly")
    
def divicion():
    global num1
    global num2
    global num3
    num1 = display1.get()
    num2 = display2.get()
    num1 = int(num1)
    num2 = int(num2)
    display3.config(state="normal")
    num3 = num1 / num2
    display3.delete(0, END)
    display3.insert(0, num3)
    display3.config(state="readonly")

def calcular():
    global lista
    if lista[0]==1:
        suma()
    if lista[0]==2:
        resta()
    if lista[0]==3:
        multiplicacion()
    if lista[0]==4:
        divicion()

#Botones
Radiobutton(root, text="Sumar",value=1,variable=op,borderwidth=5, font=('Arial',15, "bold" ), command=lambda:[lista.pop(0), lista.append(1)]).grid(row=2, column=3)
Radiobutton(root, text="Restar",borderwidth=5,value=2,variable=op, font=('Arial',15, "bold" ), command=lambda:[lista.pop(0), lista.append(2)]).grid(row=3, column=3)
Radiobutton(root, text="Multiplicar",borderwidth=5,value=3,variable=op, font=('Arial',15, "bold" ), command=lambda:[lista.pop(0), lista.append(3)]).grid(row=4, column=3)
Radiobutton(root, text="Dividir",borderwidth=5,value=4,variable=op, font=('Arial',15, "bold" ), command=lambda:[lista.pop(0), lista.append(4)]).grid(row=5, column=3, sticky=W+E)



Button(root, text="Generar",borderwidth=5, font=('italic',20, "bold" ), command=lambda:calcular()).grid(row=5, column=2)




root.mainloop()
