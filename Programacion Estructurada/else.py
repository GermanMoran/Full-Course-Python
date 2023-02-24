# Ejemplo de la Instrucción else dentro de un bucle
email = input("\nIntroduce tu email por favor: ")
for i in email:
    if i=="@":
        arroba=True
        break
else:
    arroba=False


print("El valor asociado a la variable arroba es: ",arroba)