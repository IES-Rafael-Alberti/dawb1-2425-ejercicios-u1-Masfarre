capital = float(input("Introduce la cantidad de dinero depositada en la cuenta de ahorros: "))
interes = 0.04

for i in range(1, 4):
    capital *= (1 + interes)
    print("Los ahorros tras el año",i,"seran:",round(capital,2))