def mayus(string):
    palabra = list(string)
    palabra[0] = palabra[0].upper()
    resultado = ''.join(palabra)
    print(resultado)

string = input()
mayus(string)
