acciones = input().split()
pista_raw = input()
pista = list(pista_raw)

def carrera(acciones, pista):
    carrera_correcta = True  
    for accion, obstaculo in zip(acciones, pista):
        if (accion == "run" and obstaculo == "_") or (accion == "jump" and obstaculo == "|"):
            continue
        else:
            carrera_correcta = False  
            break  

    return print(carrera_correcta)

carrera(acciones,pista)

'''
run jump run jump run
_|_|_

'''