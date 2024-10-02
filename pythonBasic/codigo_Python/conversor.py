def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuantos pesos " + tipo_pesos + " tenes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tenes U$D" + dolares + " dolares")

menu = """
Bienvenido al conversor de monedas 

1 - pesos colombianos
2 - pesos argentinos
3 - pesos mexicanos

Elije una opcion: """ #triples comillas para string de varias lineas

opcion = int(input(menu))# creo variable con un input, que le lleve al string de varias lineas

if opcion == 1:# despues de los : y hasta justo antes del elif, tengo lo que se conoce como un bloque de codigo
    conversor("colombianos", 3898.12)
 
elif opcion == 2:
    conversor("argentinos", 214)

elif opcion == 3:
    conversor("mexicanos", 20.35)
else:
    print("Ingrese un valor valido")

    

# pesos = input("¿Cuantos pesos tenes?")
# pesos = float(pesos)
# valor_dolar = 210
# dolares = pesos / valor_dolar
# dolares = round(dolares, 2)
# dolares = str(dolares)
# print("Tenes U$D" + dolares + "dolares")