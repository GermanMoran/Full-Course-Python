for i in ["America", "Nacional",3]:
    # No hacer salto de linea
    print("Hola",end=" ")




myemail = input("Introduce el email: ")

email = False
# Imprimir un string 
for i in myemail:
    # Imprimir el correo electronico en una sola linea.
    if i == "@":
        email=True



print("\nEl resultado de la consulta es :", email)