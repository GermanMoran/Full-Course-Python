# Listas inmutables no se pueden modificar no cambian en el tiempo
# No se puede modificar nada referente a las tuplas

mytupla = ("Juan",12,56,89,3,33,3)
# Acceder a un elmento de una tupla
print(mytupla[2])

# Convertir una tupla en una lista
myLista = list(mytupla)
print("Lista: ",myLista)

# Convertir una lista a tupl
nuevaTupla = tuple(myLista)
print("Nueva Tupla: ",nuevaTupla)

# verificar si existen caracteres en la lista
print("Juan" in nuevaTupla)

# preguntar cuantas veces se encuentra un elemento x en la tupla
print(mytupla.count(3))

# Logitud de la tupla
print(len(mytupla))

# Definimos tupla unitaria
tuplaU = ("juan", )
print(len(tuplaU))

# Empaquetado de tupla
tupla2 = "juan" ,8 , 5 , 12
print(tupla2)

# Desempaquetado de la tupla
nombre,dia,mes,anio = tupla2
print("Nombre: ",nombre)
print("Dia: ",dia)
print("Mes",mes)
print("Año",anio)
