import string

texto = ("El sol brilla en el cielo, y el sol ilumina todo lo que toca. La gente se siente feliz cuando el sol aparece, "
         "porque el sol trae calor y energía. Sin embargo, no todos disfrutan del sol, pues el sol puede ser muy fuerte "
         "durante el mediodía.").lower()



def contador(texto):
    texto = texto.translate(str.maketrans('', '', string.punctuation))
    palabras = texto.split()
    recuento = {}  # Diccionario para almacenar el conteo

    for palabra in palabras:
        if palabra in recuento:
            recuento[palabra] += 1
        else:
            recuento[palabra] = 1

    # Mostramos el recuento final
    for palabra, cantidad in recuento.items():
        print(f'La palabra "{palabra}" aparece {cantidad} veces.')
        
    total_palabras = len(palabras)
    print(f"\nTotal de palabras en el texto: {total_palabras}")

    

contador(texto)
