# Bucle While

edad = int(input("\nPorfavor introduzca su edad: "))
while edad<0 or edad >100:
    print("Su edad no puede ser negativa o mayor a 100 años")
    edad = int(input("\nVuelva a introduccir su edad: "))

print("Su edad es correcta")
print("La edad del aspirante es : "+str(edad))
