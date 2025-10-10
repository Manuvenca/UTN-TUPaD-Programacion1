#Ejercicio N°1
def Hola():
    print("Hola Mundo!")
#Programa principal 
Hola()


#Ejercio N°2
def saludar_usuario(nombre):
    print(f"Hola {nombre}")
#programa principla 

nombre =input("Ingrese un nombre por favor:")
saludar_usuario(nombre)

#Ejercicio N°3  
def informacion_personal(nombre, apellido,edad,residencia):
    print(f"Usted es {nombre} {apellido} y tiene {edad} años recidente de  {residencia}")
#Programa principal
nombre=input("Ingrese su nombre por favor: ")
apellido= input("Ingrese Su apellido por favor: ")
edad=input("Ingrese su edad: ")
residencia= input("Ingrese su Recidencia: ")
informacion_personal(nombre, apellido,edad,residencia)

#Ejercicio N°4
import math
def calcular_area_circulo(radio):
    area =radio*(math.pi**2)
    return print(f"El area del circulo es: {area}")

def calcular_perimetro_circulo(radio):
    perimetro=2*math.pi*radio
    return print(f"El perimetro del cirulo es : {perimetro}")
#Programa principal 
radio = int(input("Ingrese el radio del cirulo que desee saber su perimetro y su area "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

#Ejercicio N°5
def segundos_horas(segundos):
    horas=segundos/60
    return print(f"El equivalente de {segundos} a horas es {horas} ")
#Programa principal 
segundos = int(input("Ingrese la cantidad de segundos que desea saber su equivalente en horas "))
segundos_horas(segundos)

#Ejercio N6
def tabla_multiplcar(numero):
    for i in range(1,11):
        print(f"{i} x {numero}= {i*numero}")
        
#Programa principal 
numero = int(input("Ingrese un numero: "))
tabla_multiplcar(numero)

#Ejercio N°7 
def operaciones_basicas(a,b):
    suma= a+b
    resta= a-b
    multiplicacion=a*b
    division=a/b 
    return (suma,resta,multiplicacion,division)
#Programa principal
a=int(input("Ingrese el primer numero : "))
b=int(input("Ingrese el segundo numero : "))
resultado= operaciones_basicas(a,b)
print(f"La suma es {resultado[0]}")
print(f"La resta es {resultado[1]}")
print(f"La multiplicacion es {resultado[2]}")
print(f"La division es {resultado[3]}")
print(type(resultado))

#Ejercio N°8
def calcular_imc(peso,altura):
    imc=peso/(altura**2)
    return [imc]
#Programa principal
peso= float(input("Ingrese su peso  por favor en kg : "))
altura=float(input("Ingrese su altura en metros por favor: "))

indice =calcular_imc(peso,altura)
print(f"El IMC es: {indice[0]:.2f}")

#Ejercicio N°9
def celsius_a_fahrenheit(celsius):
    Fah=(1.8*celsius)+32
    return Fah
#Programa principal
celsius= float(input("Ingrese la Temperatura en Celsius que deseas saber en Fahrenheit: "))
Fah= celsius_a_fahrenheit(celsius)
print(f"La Temperatura en Fahrenheit es: {Fah}")

#Ejercicio N°10
def calcular_promedio(a, b, c):
    sumatoria= a+b+c
    promedio=sumatoria/3
    return promedio
#Programa principal
a= float(input("Ingrese la primer nota: "))
b= float(input("ingrese la segunda nota: "))
c=float(input("Ingrese la tercer nota: "))

total=calcular_promedio(a,b,c,)
print(f"El promedio total es de : {total}")