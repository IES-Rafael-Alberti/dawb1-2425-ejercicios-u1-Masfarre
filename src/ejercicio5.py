imp = int(input("Introduce el importe sin IVA: "))
iva = int(input("Introduce el tipo de IVA:  "))

print("El precio total + IVA es: ", imp + (imp * iva / 100))