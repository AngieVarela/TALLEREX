'''1.Construir un programa que permita ingresar N (cantidad digitada por
el usuario) números enteros y cuente cuantos múltiplos de 2 y de 3
fueron ingresados (+1)'''

print("multipos")
#cantidad numeros ingresados
cni=int(input("Dijita cuantos numeros deseas ingresar: "))
aux=0
numeros23=[]
numeros2=[]
numeros3=[]
while(aux<cni):
    numero=int(input(f'ingrse el numero {aux}:'))
    if(numero<0):
        print("numero negativo")
        aux=cni
    else:
        aux1=numero%2
        aux2=numero%3
        if(aux1==0 and aux2==0):
            #print("multiplo de 2 y 3")
            numeros23.append(numero)
            numeros2.append(numero)
            numeros3.append(numero)
        elif(aux1==0):
            #print("multiplo de 2 ")
            numeros2.append(numero)
        elif(aux2==0):
            #print("multiplo de 3 ")
            numeros3.append(numero)
        else:
            print("numero no es multiplo ni de 2 ni de 3")
        aux=aux+1   
else:
    print("Fin Ciclo")

print(f'cantidad de numeros multipos de 2 y 3 son {len(numeros23)} numeros')
print(f'cantidad de numeros multipos de 2 {len(numeros2)} numeros')
print(f'cantidad de numeros multipos de 3 {len(numeros3)} numeros')


