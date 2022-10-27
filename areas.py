import math

opcion = input("Ingrese una opción:\n1: área de círculo\n2: área de triángulo\n3: área de cuadrado")
if opcion == "1":
    pi = math.pi
    radio = float(input("ingrese el radio en cm: "))
    operación1 = radio*radio
    operación2 = pi*operación1
    print('El área del círculo es: '+str(operación2)+" cm²")
elif opcion == "2":
    base = float(input("ingrese la base en m: "))
    altura = float(input("ingrese la altura en m: "))
    operación1 = base*altura
    operación2 = operación1/2
    print('El área del triángulo es: '+str(operación2)+" cm²")
elif opcion == "3":
    lado = float(input("ingrese un lado en m: "))
    operación1 = lado*lado
    print('El área del cuadrado es: '+str(operación1)+" cm²")
else:
    print("La opción que selecciono no existe :'v")