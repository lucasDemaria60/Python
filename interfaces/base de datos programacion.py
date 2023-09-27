import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

conexion = mysql.connector.connect(host="localhost", user="root", password="", database="ESCUELA")

def cargar_datos():
    tree.delete(*tree.get_children())  
    cursor = conexion.cursor()
    cursor.execute("select alumnos.nombre, alumnos.apellido, alumnos.dni, Carrera.nombre, estado_alumno.nombre from alumnos join carrera on alumnos.codcarrera = carrera.codcarrera join estado_alumno on estado_alumno.cod_estado_alumno = alumnos.cod_estado_alumno where alumnos.cod_estado_alumno !=2")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)


def modificar_datos():
    dicc = tree.item(tree.selection())
    cambiar = dicc ['values'][2]
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    dni = dni_entry.get()
    nombre_carrera = carrera_combobox.get()
    estado_alumno = 1
    
    if nombre and apellido and dni and nombre_carrera:
        if(( len(dni) > 6 ) and ( len(dni) < 9)) and dni.isnumeric():
            
            carreras = cargar_carreras()
            carrera_id = None
            for carrera in carreras:
                if carrera[1] == nombre_carrera:
                    carrera_id = carrera[0]
                    break

            cursor = conexion.cursor()

            cursor.execute("""update alumnos set
                               nombre = %s,
                               apellido = %s,
                               dni = %s,
                               id_carrera = %s,
                               id_estado_alumno = %s
                               where dni = %s""", (nombre, apellido, dni, carrera_id, estado_alumno, cambiar))
            conexion.commit()
            cargar_datos()  
            nombre_entry.delete(0, tk.END)
            apellido_entry.delete(0, tk.END)
            dni_entry.delete(0, tk.END)
            carrera_combobox.set("")  
        else:
            mostrar_alerta("DNI no valido")
    else:
        mostrar_alerta("Los campos son obligatorios. Debe completarlos.")

    
    estado_alumno = 1  
    cursor = conexion.cursor()
    
    conexion.commit()
    cargar_datos()  
    nombre_entry.delete(0, tk.END)
    apellido_entry.delete(0, tk.END)
    dni_entry.delete(0, tk.END)
    carrera_combobox.set("")  
def cargar_carreras():
    cursor = conexion.cursor()
    cursor.execute("SELECT codCARRERA, NOMBRE FROM Carrera ORDER BY NOMBRE")
    carreras = cursor.fetchall()
    carrera_combobox['values'] = [row[1] for row in carreras]
    return carreras  
def mostrar_alerta(mensaje):
    messagebox.showwarning("Alerta", mensaje)

def guardar_alumno():
    nombre = nombre_entry.get().upper()
    apellido = apellido_entry.get().upper()
    dni = dni_entry.get()
    if(( len(dni) > 6 ) and ( len(dni) < 9)) and dni.isnumeric():
        carrera_nombre = carrera_combobox.get()
        estado_alumno = 1 

        if nombre and apellido and dni and carrera_nombre:
           
            carreras = cargar_carreras()
            carrera_id = None
            for carrera in carreras:
                if carrera[1] == carrera_nombre:
                    carrera_id = carrera[0]
                    break

            cursor = conexion.cursor()
            cursor.execute("INSERT INTO Alumnos (NOMBRE, APELLIDO, DNI, codCARRERA, cod_ESTADO_ALUMNO) VALUES (%s, %s, %s, %s, %s)", (nombre, apellido, dni, carrera_id, estado_alumno))
            conexion.commit()
            cargar_datos()  
            nombre_entry.delete(0, tk.END)
            apellido_entry.delete(0, tk.END)
            dni_entry.delete(0, tk.END)
            carrera_combobox.set("")  
        else:
            mostrar_alerta("Los campos son obligatorios. Debe completarlos.")
    else:
        mostrar_alerta("DNI Incorrecto")

"""
Añadir a la función de cargar_datos  el WHERE para que liste sólo los alumnos que están "REGULARES" es decir tengan id_estado_alumno = 1, para que no nos liste a los alumnos que están libres.
"""
root = tk.Tk()
root.title("Consulta de Alumnos")

formulario_frame = tk.Frame(root, bd=2, relief=tk.SOLID)
formulario_frame.pack(padx=10, pady=10)

titulo_label = tk.Label(formulario_frame, text="Formulario Inscripción", font=("Helvetica", 14))
titulo_label.grid(row=0, column=0, columnspan=2, pady=10)

nombre_label = tk.Label(formulario_frame, text="Nombre:")
nombre_label.grid(row=1, column=0)
nombre_entry = tk.Entry(formulario_frame)
nombre_entry.grid(row=1, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")

apellido_label = tk.Label(formulario_frame, text="Apellido:")
apellido_label.grid(row=2, column=0)
apellido_entry = tk.Entry(formulario_frame)
apellido_entry.grid(row=2, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")

dni_label = tk.Label(formulario_frame, text="DNI:")
dni_label.grid(row=3, column=0)
dni_entry = tk.Entry(formulario_frame)
dni_entry.grid(row=3, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")

carrera_label = tk.Label(formulario_frame, text="Carrera:")
carrera_label.grid(row=4, column=0)
carrera_combobox = ttk.Combobox(formulario_frame,  state="readonly")
carrera_combobox.grid(row=4, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")

carreras = cargar_carreras()

guardar_button = tk.Button(formulario_frame, text="Guardar", command=guardar_alumno)
guardar_button.grid(row=5, columnspan=2, pady=10, sticky="ew")

tree = ttk.Treeview(root, columns=("Nombre", "Apellido","DNI", "Carrera", "Estado del alumno"))
tree.heading("#1", text="Nombre")
tree.heading("#2", text="Apellido")
tree.heading("#3", text="DNI")
tree.heading("#4", text="Carrera")
tree.heading("#5", text="Estado Alumno")
tree.column("#0", width=0, stretch=tk.NO)  
tree.pack(padx=10, pady=10)

cargar_button = tk.Button(root, text="Cargar Datos", command=cargar_datos)
cargar_button.pack(pady=5)


root.mainloop()


conexion.close()