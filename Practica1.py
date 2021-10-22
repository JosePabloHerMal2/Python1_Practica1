
##Ejercicio 1
Base=int(input("Ingrese la base del triangulo "))
i=0
for i in range(Base+1):
    print("*"*i)


#Ejercicio 2

num=int(input("Ingrese un entero positivo "))
if num <0:
    print("Los números negativos no son permitidos")
else:
    for i in range(0,num+1):
        print(num-i,end=",")


#Ejercicio 3
#Muestre si es un número primo o no

valor=int(input("Ingrese valor a comprobar "))
if valor<2:
        print("El valor debe ser mayor que 1")
if valor==2:
        print("Es número primo")
else:
    for n in range(2,valor):
        if valor%n==0:
            print("No es un número primo")
            break
        else:
            print("Es primo")
            break
        
