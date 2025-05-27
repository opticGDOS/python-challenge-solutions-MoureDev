def fibonacci(n):
    numeros=[0,1]
    while len (numeros) < n:#comprobar que la longitud de la lista de numeros no sea mayor a 50
        nn=numeros[-1]+numeros[-2] #suma del ultimo y penultimo valor de la lista
        numeros.append(nn) # agregamos ese nuevo valor a lista
    return numeros

for i in fibonacci(50):
    print(i)