def obtener_divisores(n):
    divisores = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisores.append(i)
    return divisores

def calcular_mcd(n1, n2):
    divisores1 = obtener_divisores(n1)
    divisores2 = obtener_divisores(n2)

    comunes = []
    for d in divisores1:
        if d in divisores2:
            comunes.append(d)

    return max(comunes)

def calcular_mcm(n1, n2):

    mcd = calcular_mcd(n1, n2)
    return (n1 * n2) // mcd

a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))

mcd = calcular_mcd(a, b)
mcm = calcular_mcm(a, b)

print(f"MCD de {a} y {b} es: {mcd}")
print(f"MCM de {a} y {b} es: {mcm}")
