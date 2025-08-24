#Trabajo Practico condicionales
Ejercicio N1
edad=int(input("Ingrese su edad: "))
if edad >= 18:
    print("Usted es mayo de Edad")

#Ejercicio N2
Nota=int(input("Ingrese su nota por favor: "))
if Nota<=6 :
    print("Desaprobó")
else:
    print("Aprobado")

#Ejercicio N3
numero=int(input("Ingrese un numero por favor: "))
if numero%2 ==0 :
    print("El numero es par")
else:
    print("El numero es impar")
 
#Ejercicio N4
edad=int(input("Ingrese su edad: ")) 
if edad< 12:
    print("Niño/a")
elif edad>=12 and edad <18:
    print("Adolecente")
elif edad>=18 and edad <=30 :
    print("Adulto joven")
else:
    print("Adulto")

#Ejercicio N5
Contraseña=int(len(input("Ingrese contraseña de 8 a 14 digitos")))
if Contraseña>=8 and Contraseña <=14:
    print("Contraseña correcta")
else:
    print("Ingrese una contrasñea de 8 a 14 digitos")

#Ejercicio N6
import random
from statistics import mode,median,mean
numero_aleatorios={random.randint(1,100)for i in range(50)}
print(numero_aleatorios)
valor_mean=mean(numero_aleatorios)
valor_median=median(numero_aleatorios)
valor_mode=mode(numero_aleatorios)
print(valor_mean)
print(valor_median)
print(valor_mode)
if (valor_mean> valor_median >valor_mode):
    print("Sesgo Positivo")
elif (valor_mean<valor_median<valor_mode):
    print("Sesgo Negativo")
elif(valor_mode==valor_mean ==valor_median):
    print("Sin sesgo")

#Ejercicio N7
Frase=input("Ingrese una frase o palabra: ")

if Frase[-1].lower() in "aeiou":
    print(Frase, "!")
else:
    print(Frase)

#Ejercicio N8
nombre=input("Ingrese su nombre por favor ")
print(nombre)
opcion=int(input("""Ingrese la opcion que desea:
                 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
                 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
                 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro
                 Opcion: """))
print(opcion)
if opcion == 1 :
    nombreMay=nombre.upper()
    print(nombreMay)
elif opcion ==2:
    nombreMin=nombre.lower()
    print(nombreMin)
elif opcion== 3:
    nombreNN=nombre.title()
    print(nombreNN)

#Ejercicio N9
magnitud=int(input("Ingrese por favor la magnitud segun la escala de (0 a 10) :"))
print(f"La magnitud que elegida es",(magnitud))
if magnitud<3:
    print("Muy leve imperceptible")
elif magnitud>=3 and magnitud<4 :
    print("Leve ligeramente perceptible")
elif magnitud>=4 and magnitud<5:
    print("Moderado sentido por personas, perogeneralmente no causa daños")
elif magnitud>=5 and magnitud<6:
    print("Fuerte puede causar daños en estructuras débiles")
elif magnitud>=6 and magnitud< 7:
    print("Muy Fuerte puede causar daños significativos")
elif magnitud>=7 and magnitud<=10 :
    print("Extremo puede causar graves daños a gran escala")
elif magnitud>0 or magnitud > 10:
    print("Numero fuera de  Escala")

#Ejercicio N10
hemisferio=input("Ingrese en que hemisferio se encuentra norte (N) o sur (S)")
if hemisferio.lower() =="n":
    hemisferio_norte= hemisferio
if hemisferio.lower() == "s":
    hemisferio_Sur= hemisferio
dia=int(input("Ingrese un dia "))
if dia>31 :
    print("El Dia ingresado debe ser entre 1 y 31 ")
mes=int(input("Ingrese el mes :"))
if mes<0 and mes>12:
    print("Ingrese un mes del 1 al 12")
if (dia>=21 and dia<31 and mes==12) or (mes==1) or (mes ==2) or (mes==3 and dia<=20):
        if hemisferio.lower() =="n":
            hemisferio_norte= hemisferio
            print("Usted esta en verano")
        if hemisferio.lower() == "s":
            hemisferio_Sur= hemisferio
            print("Usted esta en invierno")  
elif (dia >=21 and dia<31 and mes==3) or(mes==4)or (mes==5) or (mes==6 and dia<=20 ):
        if hemisferio.lower() =="n":
            hemisferio_norte= hemisferio
            print("Usted esta en verano")
        if hemisferio.lower() == "s":
            hemisferio_Sur= hemisferio
            print("Usted esta en invierno") 
elif (dia >=21 and dia<31 and mes==6) or(mes==7)or (mes==8) or (mes==9 and dia<=20 ):
        if hemisferio.lower() =="n":
            hemisferio_norte= hemisferio
            print("Usted esta en verano")
        if hemisferio.lower() == "s":
            hemisferio_Sur= hemisferio
            print("Usted esta en invierno") 
elif (dia >=21 and dia<31 and mes==9) or(mes==10)or (mes==11) or (mes==12 and dia<=20 ):
        if hemisferio.lower() =="n":
            hemisferio_norte= hemisferio
            print("Usted esta en verano")
        if hemisferio.lower() == "s":
            hemisferio_Sur= hemisferio
            print("Usted esta en invierno") 