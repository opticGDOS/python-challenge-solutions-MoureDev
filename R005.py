def calcular_area(poligono, base, altura=None):
    if poligono == "triangulo":
        if altura is None:
            raise ValueError("El triángulo necesita base y altura.")
        return (base * altura) / 2
    elif poligono == "cuadrado":
        return base * base
    elif poligono == "rectangulo":
        if altura is None:
            raise ValueError("El rectángulo necesita base y altura.")
        return base * altura
    else:
        raise ValueError("Polígono no soportado.")

poligono=int((input('Escoge un poligono 1:Triangulo, 2:Cuadrado, 3:Rectangulo:')))

match poligono:
    case 1:
        base,altura=map(float,input('Ingrea la medida de la base y la altura:').split())
        print("Área del triángulo:", calcular_area("triangulo", base, altura))
    case 2:
        lado=float((input('Ingrea la medida de un lado:')))
        print("Área del cuadrado:", calcular_area("cuadrado", lado))
    case 3:
        base,altura=map(float,input('Ingrea la medida de la base y la altura:').split())
        print("Área del rectángulo:", calcular_area("rectangulo", base, altura))


        
        
        