#carrito de compras

print("Bienvenidos a Artesanias Lucas!! \n A continuacion nuestro menu: \n 1-Mostrar productos. \n 2-Detalles del producto. \n 3-Ver carrito. \n 4-Realizar compra. \n 5-Finalizar compra. \n 6-Salir.")
salir = True
opcion = ""
DicProductos = {
    "01" : {
        "Codigo" : 100,
        "Nombre" : "Mate", 
        "Marca": "Pampa",
        "Precio": 6500,
        "Stock": 5,
        "Material": "pvc" },

    "02" : {
        "Codigo" : 200,
        "Nombre" : "Mate",
        "Marca": "Lalo",
        "Precio": 3500,
        "Stock": 6,
        "Material": "pvc y goma" },
     "03" : {
        "Codigo" : 300,
        "Nombre" : "Termo",
        "Marca": "Romania",
        "Precio": 11500,
        "Stock": 5,
        "Material": "Acero" },
     "04" : {
        "Codigo" : 400,
        "Nombre" : "Termo",
        "Marca": "Stanley",
        "Precio": 21000,
        "Stock": 3,
        "Material": "pvc y goma" },
}
primer_producto = DicProductos ["01"]
segundo_producto = DicProductos ["02"]
tercero_producto = DicProductos ["03"]
cuarto_producto = DicProductos ["04"]

DicDetalles = { }

while salir :
    opcion = int(input("Que desea realizar? "))
    if opcion == 1:
        mostrarProductosCompletos(DicProductos)
    if opcion == 2:
          






def mostrarProductosCompletos():
      # mostrarProductosCompletos()
            for codigo, producto in DicProductos.items():
                  print("Codigo: ", producto["Codigo"])
                  print("Nombre: ", producto["Nombre"])
                  print("Marca: ", producto["Marca"])
                  print("Precio: ", producto["Precio"])
                  print("Stock: ", producto["Stock"])
                  print("Material: ", producto["Material"])



def validarOpciones():
    if opcion == 1:
            mostrarProductosCompletos()           
   
    if opcion == 2:
            #mostrarProductoBreve()

    if opcion == 3:
            #buscarProductoPorCodigo()  



"""def mostrarProductosBreve():
       #revisar en consigna q muestro aca
"""



#while salir :
    #opcion = int(input("Que desea realizar? "))
    #validarOpciones (1 al 5)
   #aca hacer una funcion para validar opcion , si existe la opcion
   #derivar a la opcion correspondiente a su ves con otra funcion
   #validarOpciones