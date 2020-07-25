# Uso del Operador and

a = 3
valorMinimo = 0
valorMaximo = 5
dentroDeRango = (a >= valorMinimo and a <= valorMaximo)
#print(dentroDeRango)
if(dentroDeRango):
    print("La variable a =",a," se encuentra Dentro de Rango")
else:
    print("La variable a =",a," se encuentra Fuera de Rango")

a = -1
valorMinimo = 0
valorMaximo = 5
dentroDeRango = (a >= valorMinimo and a <= valorMaximo)
#print(dentroDeRango)
if(dentroDeRango):
    print("La variable a =",a," se encuentra Dentro de Rango")
else:
    print("La variable a =",a," se encuentra Fuera de Rango")
    
a = int(input("Por favor proporciona un valor: "))
valorMinimo = 0
valorMaximo = 5
dentroDeRango = (a >= valorMinimo and a <= valorMaximo)
#print(dentroDeRango)
if(dentroDeRango):
    print("La variable a =",a," se encuentra Dentro de Rango")
else:
    print("La variable a =",a," se encuentra Fuera de Rango")

#______________________________________________    
# Uso del Operador or

vacaciones = False
diaDescanso = False
if (vacaciones or diaDescanso):
    print("Podemos ir al parque")
else:
    print("Tienes deberes que hacer")
    
vacaciones = True
diaDescanso = False
if (vacaciones or diaDescanso):
    print("Podemos ir al parque")
else:
    print("Tienes deberes que hacer")
    
vacaciones = False
diaDescanso = True
if (vacaciones or diaDescanso):
    print("Podemos ir al parque")
else:
    print("Tienes deberes que hacer")
    
#______________________________________________    
# Uso del Operador not

# Se usa para invertir el valor boleano o invertir la logica de nuestros algoritmos

print(not(vacaciones))
