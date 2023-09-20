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
    #opcion = int(input("Que desea realizar? "))
