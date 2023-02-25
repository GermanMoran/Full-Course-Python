# Simplificar la estructura de los bucles for anidados
# Funcion generador que devuelva ciudades
# * Dentro de la función significa que recibira un numero determinado de elementos

'''
Esta es la forma clasica de realizar Generador con for anidados
'''
def devuelveCiudades(*ciudades):
    for elemento in ciudades:
        for subElmento in elemento:
            yield subElmento

# Creamos el objeto iterable
ciudades_recuperadas = devuelveCiudades("Madrid","Bogota","Venecia","Paris")
# Imprimimos algunos elementos del objeto iterbles
print(next(ciudades_recuperadas))
print("salto de linea")
print(next(ciudades_recuperadas))



'''
  yield from reduce los for anidados yield form  [primer elemento]
  Acceder desde la funcion generador a cada una de las letras que forman parte de los elementos

'''


def devuelveCiudades1(*ciudades):
    for elemento in ciudades:
        yield from elemento

# Creamos el objeto iterable
ciudades_recuperadas2 = devuelveCiudades1("Madrid","Bogota","Venecia","Paris")
# Imprimimos algunos elementos del objeto iterbles
print(next(ciudades_recuperadas2))
print("salto de linea")
print(next(ciudades_recuperadas2))


