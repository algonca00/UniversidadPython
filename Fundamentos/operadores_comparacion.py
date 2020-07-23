# operador de comparacion == (es igual que)
a = 3
b = 3
resultado = (a == b)     # Los parantesis son opcionales
print("a = ",a," y b = ",b)
print("es a = b ? ",resultado)

a = 3
b = 2
resultado = (a == b)
print("a = ",a," y b = ",b)
print("es a = b ? ",resultado)

# operador de comparacion != (es diferente que)
resultado = (a != b)
print("a = ",a," y b = ",b)
print("es a diferente a b ? ",resultado)

# operador de comparacion > (mayor que)
resultado = (a > b)
print("a = ",a," y b = ",b)
print("es a > b ? ",resultado)

# operador de comparacion >= (mayor o igual  que)
resultado = (a >= b)
print("a = ",a," y b = ",b)
print("es a >= b ? ",resultado)

# operador de comparacion < (menor que)
resultado = (a < b)
print("a = ",a," y b = ",b)
print("es a < b ? ",resultado)

# operador de comparacion <= (menor o igual  que)
resultado = (a <= b)
print("a = ",a," y b = ",b)
print("es a <= b ? ",resultado)

a = 4
if a % 2 == 0:
    print("La variable a es igual a:",a,"osea es par")
else:
    print("La variable a es igual a:",a,"osea es inpar")
a = 5
if a % 2 == 0:
    print("La variable a es igual a:",a,"osea es par")
else:
    print("La variable a es igual a:",a,"osea es inpar")   
    
edadLimite = 18
edadPersona = 5
print("Pedro tiene ",edadPersona," años de edad")
if (edadPersona > edadLimite):
    print("es un adulto")
else:
    print("se considera menor de edad")
    
edadPersona = 20
print("Juan tiene ",edadPersona," años de edad")
if (edadPersona > edadLimite):
    print("es un adulto")
else:
    print("se considera menor de edad")
    
