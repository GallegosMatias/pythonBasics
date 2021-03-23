#Primer proyecto: Conversor de monedas

pesos = input("Cuántas copas tenés?: ")
pesos = float(pesos)
valor_dolar = 150
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print('Tenés ' + dolares + ' copas')