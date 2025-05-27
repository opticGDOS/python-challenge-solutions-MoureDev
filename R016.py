from datetime import datetime

def dias_entre_fechas(fecha1: str, fecha2: str) -> int:
    formato = "%d/%m/%Y"  # Define el formato esperado: día/mes/año
    try:
        # Convertimos las cadenas de texto a objetos de fecha (datetime)
        f1 = datetime.strptime(fecha1, formato)
        f2 = datetime.strptime(fecha2, formato)
        
        # Calculamos la diferencia en días y devolvemos el valor absoluto
        return abs((f1 - f2).days)
    except ValueError as e:
        # Si alguna de las fechas no tiene el formato correcto o es inválida (como 31/02/2023), se lanza un error
        raise ValueError(f"Error: una de las fechas no es válida. Detalle: {e}")

# ----------- Programa principal con input -----------

# Pedimos las fechas al usuario
fecha1 = input("Introduce la primera fecha (dd/MM/yyyy): ")
fecha2 = input("Introduce la segunda fecha (dd/MM/yyyy): ")

try:
    resultado = dias_entre_fechas(fecha1, fecha2)
    print(f"La diferencia entre las fechas es de {resultado} días.")
except ValueError as error:
    print(error)
