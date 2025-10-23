#Ejercicio N°1
precio_frutas={'Banana':1200,'Ananá':2500,'Melón':3000,'Uva':1450}
print(precio_frutas)
precio_frutas['Naranja']=1200
precio_frutas['Manzana']=1500
precio_frutas['Pera']=2300
print(precio_frutas)

#Ejercicio N°2
precio_frutas['Banana']=1330
precio_frutas['Manzana']=1700
precio_frutas['Melon']=2800
print(precio_frutas)

#Ejercicio N°3
print(precio_frutas.keys())

#Ejercicio N°4
agenda={}
for i in range(5):
    nombre=input(f"Ingrese el  {i+1} nombre  :")
    cel=input(f"Ingrese su numero de celular de {nombre}: ")
    agenda[nombre]=cel
   
print(agenda) 
busqueda= input("Ingrese el nombre que desea buscar? ")

if busqueda in agenda:
    print(f"El nombre que usted ingreso es {agenda[busqueda]}")
    
else:
    print("El nombre no se encuentra en la agenda!!")
    
#Ejercicio N°5
frase=input("Ingrese una frase ")
palabras=frase.split()
palabras_unicas = set(palabras)
contador= {}
for i in palabras:
    contador[i]= contador.get(i, 0)+1
print(f"palabras unicas {palabras_unicas}")
print(f"Contador de palabras {contador}")
 
#Ejercicio N°6   
alumnos={}

for i in range(3):
    nombre=input(f"Ingrese el nombre del alumno {i+1}: ")
    nota1=float(input(f"Ingrese las primer nota de {nombre}: "))
    nota2=float(input(f"Ingrese la segunda nota de {nombre}: "))
    nota3=float(input(f"Ingrese la tercer nota de {nombre}: "))

    alumnos[nombre]=(nota1,nota2,nota3)
for nombre, notas in alumnos.items():
    promedio= sum(notas)/len(notas)
    print(f"Alumno {nombre} promedio {promedio}")
    
#Ejercicio N°7
parcial1={'Franco','Carlos','Elio','German'}
parcial2={'Franco','Damian','Elio','Dario'}

print(f"Los Alumnos que aprobaron ambos parciales son :{parcial1 & parcial2}")
print(f"Los que aprobaron solo un parcial son: {parcial1 ^ parcial2 }")
print(f"Los que al menos aprobaron un parcial {parcial1 | parcial2}")

#Ejercicio N°8
lista_productos={"sillas":5, "mesas":7 ,"manteles":10}
print(f"Estos son los productos disponibles {lista_productos}")

nombre=str(input("Ingrese el producto que desea saber el stock: ")).lower()
if nombre in  lista_productos:
    print(f"El producto {nombre} y el stock de ese producto es {lista_productos[nombre]} unidades. ")
else:
    print("Ese Producto no existe!")
    nuevo=input("Desea agregar este producto? s(si) o n(no)").lower()
if nuevo=='s':
    cantidad=int(input("Stock del nuevo producto:"))
    lista_productos[nombre]=cantidad
    print(f"El producto es {nombre} y su stock {lista_productos[nombre]} unidades.")
print(f"Nueva lista de productos {lista_productos}")

#Ejercicio N°9
agenda = {}
for i in range(3):
    dia = input("Ingresá el día del evento: ")
    hora = input("Ingresá la hora del evento (por ejemplo 14:00): ")
    evento = input("Ingresá la descripción del evento: ")
    clave = (dia, hora)
    agenda[clave] = evento
print("\nAgenda completa:")
for clave, evento in agenda.items():
    print(f"{clave}: {evento}")
dia = input("\nConsultá un evento - ingresá el día: ")
hora = input("Ingresá la hora: ")
clave = (dia, hora)

if clave in agenda:
    print(f"En {dia} a las {hora} tenés: {agenda[clave]}")
else:
    print("No hay eventos en ese día y hora.")

#Ejercicio N°10
paises = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo"
}
capitales = {capital: pais for pais, capital in paises.items()}
print("Diccionario original (país -> capital):")
print(paises)
print("Diccionario invertido (capital -> país):")
print(capitales)
