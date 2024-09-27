impt = int(input("Introduce el importe total de un articulo: "))

iva = (impt * 1.1)  / 10
imp = impt - iva

print("El importe sin iva es:",imp, "Y el iva es: ",  iva)