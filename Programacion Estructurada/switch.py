# No esta disponoble en el lenguaje de progración python
salario_presidente = int(input("Introduzca salario del presidente: "))
print("salario presidente es : "+str(salario_presidente))

salario_jefe = int(input("Introduzca salario del jefe: "))
print("salario presidente es : "+str(salario_jefe))

salario_cordinador = int(input("Introduzca salario del cordinador: "))
print("salario presidente es : "+str(salario_cordinador))

salario_administrativo = int(input("Introduzca salario del administrativo: "))
print("salario presidente es : "+str(salario_administrativo))

if (salario_presidente < salario_jefe < salario_cordinador < salario_administrativo):
    print("Todo funciona bien")
else:
    print("Ha ocurrido un error en la ejecucio")