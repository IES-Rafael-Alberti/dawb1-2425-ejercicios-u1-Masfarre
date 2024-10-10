impt = float(input("Introduce el importe total de un articulo: "))

iva = (impt * 1.1)  / 10
imp = impt - iva

print("El importe sin iva es:",round(imp,2), "Y el iva es: ",  round(iva,2))