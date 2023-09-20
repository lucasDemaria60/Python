
"""def mostrarProductosBreve():
       #revisar en consigna q muestro aca
"""







def mostrarProductosCompletos():
      # mostrarProductosCompletos()
            for codigo, producto in DicProductos.items():
                  print("Codigo: ", producto["Codigo"])
                  print("Nombre: ", producto["Nombre"])
                  print("Marca: ", producto["Marca"])
                  print("Precio: ", producto["Precio"])
                  print("Stock: ", producto["Stock"])
                  print("Material: ", producto["Material"])



#escribiendo todas las funciones
def validarOpciones():
    if opcion == 1:
            mostrarProductosCompletos()           
   
    if opcion == 2:
            #mostrarProductoBreve()

    if opcion == 3:
            #buscarProductoPorCodigo()  





#while salir :
    #opcion = int(input("Que desea realizar? "))
    #validarOpciones (1 al 5)
   #aca hacer una funcion para validar opcion , si existe la opcion
   #derivar a la opcion correspondiente a su ves con otra funcion
   #validarOpciones