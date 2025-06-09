def comparar_arrays(array1, array2, booleano):
    resultado = []
    
    for elemento in array1:
        if booleano==True:
            if elemento in array2 and elemento not in resultado:
                resultado.append(elemento)
        else:
            if elemento not in array2 and elemento not in resultado:
                resultado.append(elemento)

    for elemento in array2:
        if booleano != True:
            if elemento not in array1 and elemento not in resultado:
                resultado.append(elemento)

    return resultado

a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]

print(comparar_arrays(a, b, True))  
print(comparar_arrays(a, b, False)) 
