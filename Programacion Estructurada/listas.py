#  Objeto iterable de la lista
# <------------- Las listas de python pueden almacenar cualquier tipo de datos   --------->
myLista = [1,2,8,"casa",78]
#Imprimier todos los elementos de la lista
print(myLista[:])
#Imprimir el ultimo elmento de la lista 
print(myLista[-1])
#Acceder porcion de la lista
print(myLista[1:3])
# Agregar elementos de la lista   metodo append Agrega elmento al final
myLista.append("Carlos")
myLista.append("Andres")

# Agregar elementos a la lista - metodo inset agrega el elemnto en la posicion definida
myLista.insert(2, 2040)
print("La nueva lista es : ",myLista)

# Agregar varios elemntos a la lista mediante el metodo extende
myLista.extend(["casa","alba","viaje","hoy","viaje"])
print("Nueva lista: ", myLista)

# Obteber el indice de un elemnto de la lista
print(myLista.index("viaje"))

# Comrpbar si un elemento se encuentra en una lista
print( "casas" in myLista)

# Eliminar elementos de las listas python
print(myLista.remove("Carlos"))
print("La nueva lista despues de la eliminacion de elementos: ",myLista)

# Eliminar el ultimo elemnto de la lista
myLista.pop()
print(myLista)


# OPERACIONES ENTRE LISTAS ---- (UNION - +)
lista1 = [5,8 ,"carlos","True",56]*3
lista2=[12,8,5,"casa","verano"]
lista3 =lista1 + lista2
print("La nueva lista es: ", lista3)

# Operador repetidors (*)
print("Operador repetidor: ",lista1)