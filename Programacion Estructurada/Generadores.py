# Funcion que genere direcciones ip al azar - trabajar con generadores es  muchos mas util que
# hacerlos con una funcion.

# Funcion para generar numero pares


listaPares=[]
def generarPares(limite):
    num = 1
    while num < limite:
        listaPares.append(num*2)
        num = num+1
    
    return listaPares

# Funcion principal
print(generarPares(6))


# Generacion de las la lista de pares mediante un iterador

def generarParesGenerador(limite):
    num = 1
    while num < limite:

        # Yield: constuye un objeto iterable y almacena los valores de la lista de 1-1
        yield num*2
        num = num+1
    

# Creo el objeto iterable
ObjIterable = generarParesGenerador(10)


#Imprimir los valores del generador
#Imprimir en consola - valor a valor que se va amacenado en el generador
#Entre llamda y llamda el generador entra en un estado de suspencion  - se ahorran recursos


print(next(ObjIterable))
print("Aqui podria ir mas codigo")
print(next(ObjIterable))
print("Aqui podria ir mas codigo")
print(next(ObjIterable))
print("Aqui podria ir mas codigo")
