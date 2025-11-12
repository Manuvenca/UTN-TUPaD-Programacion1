#Funcion Factorial
def Factorial(x):
    if x == 0:
        return 1
    else:
        return x * Factorial(x-1)

x=(int(input("Ingrese el numero que desea saber su factorial: ")))
print(f"El factorial de {x} es {Factorial(x)}")

#Funcion Fibonacci
def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos-1)+fibonacci(pos-2)
pos= int (input("Ingrese la posicion que desea saber su fibonacci: "))
print(f"La posicion {pos} su fibonacci es  {fibonacci(pos)}")

#Calculo de Potencia 
def potencia (base,exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base , exponente -1)
base = int (input("Ingrese la base: " ))
exponente = int (input("Ingrese el exponente:" ))
print(f"La potencia de {base} elevado a {exponente} es {potencia(base, exponente)}")

#Calculo Binario
def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
num = int(input("Ingrese un numero decimal para convertir en binario: " ))
print(f"El numero decimal {num} en binario es {decimal_a_binario(num)} ")

#Verificar palindromo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    
    return es_palindromo(palabra[1:-1])
palabra=(input("Ingrese la palabra que deseas: "))

if es_palindromo(palabra)== True:
    print(f"La {palabra} es palindromo")
else:
    print(f"La {palabra} no es palidromo")

#Suma de digitos 
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

n=int(input("Ingrese el numero que deseas: "))
print(f"La suma de {n} es {suma_digitos(n)}")

#Contar Bloques 
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)
n = int(input("Ingrese la cantidad de bloques del primer nivel: "))
print(contar_bloques(n))

#Contador de digito
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)
numero= int(input("Ingrese el numero que desee: "))
digito= int (input("Ingrese el numero del digito que desea saber: "))
print(f"El numero es: {numero} y el digito es: {digito} y la cantidad de veces es que se repite el digito es: {contar_digito(numero,digito)}")




