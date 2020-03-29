#Leer una secuencia de números y sumar solo los pares mostrando el resultado del proceso.
print("Ejercicio #1")
def producto():
    primerNumero = int(input("Escribe un número: "))
    segundoNumero = int(input("Escribe otro numero: "))

    producto = int(0)

    while segundoNumero !=0:
        producto = producto + primerNumero
        segundoNumero = segundoNumero -1

    print("El producto de la suma es de los datos ingresados es: " + str(producto))
producto()

print("Ejericio #2")
def productoraro():
    num1=1
    num2=1
    i = ord('d')
    while not i == 102:
        num2 = int(input("Ingrese un numero"))
        i = ord(input("Presione f para salir"))
        print(num2)
        num1 = num1 * num2
    print(num1)
productoraro()

print("Ejercicio #3")
def nmayor():
    numero_mayor =0
    k=1
    contador = int(input("Escriba la cantidad de numeros que desea comparar: "))
    while k<=contador:
        numeros = float(input("Digitar el numero: "))
        if numeros>numero_mayor:
            numero_mayor=numeros
        else:
            numero_mayor=numero_mayor
        k=k+1
    print("El numero mayor es: ",str(numero_mayor))
nmayor()
print("Ejercicio #4")
def fibonacci():
    aux, fib, init= 1,0,1

    limite=int(input("Ingrese un numero entero positivo para la serie de Fibonacci: "))

    if limite >0:
        print("El resultado es: ")
        while init <=limite:
            print("[{0}]".format(fib), end="")
            aux += fib
            fib =aux -fib
            init +=1
            print()
fibonacci()
print("Ejercicio #6")
def factorial():
    from math import factorial
    nfactorial=int(input("Ingrese un numero entero posisitivo: "))
    print(factorial(nfactorial))
factorial()

print("Ejercicio #7")
def secuencia():
    primos = [2]
    nmax = 30
    for x in range(2, nmax):
        for i in range(2, x):
            if x%i != 0:
                continue
            else:
                break
        else:
            print ('%d es primo'%x)
            primos.append(x)
    F = open('numerosprimos.txt', 'w')
    for data in primos:
        F.write('%d\n'%data)
secuencia()