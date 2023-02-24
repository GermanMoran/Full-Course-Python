print("Programa de Evaluacion de notas de alumnos")
Nota_alumno = input("Introduzca un valor: ")
def evaluacion(nota):
    valoracion = "aprobado"
    if int(nota) < 5:
        valoracion="reprobado"
    return valoracion

print("La nota es: ",evaluacion(Nota_alumno))