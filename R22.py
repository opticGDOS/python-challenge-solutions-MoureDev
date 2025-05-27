import requests

def procesar_calculadora_desde_url(url):
    try:
        # Realizamos una solicitud HTTP GET para obtener el contenido del archivo
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Lanza una excepción si la solicitud fue incorrecta

        # Dividimos el contenido en líneas y eliminamos líneas vacías
        lineas = [linea.strip() for linea in respuesta.text.splitlines() if linea.strip() != '']

        # Verificamos que haya al menos tres líneas y que el número total de líneas sea impar
        if len(lineas) < 3 or len(lineas) % 2 == 0:
            raise ValueError("Formato inválido: número de líneas incorrecto.")

        # Intentamos convertir el primer número
        resultado = float(lineas[0])

        # Iteramos de dos en dos: operador y luego número
        for i in range(1, len(lineas), 2):
            operador = lineas[i]
            try:
                numero = float(lineas[i + 1])
            except ValueError:
                raise ValueError(f"Número inválido en la línea {i + 2}: '{lineas[i + 1]}'")

            if operador == '+':
                resultado += numero
            elif operador == '-':
                resultado -= numero
            elif operador == '*':
                resultado *= numero
            elif operador == '/':
                if numero == 0:
                    raise ZeroDivisionError("División entre cero.")
                resultado /= numero
            else:
                raise ValueError(f"Operador inválido en la línea {i + 1}: '{operador}'")

        print(f"Resultado: {resultado}")

    except Exception as e:
        print("No se han podido resolver las operaciones.")
        print(f"Error: {e}")

# URL del archivo Challenge21.txt en GitHub
url = "https://raw.githubusercontent.com/mouredev/Weekly-Challenge-2022-Kotlin/main/app/src/main/java/com/mouredev/weeklychallenge2022/Challenge21.txt"

# Llamada a la función con la URL
procesar_calculadora_desde_url(url)
