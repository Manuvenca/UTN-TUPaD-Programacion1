#Ejercici N°1
lista_notas=[7.5,5,3.6,9,10,8.5,9.6,7,8,1]
promedio=sum(lista_notas)/ len(lista_notas)
print(f"el maximo es:", max(lista_notas))
print(f"el minimo es:", min(lista_notas))
print("Y el promedio es: ", promedio)

#Ejercicio N°2
productos=[]
for i in range(5):
    elemn=input(f"Ingrese el elemento "+ str(i+1)+ " :")
    productos.append(elemn)
print (sorted(productos))
eliminar=input("¿Que elemento desea eliminar?")
if eliminar in productos:
    productos.remove(eliminar)
    print (sorted(productos))
else:
   print("No se encontro el prducto")
    
#Ejercico N°3
import random
numeros = [random.randint(1, 100) for _ in range(15)]
print("Lista original:", numeros)


pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]

# Mostrar resultados
print("\nLista de pares:", pares)
print("Cantidad de pares:", len(pares))

print("\nLista de impares:", impares)
print("Cantidad de impares:", len(impares))

#Ejercicio N°4
lista=[1,3,5,3,7,1,9,5,3]
nueva_lista=list(set(lista))
print("La nueva lista es ", nueva_lista)

lista_sinrepetir=[]
for elm in lista:
    if elm not in lista_sinrepetir:
        lista_sinrepetir.append(elm)
print("Esta es otra forma de hacer un lista", lista_sinrepetir)

#Ejercicio N°5
listra_estudiantes=[]
for i in range(3):
    estudiante=input("Ingese el estudiante "+ str(i+1)+" : ")
    if estudiante not in listra_estudiantes:
        listra_estudiantes.append(estudiante)
print(listra_estudiantes)
opcion=int(input("¿Desea agregar o eliminar un estudiante? \n Presione 1 para agregar o 2 para eliminar: " ))
eliminar=""
if opcion==1:
    eliminar=input("Ingrese el nombre que desea agregar: ")
    if eliminar not in listra_estudiantes:
        listra_estudiantes.append(eliminar)
elif opcion==2:
    eliminar=str(input("Ingrese el nombre que desea eliminar:"))
    if eliminar in listra_estudiantes:
        listra_estudiantes.remove(eliminar)   
    else:
        eliminar not in listra_estudiantes
        print("El nombre no esta en la lista ")  
else:
    print("Opcion incorrecta")
print(listra_estudiantes)

#Ejercicio N°6
lista=[]
lista_original=[1,2,3,4,5,6,7]
lista_invertida=list(reversed(lista_original))
print("Esta es la lista original ", (lista_original), "\n y esta es la lista invertida ", (lista_invertida))

#Ejerccio N°7
temperatura=[
    [10,16],
    [15,25],
    [9,12],
    [19,21],
    [22,25],
    [13,19],
    [7,11]   
]
print(temperatura)
print(type(temperatura))

minimas = [dia[0] for dia in temperatura]
maximas = [dia[1] for dia in temperatura]
print(minimas)
print(maximas)
prom_min = sum(minimas) / len(minimas)
prom_max = sum(maximas) / len(maximas)

print(f"Promedio de mínimas: {prom_min:.1f}")
print(f"Promedio de máximas: {prom_max:.1f}")

amplitudes = [dia[1] - dia[0] for dia in temperatura]
mayor_amplitud = max(amplitudes)
dia_max_amp = amplitudes.index(mayor_amplitud) + 1  # +1 porque los días empiezan en 1

print(f"La mayor amplitud térmica fue {mayor_amplitud}°C, en el día {dia_max_amp}.")

#Ejercicio N°8
nota=[
    [8,9,10],#Estudiante1
    [6,5,7],#Estudiante2
    [3,4,2],#Estudiante3
    [10,9,6],#Estudiante4
    [7,5,3],#Estudiante5
]
for i in range(len(nota)):
    promedio=sum(nota[i])/len(nota[i])
    print("estudiante",(i+1), "promedio es ",(promedio))
    
materia=len(nota[0])
estudiante=len(nota)

for j in range(materia):
    suma=0
    for i in range(estudiante):
        suma+=nota[i][j]
        promedio=suma/estudiante
    print(f"Materia {j+1}: {promedio:.1f}")

#Ejercicio N°9
tablero=[]
for i in range(3):
    fila=[]
    for j in range(3):
        fila.append("-")
    tablero.append(fila)    
for fila in tablero:
    for celda in fila:
        print(celda, end= " ")
    print()
jugador="x"
jugadas=0
while jugadas<9:
    print(f"\n turno del jugador{jugador}")
    fila=int(input("Ingrese un numero para la fila entre 0-2: "))
    columna=int(input("Ingrese un numero para la columna entre 0-2: "))
    if fila>2 or fila< 0 or columna<0 or columna> 2:
        print("Piscion fuera de rango , Intente de nuevo")
        continue
    if tablero[fila][columna]=="-":
        tablero[fila][columna]=jugador
        jugadas+=1
    else:
        print("Casilla ocupada, intente de nuevo")    
        continue
    for fila in tablero:
        for celda in fila:
            print(celda, end= " ")
        print()   
    if jugador=="x":
        jugador="O"
    else:   
        jugador="x"   
#Ejercico N°10
ventas = [
    [10, 12, 15, 20, 18, 25, 22],  # Producto 1
    [5, 8, 6, 7, 9, 10, 6],        # Producto 2
    [12, 15, 10, 18, 20, 17, 16],  # Producto 3
    [8, 7, 9, 12, 10, 11, 9]       # Producto 4
]
print("Total vendido por cada producto:")
totales_productos = []
for i in range(len(ventas)):
    total = sum(ventas[i])
    totales_productos.append(total)
    print(f"Producto {i+1}: {total}")
print()
ventas_dias = [sum(ventas[i][j] for i in range(len(ventas))) for j in range(7)]
mayor_venta = max(ventas_dias)
dia_mayor = ventas_dias.index(mayor_venta) + 1 
print(f"El día con mayores ventas totales fue el día {dia_mayor} con {mayor_venta} unidades.")

print()
producto_mas_vendido = totales_productos.index(max(totales_productos)) + 1
print(f"El producto más vendido en la semana fue el Producto {producto_mas_vendido}.")

