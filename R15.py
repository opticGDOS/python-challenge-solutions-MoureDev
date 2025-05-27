numero = input()
potencia = len(numero)  # número de dígitos

def numero_narcisista(numero):
    suma = 0
    for digito in numero:
        suma += int(digito) ** potencia
    if suma == int(numero):
        return 'Es un número narcisista'
    else:
        return 'Es un número común'

print(numero_narcisista(numero))
1