#Ejercicio N°1 
print("Hola Mundo!")
a=10
b=3.0
c=a*b
d=a*b

#Ejercicio N°2
nombre=input("Ingrese un nombre: ")
print(f"Hola  {nombre} !")

#Ejercicio N°3
nombre=input("Escriba su nombre: ")
apellido=input("Ahora su apellido: ")
edad=input("Ingrese su edad: ")
residencia=input("Indique su lugar de residencia por favor: ")
print(f"Soy {nombre} {apellido} tengo {edad} años y vivo en {residencia} ")

#Ejercicio N°4
import math
radio=int(input("Por Favor coloque el radio de la circurferencia que desea saber su area y perimetro: "))

area=math.pi*(radio**2)
perimetro=2*math.pi*radio
print(f"El radio ingresao es : {radio}\nEl area es : {area}\nEl perimetro es : {perimetro}")

#Ejercicio N°5
segundos=int(input("Ingrese la cantidad que desee saber en segundos: "))
hora=float(1/3600)
equivalente=(segundos*hora)
print(f"El equivalenten en horas es {equivalente}")

#Ejercicio N°6
numero=input("Ingrese un numero: ")
numero=int(numero)
print(f"""
      {numero}x0 ={numero*0}
      {numero}x1 ={numero*1}
      {numero}x2 ={numero*2}
      {numero}x3 ={numero*3}
      {numero}x4 ={numero*4}
      {numero}x5 ={numero*5}
      {numero}x6 ={numero*6}
      {numero}x7 ={numero*7}
      {numero}x8 ={numero*8}
      {numero}x9 ={numero*9}
      {numero}x10 ={numero*10}
      """)

#Ejercicio N°7
num1=int(input("Ingrese un numero : ") )
num2=int(input("Ingrese un numero : ") )
suma=num1+num2
resta=num1-num2
division=num1/num2
multiplicacion=num1*num2
print(f" La suma es {suma}\n La Resta es {resta}\n La multiplicacion es {multiplicacion}\n La division es {division}")

#Ejercicio N°8
altura=float(input("Ingrese  su altura: "))
peso=float(input("Ingrese su peso: "))
IMC=peso/(altura**2)
print("Su indice de masa corporal es ",IMC)

#Ejercicio N°9
temp=int(input("Ingrese la tempereratura en Celsius "))
Equiv=9/5*temp+32
print(f"El equivalente en farentheit es {Equiv}")

#Ejercicio N°10
num1=int(input("Ingrese un numero: "))
num2=int(input("Ingrese un numero: "))
num3=int(input("Ingrese un numero: "))
promedio=(num1+num2+num3)/3
print("El promedio de los 3 numeros es: ", promedio)