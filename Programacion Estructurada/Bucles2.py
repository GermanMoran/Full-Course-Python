# Operador Range en Bucles
'''
# Manejo
for i in range(5):
    print(f"Valor de la variable {i}")


#Listas desde un numero inicial al final
for i in range(5,50,3):
    print(f"Valor de la variable {i} ")

'''
# Programa simple para comprabar si un correo electronico es valido

emailValido = False
contador = 0
email = input("\nDigitar su email: ")
for i in email:
    print(i)
    if i == "@":
        emailValido = True
    else:
        pass

print(f"El email digitado es {emailValido}")
