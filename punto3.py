'''Construir un programa para ir de compras en un supermercado que permita la construcción del siguiente MENU: 

1. Digitar 1 para recibir {código, nombre, precio} de un producto (+0.4) 
2. Digitar 2 para mostrar todos los productos registrados (+0.4) 
3. Digitar 3 para permitir buscar por código un producto y editar el precio de este (+0.4) 
4. Digitar 4 para permitir buscar por código un producto y eliminar el producto (+0.4) 
5. Digitar 0 para SALIR 

Finalmente, versione y comparta el repositorio según las indicaciones dadas+(1.4) ''' 

print("Menu")
print("Digitar 1 para recibir {código, nombre, precio} de un producto")
print("Digitar 2 para mostrar todos los productos registrados")
print("3. Salir")
opcion=100

#datos empanadas
#sabor
#ingredientes (x3)
#precio fabricacion
#precio venta
productos=[]

while(opcion !=0):
    opcion=int(input("Digite una opcion  (▀̿̿Ĺ̯̿▀̿ ̿): "))
    if(opcion==1):
        producto={}
        producto['codigo']=int(input("Digite el codigo del producto: "))
        producto['nombre']=input("Digite el nombre del producto: ")
        producto['precio']=input("Digite el precio del producto: ")

        productos.append(producto)
        opcion=opcion+1
        print("se agrego producto")
    elif(opcion==2):
        print(f"Asi quedaron tus productos: {productos}")
    elif(opcion==3):
        codigo=int(input("Digite un codigo de producto a buscar: "))
        for validar in productos:
            if(validar['codigo']==codigo):
                validar['precio']=input("ingrese el precio que desea reemplazar: ")
                print(productos['codigo'])
            else:
                print("Dont exist")
    else:
        print("Digite los numeros del menu (-_-;)")
else:
    print("termine")
