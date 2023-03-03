# POLIMORFISMO
# =======================================================================================


class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando 4 ruedas")
    
class Moto():
    def desplazamiento(self):
        print("Me desplzao utilizando 2 ruedas")

class Camion():
    def desplazamiento(self):
        print("Me desplazo utilizando 6 ruedas")


# Se intancia la clase Moto
# El metodo o comportamiento pertenece a 2 clases diferentes
# =======================================================================================

miVehiculo = Moto()
miVehiculo.desplazamiento()

miVehiculo2=Camion()
miVehiculo2.desplazamiento()

# Polimorfismo: Un objeto tiene la capacidad de cambair de forma y
# comportarse dependiendo del contexto.
# Python es debilmente tipado, no se tiene que especificar forzosamente que tipo es
# ==================================================================================

def desplazaminetoVehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo3 = Coche()
desplazaminetoVehiculo(miVehiculo3)