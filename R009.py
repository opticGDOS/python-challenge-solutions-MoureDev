def convertir_binario(numero):
    numero = int(numero)
    if numero == 0:
        return "0"
    binario = []

    while numero > 0:
        residuo = numero % 2
        binario.insert(0, str(residuo))
        numero = numero // 2
    return ''.join(binario)


numero = input('Número a convertir: ')
print('Número binario:', convertir_binario(numero))