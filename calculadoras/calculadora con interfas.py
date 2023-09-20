from tkinter import *

root = Tk()
root.title("Calculadora De Lucas")

i = 0

display = Entry(root, font=('ITALIC', 20), bg='black', fg='white', justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=8, ipady=8)

def obtener_numeros(n):
    global i
    display.insert(i, n)
    i+=1

def operaciones(operacion):
    global i 
    largo = len(operacion)
    display.insert(i, operacion)
    i+=largo

def limpiar():
    display.delete(0, END)

def undo():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        limpiar()
        display.insert(0, display_new_state)
    else: 
        limpiar()
        display.insert(0, "Error")
    
def calculo():
    display_state = display.get()
    try:
        math_expression =  compile(display_state, 'calculadora con interfas.py', 'eval')
        result = eval(math_expression)
        limpiar()
        display.insert(0,result)
    except:
        limpiar()
        display.insert(0,"error")


# Numeros
Button(root, text="1",borderwidth=5, font=('italic',25 ), command=lambda:obtener_numeros(1)).grid(row=5, column=0, sticky=W+E)
Button(root, text="2",borderwidth=5, font=('italic',25 ), command=lambda:obtener_numeros(2)).grid(row=5, column=1, sticky=W+E)
Button(root, text="3",borderwidth=5, font=('italic',25 ), command=lambda:obtener_numeros(3)).grid(row=5, column=2, sticky=W+E)

Button(root, text="4",borderwidth=5, font=('italic',25 ), command=lambda:obtener_numeros(4)).grid(row=4, column=0, sticky=W+E)
Button(root, text="5",borderwidth=5, font=('italic',25 ), command=lambda:obtener_numeros(5)).grid(row=4, column=1, sticky=W+E)
Button(root, text="6",borderwidth=5, font=('italic',25 ),command=lambda:obtener_numeros(6)).grid(row=4, column=2, sticky=W+E)

Button(root, text="7",borderwidth=5, font=('italic',25 ),command=lambda:obtener_numeros(7)).grid(row=3, column=0, sticky=W+E)
Button(root, text="8",borderwidth=5, font=('italic',25 ),command=lambda:obtener_numeros(8)).grid(row=3, column=1, sticky=W+E)
Button(root, text="9",borderwidth=5, font=('italic',25 ),command=lambda:obtener_numeros(9)).grid(row=3, column=2, sticky=W+E)
Button(root, text="0",borderwidth=5,  font=('italic',25 ),command=lambda:obtener_numeros(0)).grid(row=6, column=1, sticky=W+E)


#Especiales?
Button(root, text="🚽",borderwidth=5, fg='red' , font=('arial', 25, "bold" ),command=lambda:limpiar()).grid(row=2, column=0, sticky=W+E) #BorrAR todo
Button(root, text="🧻",borderwidth=5, font=('italic',25 ), command=lambda:undo()).grid(row=2, column=1, sticky=W+E) #Borrar de a un numero


#Calculos
Button(root, text="➕",borderwidth=5, font=('italic',25 ), command=lambda:operaciones("+")).grid(row=5, column=3, sticky=W+E)
Button(root, text="➖",borderwidth=5, font=('italic',25 ), command=lambda:operaciones("-")).grid(row=4, column=3, sticky=W+E)
Button(root, text="❌",borderwidth=5, font=('italic',25 ), command=lambda:operaciones("*")).grid(row=3, column=3, sticky=W+E)
Button(root, text="➗",borderwidth=5, font=('italic',25 ), command=lambda:operaciones("/")).grid(row=2, column=3, sticky=W+E)
Button(root, text="%", borderwidth=5, font=('italic',25 ), command=lambda:operaciones("%")).grid(row=2, column=2, sticky=W+E)
Button(root, text="(",borderwidth=5, font=('italic',25 ), command=lambda:operaciones("(")).grid(row=6, column=0, sticky=W+E)
Button(root, text=")",borderwidth=5, font=('italic',25 ), command=lambda:operaciones(")")).grid(row=6, column=2, sticky=W+E)
Button(root, text="=",borderwidth=5, font=('italic',25 ),command=lambda:calculo()).grid(row=6, column=3, sticky=W+E)

#Me rompian la estetica
"""Button(root, text="exp", command=lambda:operaciones("**")).grid(row=3, column=4, sticky=W+E)
Button(root, text="^2", command=lambda:operaciones("**2")).grid(row=3, column=5, sticky=W+E)"""


root.mainloop()
