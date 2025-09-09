#Ejercicio N°1
for cont in range(0,101,1):
    print(cont)

#Ejercicio N°2
numero=int(input("Ingrese un numero: "))
digito=0
if numero==0:
    print("La Cantidad de digitos es \"1\"")
else:
    while numero > 0:
        numero=numero//10
        digito+=1
print("La cantidad de digitos es "+ str(digito))

#Ejercicio N°3
print("Ingrese un numero: ")
a=int(input())
print("Ingrese otro numero: ")
b=int(input())
mayor=0
menor=0
suma=0
comprendidos=0
if a>b:
    mayor=a
    menor=b
elif b>a:
    mayor=b
    menor=a
while mayor>=menor:
    suma=suma+mayor
    comprendidos=mayor
    mayor-=1
    print("Los comprendidos son: ", comprendidos)
print("La suma comprendidos es ",suma)

#Ejercicio N°4
corte=0
print("Ingrese numeros enteros para salir presiones "+"(" + str(corte)+ ")"  )
num=int(input())
contador=0
suma=0
while num != 0 :
    contador+=1
    suma+=num
    #print("Ingrese otro numero y presiones "+"("+str(corte) + ")"+ "para salir "  )
    num=int(input())
print(f"La cantidad de numeros ingresador fue:",contador,"y la suma fue: ", suma)

#Ejercicio N°5
condic="0 y 9"
print("Ingrese un numero entre: ", condic)
import random
aleatorio=random.randint(0,9)
num=int(input())
intentos=1
if num <9 and num >0:
    while num != aleatorio:
        intentos+=1
        print("Ingrese otro numero")
        num=int(input())
else:  
    print("Ingrese numeros dentro del rango")
print("El numero aleatorio es "+ str(aleatorio) + " y los intentos fueron "+str(intentos))

#Ejercicio N°6
for i in range(100,-2,-2):
    print(i)

#Ejercicio N°7
print("Ingrese un numero: ")
num=int(input())
suma=0
for i in range(0,num+1):
    print("los comprendidos son ",i)
    suma+=i
print("Y la suma de todos ellos es: ",suma)

#Ejercicio N°8
condicion=8
positivo=0
negativo=0
par=0
impar=0
cantidad=0
num=0
while cantidad != condicion:
    print("Ingrese un numero: ")
    num=int(input())
    
    if num>0:
        positivo+=1
    elif num<0:
        negativo+=1
    if num % 2==0:
        par+=1
    elif num% 2 !=0:
        impar+=1
    cantidad+=1
print("Los numeros positivos son: ",positivo)  
print("Los numeros negativos son: ",negativo)
print("Los numeros par son: ",par)
print("Los numeros impar son: ",impar)

#Ejercicio N°9
Total=10
cant=0
suma_total=0
conta=0
while cant != Total:
    print("Ingrese un numero: ")
    num=int(input())
    suma_total+=num
    cant+=1
print(f"La suma total es {suma_total} y la media  es {suma_total/Total}")

#Ejercicio N°10
import math
print("Ingrese un numero: ")
num=int(input())
dig=0
inverso=0
while num!=0:
    
    dig=num % 10
    num=(math.trunc(num/10))
    inverso=inverso*10+dig
print("El inverso es: ", inverso)