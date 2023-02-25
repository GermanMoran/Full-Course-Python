# Programa division basica manejo de errores
numero1 = int(input("\nDiguite el primer numero: "))
numero2 = int(input("\nDiguite el segundo numero: "))

def division(numero1,numero2):
    try:
        return numero1/numero2
    except :
        return "La divición no se puede ejecutar"

# Llamamos la función
print("La division es: ",division(numero1, numero2))