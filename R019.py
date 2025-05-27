def analizar_matriz(matriz):
    # Verificamos que la matriz sea 3x3
    if len(matriz) != 3 or any(len(fila) != 3 for fila in matriz):
        return "Nulo"

    # Contamos la cantidad de "X", "O" y vacíos
    contador_x = sum(fila.count("X") for fila in matriz)
    contador_o = sum(fila.count("O") for fila in matriz)
    vacios = sum(fila.count("") for fila in matriz)

    # Reglas del juego: X empieza, así que X nunca puede tener menos que O,
    # y no puede haber más de una diferencia entre ambos
    if contador_o > contador_x or contador_x - contador_o > 1:
        return "Nulo"

    # Función para revisar si alguien ha ganado
    def ha_ganado(simbolo):
        # Revisar filas
        for fila in matriz:
            if fila == [simbolo, simbolo, simbolo]:
                return True
        # Revisar columnas
        for col in range(3):
            if all(matriz[fila][col] == simbolo for fila in range(3)):
                return True
        # Revisar diagonales
        if all(matriz[i][i] == simbolo for i in range(3)):
            return True
        if all(matriz[i][2 - i] == simbolo for i in range(3)):
            return True
        return False

    gana_x = ha_ganado("X")
    gana_o = ha_ganado("O")

    # Si ganan los dos, es inválido (nulo)
    if gana_x and gana_o:
        return "Nulo"

    # Si gana uno solo, devolvemos el ganador
    if gana_x:
        return "X"
    if gana_o:
        return "O"

    # Si no ganó nadie, y no hay espacios vacíos, es empate
    if vacios == 0:
        return "Empate"

    # Si no ganó nadie pero aún hay espacios vacíos, el juego no ha terminado
    return "Empate"  # o podría ser "En curso" si quieres agregar ese estado

# Ejemplo de uso:
matriz = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["O", "X", "X"]
]

print(f'Gana {analizar_matriz(matriz)}')  # Output esperado: "X"
