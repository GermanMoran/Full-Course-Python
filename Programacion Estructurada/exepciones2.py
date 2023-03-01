# Libreias y dependencias
import math

# Lanzar de forma intencionada las execpciones en nuestro codigo (raise)
def evaluarEdad(edad):

    # Metodo raise para lanzar la exepción.
    # Raise permite personalizar el mensaje lanzado al usuario.
    # Typeerror es una clase ya definida, por lo tanto se puede usar.
    if edad < 0:
        raise TypeError("No se permiten edades negativas")

    if edad < 20:
        return "Eres muy joven"
    elif edad < 40:
        return "Eres joven"
    elif edad < 60:
        return "Eres viejo"
    elif edad < 80:
        return "Eres demasiado viejo"


# Funcion para calular la raiz cuadrada
def calcularRaiz(numero):
    if numero < 0:
        raise ValueError("No se puede calcular raiz negativa de un numero")
    else:
        raiz = math.sqrt(numero)
    
    return raiz
    
# Primera funcion 
print(evaluarEdad(8))
numero = int(input("\nIntroduce el numero: "))

try: 
    print("La raiz cuadrada del numero es: ",calcularRaiz(numero))
except ValueError as errNum:
    print(errNum)



print("Programa termiando")