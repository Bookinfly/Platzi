dolares = input("¿Cuantos dolares tenes?")
dolares = float(dolares)
valor_peso = 0.0045
pesos = dolares / valor_peso
pesos = round(pesos, 2)
pesos = str(pesos)
print("Tenes $" + pesos + "pesos")