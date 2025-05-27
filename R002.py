palabra1=input('p1  ')
palabra2=input('p2  ')


def son_anagramas(palabra1, palabra2):
    if palabra1 == palabra2:
        return False
    
    # Convertir las palabras a listas de letras, ordenarlas y compararlas
    return sorted(palabra1) == sorted(palabra2)

print(son_anagramas(palabra1,palabra2))

'''
sorted(palabra1) y sorted(palabra2) crean listas de caracteres
ordenados de palabra1 y palabra2, respectivamente.
'''