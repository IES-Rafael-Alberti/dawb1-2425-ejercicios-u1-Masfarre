imp = float(input("Introduce el importe sin IVA: "))
iva = float(input("Introduce el tipo de IVA:  "))

print("El precio total + IVA es: ", imp + (imp * iva / 100))