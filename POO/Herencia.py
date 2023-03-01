# se crea la superclase
class vehiculos():
    # Se define el constructor de la clase.
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera = False
        self.frena=False
    
    # Se definen los comportamientos y metodos del vehiculo

    def enmarcha(self):
        self.enmarcha=True

    def acelera(self):
        self.acelera=True
    
    def frenar(self):
        self.frena=True
    
    def estado(self):
        print("Marca: ",self.marca,"\nModelo: ",self.modelo,"\nEsta en marcha: ",self.enmarcha,"\nEsta acelerando: ",self.acelera,"\nEsta frenado: ",self.frena)


# Definimos una nueva instancia de la clase en este caso es la clase furgon
# ==================================================================================================
class Furgon(vehiculos):
    def carga(self,cargar):
        self.cargaPesada = cargar
        print("La furgoneta Carga alrededor de: ",self.cargaPesada)


# Definimos la herencia entre clases - se crea una clase hija Moto
# ==================================================================================================
class Moto(vehiculos):
    hstum = ""
    def haceStum(self):
        self.hstum = "En moto se puede hacer stum"
    
    # Como esta clase tiene el mismo metodo estado, se sobre escribe este metodo por encima del metodo
    # heredado de la clase padre
    def estado(self):
         print("Marca: ",self.marca,"\nModelo: ",self.modelo,"\nEsta en marcha: ",self.enmarcha,"\nEsta acelerando: ",self.acelera,"\nEsta frenado: ",self.frena,"\n: ",self.hstum)


# Clase vehiculos electricos
class vElectricos():
    def __init__(self):
        # Numero de km que recorrera el vehiculo
        self.autonomia = 100
    
    def cargarEnergia(self):
        self.cargando = True


# Creamos una instancia de la clase Moto
# ================================================================================================00
miMoto = Moto("Honda","CBR")
# Utilizamos la instancia para llamar al metodo
miMoto.estado()


# Creamos una instancia de la clase Furgoneta
# ================================================================================================
miFurgoneta = Furgon("Hino", "2008")
# Utilizamos la instancia para llamar al metodo
miFurgoneta.estado()
miFurgoneta.carga(10)


# La bicicleta electrica puede tener comportamiento de 2 clases
# clase vehiculo - clase vehiculos electricos

# HERENCIA MULTIPLE - SE HEREDA DE 2 CLASES
# Nota: Cuando hay herencia multiple se da preferencia a la primera clase que se colque.
# ===============================================================================================

class bicicletaElectrica(vElectricos,vehiculos):
    pass

# se crea una instancia de la clase
miBici = bicicletaElectrica()
miBici.cargarEnergia()