import requests
from PIL import Image
from io import BytesIO
import math

def calcular_aspect_ratio(url):
    """
    Calcula el aspect ratio de una imagen descargada desde una URL.
    
    Args:
        url (str): URL de la imagen a procesar
    
    Returns:
        tuple: Una tupla con (ancho, alto, ratio en formato texto)
    """
    try:
        # Descargar la imagen desde la URL
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Lanzará un error si la descarga falla
        
        # Abrir la imagen desde la memoria
        imagen = Image.open(BytesIO(respuesta.content))
        
        # Obtener dimensiones
        ancho, alto = imagen.size
        
        # Calcular el máximo común divisor
        mcd = math.gcd(ancho, alto)
        
        # Calcular aspect ratio simplificado
        ratio_x = ancho // mcd
        ratio_y = alto // mcd
        
        # Formatear el ratio
        ratio_texto = f"{ratio_x}:{ratio_y}"
        
        return (ancho, alto, ratio_texto)
    
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar la imagen: {e}")
        return None
    except Exception as e:
        print(f"Error procesando la imagen: {e}")
        return None

# Ejemplo de uso
url_ejemplo = "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"
resultado = calcular_aspect_ratio(url_ejemplo)

if resultado:
    ancho, alto, ratio = resultado
    print(f"Dimensiones: {ancho}x{alto}")
    print(f"Aspect Ratio: {ratio}")