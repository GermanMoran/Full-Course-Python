# Se importa las funciones - variables clases con un alias
# * Permite importar todas las funciones relacionadas al modulo
# * reserva un espacio en emmoria al importar todas las clases, en programas complejos se debe importar unicamnete la clase


import funciones_matematicas as fm
fm.suma(5, 7)

# otra forma de importar
from funciones_matematicas import *
resta(10, 5)
producto(5, 6)
