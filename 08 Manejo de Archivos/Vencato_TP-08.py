#Ejercicio N°1 
archivo= open("productos.txt","w")
archivo.write("nombre,precio,cantidad\n")
archivo.write("Destornillador,500,12\n")
archivo.write("Alicate,700,16\n")
archivo.write("Pinza,1000,7\n")
archivo.close()

#Ejercicio N°2 
with open("productos.txt","r")as archivo:
    for linea in archivo:
        linea=linea.strip()
        partes=linea.split(",")
        if len(partes)==3:
            productos=partes[0]
            precio=partes[1]
            cantidad=partes[2]
        print(f"Producto={productos}|Precio={precio}|Cantidad={cantidad}")
#Ejercicio N°3
with open("productos.txt", "r") as caja:
    herramientas=caja.read()
    print(herramientas)
    nombre=input("Ingrese el nombre del producto: ").strip()
    precio=input("Ingrese el precio del producto: ").strip()
    cantidad=input("Ingrese la cantidad del producto").strip()
with open("productos.txt","a")as caja:
    caja.write(f"{nombre},{precio},{cantidad}\n")
    
#Ejercicio N°4
productos = []  
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        partes = linea.split(",")
        if len(partes) == 3:
            nombre = partes[0]
            precio =partes[1] 
            cantidad = partes[2]
                
            producto = {
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cantidad
                }
        productos.append(producto)
        
if productos:
    print(" Productos cargados:\n")
    for p in productos:
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
else:
    print(" No hay productos cargados.")

print("\n Ingresar nuevo producto:")
nombre = input("Nombre del producto: ").strip()
precio = input("Precio: ")
cantidad = input("Cantidad: ")

nuevo = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
productos.append(nuevo)

with open("productos.txt", "a") as archivo:
    archivo.write(f"{nombre},{precio},{cantidad}\n")

print(f"\n Producto '{nombre}' agregado correctamente.")

#Ejercicio N°5
productos = []  
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        productos.append({
                "nombre": nombre,
                "precio": precio,
                "cantidad": cantidad
            })

buscado = input(" Ingresá el nombre del producto a buscar: ").strip()
encontrado = False

for p in productos:
    if p["nombre"].lower() == buscado.lower():
        print(f"\n Producto encontrado:")
        print(f"Nombre: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print(" No se encontró el producto solicitado.")
    
#Ejercicio N°6

with open("productos.txt", "w") as archivo:
    for p in productos:
        linea = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
        archivo.write(linea)

print(" Archivo 'productos.txt' actualizado correctamente.")

