def crear_matriz_clave(clave):
    clave = clave.upper().replace("J", "I")
    matriz = []
    usada = set()

    for letra in clave:
        if letra not in usada and letra.isalpha():
            matriz.append(letra)
            usada.add(letra)

    for letra in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # Sin la J
        if letra not in usada:
            matriz.append(letra)

    matriz_5x5 = [matriz[i:i + 5] for i in range(0, 25, 5)]
    print("\nMatriz clave 5x5:")
    for fila in matriz_5x5:
        print(' '.join(fila))
    return matriz_5x5

def preparar_pares(texto):
    texto = texto.upper().replace("J", "I")
    texto = ''.join(filter(str.isalpha, texto))
    pares = []
    i = 0

    print("\nPreparando pares de letras:")
    while i < len(texto):
        a = texto[i]
        b = ''
        if i + 1 < len(texto):
            b = texto[i + 1]
            if a == b:
                b = 'X'
                print(f"Par detectado con letras repetidas: '{a}{a}', se cambia a '{a}X'")
                i += 1
            else:
                print(f"Par: {a}{b}")
                i += 2
        else:
            b = 'X'
            print(f"Última letra sin pareja: '{a}', se añade 'X' para formar par '{a}X'")
            i += 1
        pares.append((a, b))
    return pares

def buscar_posicion(letra, matriz):
    for fila in range(5):
        for col in range(5):
            if matriz[fila][col] == letra:
                return fila, col
    return None

def cifrar_par(par, matriz):
    a, b = par
    fila_a, col_a = buscar_posicion(a, matriz)
    fila_b, col_b = buscar_posicion(b, matriz)

    if fila_a == fila_b:
        # misma fila
        c1 = matriz[fila_a][(col_a + 1) % 5]
        c2 = matriz[fila_b][(col_b + 1) % 5]
        print(f"Par '{a}{b}' -> misma fila {fila_a}: '{a}' en col {col_a}, '{b}' en col {col_b}")
        print(f"Se cifran con las letras a la derecha: '{c1}{c2}'")
        return c1 + c2
    elif col_a == col_b:
        # misma columna
        c1 = matriz[(fila_a + 1) % 5][col_a]
        c2 = matriz[(fila_b + 1) % 5][col_b]
        print(f"Par '{a}{b}' -> misma columna {col_a}: '{a}' en fila {fila_a}, '{b}' en fila {fila_b}")
        print(f"Se cifran con las letras debajo: '{c1}{c2}'")
        return c1 + c2
    else:
        # rectángulo
        c1 = matriz[fila_a][col_b]
        c2 = matriz[fila_b][col_a]
        print(f"Par '{a}{b}' -> forma rectángulo:")
        print(f"'{a}' en ({fila_a},{col_a}), '{b}' en ({fila_b},{col_b})")
        print(f"Se cifran intercambiando columnas: '{c1}{c2}'")
        return c1 + c2

def cifrar_playfair(texto, clave):
    matriz = crear_matriz_clave(clave)
    pares = preparar_pares(texto)
    texto_cifrado = ""

    print("\nCifrado paso a paso:")
    for par in pares:
        texto_cifrado += cifrar_par(par, matriz)

    return texto_cifrado

if __name__ == "__main__":
    clave = input("Ingrese la clave para el cifrado Playfair: ")
    texto = input("Ingrese el texto a cifrar: ")

    cifrado = cifrar_playfair(texto, clave)
    print("\nTexto cifrado final:", cifrado)
