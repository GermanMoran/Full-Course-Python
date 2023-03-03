# Manipulación de cadenas en python
# Metodos python : 
# =======================================================================================
nombreUsuario = input("\nIntroduzca nombre Usuario: ")
print("El nombre es: ",nombreUsuario)

# Pasar a mayuscula la cadena
print("MAYUSCULA: ",nombreUsuario.upper())
print("MINUSCULA: ",nombreUsuario.lower())
print("MINUSCULA: ",nombreUsuario.capitalize())



# EJEMPLO 2
# =====================================================================================

edad = input("\nIntroduze la edad: ")


# Verificar si la edad es un valor numerico
if (edad.isdigit()):
    print("Edad numerica")
else:
    print("La edad no es un valor numerico")