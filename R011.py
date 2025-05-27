def esta_equilibrado(expresion):
    pila = []
    pares = {')': '(', ']': '[', '}': '{'}

    for caracter in expresion:
        if caracter in '([{':
            pila.append(caracter)
        elif caracter in ')]}':
            if not pila or pila[-1] != pares[caracter]:
                return False
            pila.pop()

    return not pila

# Pedir la expresión al usuario
expresion_usuario = input("Introduce una expresión con (), {}, []: ")

if esta_equilibrado(expresion_usuario):
    print("La expresión está equilibrada.")
else:
    print("La expresión NO está equilibrada.")
