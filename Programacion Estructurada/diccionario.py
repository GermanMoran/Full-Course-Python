# Sintasis diccion
# claves (valor numerico. textto, tuplas)
dicc = {"colombia":"Bogota","Alemania":"Berlin","Freancia":"paris","España":"Madrid"}
# Acceder elemento completo del diccionario
print("Capital",dicc["España"])
print("Diccionario", dicc)
# Agregar mas elementos a un diccionario  ya construido
dicc["portugal"]= "lisboa"
print("Nuevo diccionario: ",dicc)
# Modificar valor diccionario
dicc["Italia"] = "Roma"
print("Nuevo diccionario: ",dicc)

# Eliminar elementos de la lista
del dicc["Italia"]
print("Elemntos eliminados del diccionario : ",dicc)

# <------- ELIMINAR ELEMENTOS DEL DICCIONARIO ------------------------>

nuvo_dicc = {"colombia":"Bogota",52:"jordan",10:"mesi"}
mitupla = ["España","Francia","Reino Unido","Alemania"]
midiccionario = {mitupla[0]:"A",mitupla[1]:"B",mitupla[2]:"C"}
print(midiccionario)

# hACER QUE UN DICCIONARIO ALMECENA UNA TUPLA
midicc = {23:"Jordan","equió":"chicago","anillo":[1999 , 1993,2018]}
print("El nuevo diccionario: ",midicc)

# Acceder a la lista dentro del diccioanrio
print(midicc["anillo"])

# METODOS DEL DICCIONARIO
print(midicc.keys())
print(midicc.values())
print("Longitud del diccionario: ",len(midicc))