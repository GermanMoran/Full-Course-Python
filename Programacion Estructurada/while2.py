# Programa que permite calcular la raiz cuadrada de un numero (Exepcion numeros negativos)

import math
print("Programa de calculo de raiz cuadrada")
numero = int(input("\nIntroduce un numero por favor: "))
intentos = 0

while numero <0:
    print("no se puede hallar la raiz de un numero negativo")

    if intentos==2:
        print("Has consumido muchos intentos intentos")
        break

    numero =  int(input("\nIntroduce un numero por favor: "))
    if numero < 0:
        intentos = intentos+1


if intentos <2 :
    print(f"La raiz cuadrada del numero {numero} es: {math.sqrt(numero)}")