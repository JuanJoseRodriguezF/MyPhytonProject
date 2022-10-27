precio = float(input("Ingrese precio del producto: "))
iva = precio*0.21 #21/100
precio_final = precio+iva
print("El precio final del producto con IVA incluido es: "+str(precio_final)+" pesos")