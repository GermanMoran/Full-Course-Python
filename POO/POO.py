class carro():


    # Definimos el constructor de la clase
    def __init__(self):
            self.__largoChasis=250
            self.__anchoChasis=150
            # Encapsulas la variable ruedas que no se accesible desde el esterior de la clase, pero si internamente
            # dentro de la misma clase
            self.__ruedas=4
            self.__enmarcha = False

    def arranca(self,estadoCarro):
        self.__enmarcha = estadoCarro

        # Una vez que el coche esta en marcha se verifica su estado interno
        if(self.__enmarcha):
            chequeo = self.__chequeoInterno()

        if(self.__enmarcha and chequeo==True):
            return "El coche esta encendido"
        
        elif(self.__enmarcha and chequeo==False):
            return "No se puede arrancar porque algo ha ido mal en el chequeo"
        else:
            return "El coche esta Apagado"

    
    def estado(self):
        print("El carro tiene: ",self.__ruedas," ruedas, un lardo de chasis de: ",self.__largoChasis," y un ancho de chasis de: ",self.__anchoChasis)



    # se crea un nuevo metodo para analizar el chequeo del carro
    def __chequeoInterno(self):
        print("Se realiza un chequeo interno del estado del carro /n")
        self.gasolina= "OK"
        self.carbulador="false"
        self.puertas ="Cerradas"

        if (self.gasolina=="OK" and self.carbulador=="OK" and self.puertas=="Cerradas"):
            return True
        else:
            return False
       


#INSTANCIAMOS LAS CLASES
# =======================================================================================0
print("-------------------Creamos el primer objeto ------------------------")
miCarro =carro()
print(miCarro.arranca(True))
miCarro.estado()

print("-------------------Creamos el segundo objeto ------------------------")
miCarro2 =carro()
print(miCarro2.arranca(False))
miCarro2.ruedas=2
miCarro2.estado()
print(miCarro2.chequeoInterno())


