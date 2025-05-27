import asyncio  # Importamos asyncio para usar programación asíncrona

# Función asíncrona que suma dos números después de esperar 'segundos' segundos
async def sumar_con_retardo(a, b, segundos):
    # Espera asíncrona sin bloquear el programa principal
    await asyncio.sleep(segundos)
    
    resultado = a + b  # Calcula la suma
    # Imprime el resultado justo cuando termina la espera
    print(f"Suma de {a} + {b} después de {segundos} segundos es: {resultado}")
    return resultado  # Devuelve el resultado

async def main():
    # Creamos tareas para ejecutar varias sumas en "paralelo"
    # asyncio.create_task lanza cada función sin esperar a que termine inmediatamente
    tareas = [
        asyncio.create_task(sumar_con_retardo(5, 3, 2)),   # Espera 2 segundos
        asyncio.create_task(sumar_con_retardo(10, 20, 1)), # Espera 1 segundo
        asyncio.create_task(sumar_con_retardo(7, 8, 3))    # Espera 3 segundos
    ]

    # Aquí podrías hacer otras cosas mientras las sumas están "durmiendo"
    
    # Esperamos que todas las tareas terminen para que el programa no se cierre antes
    await asyncio.gather(*tareas)

# Ejecuta la función principal en el event loop de asyncio
asyncio.run(main())
