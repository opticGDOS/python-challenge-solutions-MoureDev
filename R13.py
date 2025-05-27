def palindromo(texto):
    texto = texto.replace(",", "").replace(".", "").replace(" ", "")
    texto = texto.lower()
    texto_invertido = texto[::-1]
    if texto == texto_invertido:
        return True
    else:
        return False

print(palindromo('Hola, mundo. Esto es una prueba.'))
print(palindromo('Ana lleva al oso la avellana'))