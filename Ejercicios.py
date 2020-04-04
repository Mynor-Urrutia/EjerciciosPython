print("Ejercicio #1 - Leer un numero y mostrarlo por la salida estándar si dicho número es o no es par")
def ejercicio1():
    numero=0
    numero=float(input("Ingrese un numero: "))
    if numero %2==0:
        print("El numero ", numero, " es un numero par")
    else:
        print("El numero ", numero, " es un numero inpar")
ejercicio1()

#-----------------------------------------------------------------------------------------------------------------------

print("Ejercicio #2 - Leer 2 números y mostrar el producto de ellos")
def ejercicio2():
    primernumero=int(input("Ingrese un numero: "))
    segundonumero=int(input("Ingrese un numero: "))
    producto=int(0)
    while segundonumero !=0:
        producto=producto+primernumero
        segundonumero=segundonumero-1
    print("El producto es de: ", producto)
ejercicio2()

#-----------------------------------------------------------------------------------------------------------------------

print("Ejercicio #3 - Leer 2 números y determinar el mayor de ellos. ")
def ejercicio3():
    numero1=int(input("Ingrese un numero: "))
    numero2=int(input("Ingrese el siguiente numero: "))

    if numero1 == numero2:
        print("Ambos numeros son iguales")
    else:
        if numero1>numero2:
            print("El numero mayor es: ", numero1)
        else:
            print("El numero mayor es: ", numero2)

ejercicio3()

#-----------------------------------------------------------------------------------------------------------------------

print("Ejercicio #4 - Leer 3 numeros y determinar el mayor de ellos.")
def ejercicio4():
    num1=int(input("Ingrese un numero"))
    num2=int(input("Ingrese otro numero"))
    num3=int(input("Ingrese otro numero"))

    if num1==num2 & num1==num3:
        print("Todos los numeros ingresados son iguales")
    else:
        if num1>num2 & num1>num3:
            print("El numero mayor es: ", num1)
        else:
            if num2>num1 & num2>num3 or (num3<=num2):
                print("El numero mayor es: ", num2)
            else:
                print("el numero mayor es: ", num3)
ejercicio4()

#-----------------------------------------------------------------------------------------------------------------------

print("Ejercicio #5 - Leer un numero y mostrar una tabla de multiplicar")

def ejercicio5():
    factor1=int(input("Ingrese el numero a multiplicar: "))
    factor2=int(input("Ingrese las veces que quiere multiplicar el numero anterior: "))

    for i in range(1,factor2+1):
        print(str(i)+" * "+str(factor1)+" = "+str(i*factor1))
ejercicio5()

#-----------------------------------------------------------------------------------------------------------------------

print("Ejercicio #6 - Leer una secuencia de 30 números y mostrar la suma y el producto de ellos")

def ejercicio6():
    contador=30
    sumatotal=0
    producto=0
    productototal=0

    while contador != 0:
        numero = int(input("Ingrese un numero: "))
        sumatotal=sumatotal+numero
        productototal=productototal*numero
        contador=contador-1
    print("La suma de los digitos es de: ", sumatotal, "y su producto es: ", productototal)
ejercicio6()

#-----------------------------------------------------------------------------------------------------------------------

print("Ejericicio #7 - Leer una secuencia de números, hasta que se introduce un número negativo y mostrar la suma de dichos números. ")
def ejercicio7():
    cantidadcontador=int(input("Ingrese la cantidad de digitos que va a ingresar"))
    sumaTotal=0
    while cantidadcontador != 0:
        numeros=int(input("Ingrese los numeros: "))
        if numeros <= 0 :
            cantidadcontador = cantidadcontador - cantidadcontador
        else:
            sumaTotal = sumaTotal + numeros
            cantidadcontador = cantidadcontador - 1
    print("La suma total de los numero ingresados es de: ", sumaTotal)
ejercicio7()

#-----------------------------------------------------------------------------------------------------------------------

print("Ejericicio #8 - Leer dos números y realizar el producto mediante sumas. ")

def ejercicio8():
    primernumero = int(input("Ingrese un numero: "))
    segundonumero = int(input("Ingrese un numero: "))
    producto = int(0)
    while segundonumero != 0:
        producto = producto + primernumero
        segundonumero = segundonumero - 1
    print("El producto es de: ", producto)
ejercicio8()

#-----------------------------------------------------------------------------------------------------------------------

print("Ejercicio #9 - Leer dos números y realizar la división mediante restas mostrando el cociente y el resto. ")

def ejercicio9():
    divisor=int(print("Ingrese el dividendo: "))
    dividendo=int(print("Ingrese el divisor: "))
    contador=int(0)
    dividendo=dividendo-divisor
    while dividendo >= 0:
        contador=contador+1
        dividendo=dividendo-divisor
    print("El numero es, ", contador)
ejercicio9()
