def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):  # Recorremos desde 2 hasta n-1
        if n % i == 0:  # Si es divisible, no es primo
            return False
    return True  # Si no tuvo divisores, es primo

# Imprimir los números primos del 1 al 100
for num in range(1, 101):
    if es_primo(num):
        print(num, end=" ")
