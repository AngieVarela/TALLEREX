'''Leer el nombre de 10 frutas {nombre, color, precio} para preparar un salpicón; el programa debe permitir mostrar las 10 frutas ingresadas al mismo tiempo en sentido inverso al ingresado+(1) '''


frutas=[]
observador=1
while(observador <4):
    fruta={}
    fruta ['fruta']= input(f'Ingrese la fruta {observador}: ')
    fruta ['color']= input(f'Ingrese el color de la fruta: ')
    fruta ['precio']= input(f'Ingrese el precio de la fruta: ')
    print(" ")
    
    frutas.append(fruta)
    observador=observador+1
else:
    frutas.reverse()
    print(f'las frutras fueron {frutas}')
