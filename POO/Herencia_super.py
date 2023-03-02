# Metodo super() utilizado en la herencia multiple
# La función isinstance() TRUE OR  FALSE para determinar si es instancia de una clase.
# ===============================================================================================

# clase persona
class Persona():

    #constructor - parametros iniciales
    def __init__(self,nombre,edad,lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia
    
    # Definicion de metodos

    def descripcion(self):
        print("\nNombre: ",self.nombre,"\nEdad: ",self.edad,"\nResidencia: ",self.lugar_residencia)




# Clase empleado
# La clase empleado hereda de persona
class Empleado(Persona):
    # cosntructor

    def __init__(self, salario, antiguedad,nombre_empleado,edad_empleado,residencia_empleado):
        
        # Incluimos el metodo super , de esta manera estamos llamando el metodo init de la clase padre

        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario = salario
        self.antiguedad = antiguedad
    
    


#Intancia de la clase
Antonio = Empleado(1500, 15,"Manuel",55,"colombia")
Antonio.descripcion()


print(isinstance(Antonio, Persona))