from flask import Flask, render_template, request

app = Flask(__name__)

# --- Algoritmo César ---
def cifrado_cesar_visual(texto, desplazamiento):
    resultado = ""
    log = []
    for caracter in texto:
        if caracter.isalpha():
            base = ord('A') if caracter.isupper() else ord('a')
            original_pos = ord(caracter) - base
            nueva_pos = (original_pos + desplazamiento) % 26
            nueva_letra = chr(nueva_pos + base)
            log.append(f"'{caracter}' ({original_pos}) + {desplazamiento} -> {nueva_pos} -> '{nueva_letra}'")
            resultado += nueva_letra
        else:
            log.append(f"'{caracter}' no es letra, se mantiene igual.")
            resultado += caracter
    return resultado, log

# --- Algoritmo Vigenère ---
def generar_clave(texto, clave):
    clave_generada = []
    indice = 0
    for i in range(len(texto)):
        if texto[i].isalpha():
            clave_generada.append(clave[indice % len(clave)])
            indice += 1
        else:
            clave_generada.append(" ")
    return "".join(clave_generada)

def cifrar_vigenere(texto, clave):
    clave_ext = generar_clave(texto, clave)
    resultado = []
    log = []
    for i in range(len(texto)):
        char = texto[i]
        clave_char = clave_ext[i]
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            desplazamiento = ord(clave_char.lower()) - ord('a')
            cifrado = chr((ord(char) - base + desplazamiento) % 26 + base)
            resultado.append(cifrado)
            log.append(f"{char} + {clave_char} -> desplazamiento {desplazamiento} -> {cifrado}")
        else:
            resultado.append(char)
            log.append(f"{char} no es letra, se mantiene igual")
    return "".join(resultado), log

def descifrar_vigenere(texto, clave):
    clave_ext = generar_clave(texto, clave)
    resultado = []
    log = []
    for i in range(len(texto)):
        char = texto[i]
        clave_char = clave_ext[i]
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            desplazamiento = ord(clave_char.lower()) - ord('a')
            descifrado = chr((ord(char) - base - desplazamiento + 26) % 26 + base)
            resultado.append(descifrado)
            log.append(f"{char} - {clave_char} -> desplazamiento {desplazamiento} -> {descifrado}")
        else:
            resultado.append(char)
            log.append(f"{char} no es letra, se mantiene igual")
    return "".join(resultado), log

# --- Algoritmo Playfair ---
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
    return matriz_5x5

def preparar_pares(texto):
    texto = texto.upper().replace("J", "I")
    texto = ''.join(filter(str.isalpha, texto))
    pares = []
    i = 0
    while i < len(texto):
        a = texto[i]
        b = ''
        if i + 1 < len(texto):
            b = texto[i + 1]
            if a == b:
                b = 'X'
                i += 1
            else:
                i += 2
        else:
            b = 'X'
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
        c1 = matriz[fila_a][(col_a + 1) % 5]
        c2 = matriz[fila_b][(col_b + 1) % 5]
        return c1 + c2
    elif col_a == col_b:
        c1 = matriz[(fila_a + 1) % 5][col_a]
        c2 = matriz[(fila_b + 1) % 5][col_b]
        return c1 + c2
    else:
        c1 = matriz[fila_a][col_b]
        c2 = matriz[fila_b][col_a]
        return c1 + c2

def cifrar_playfair(texto, clave):
    matriz = crear_matriz_clave(clave)
    pares = preparar_pares(texto)
    texto_cifrado = ""
    for par in pares:
        texto_cifrado += cifrar_par(par, matriz)
    return texto_cifrado

# Descifrado César (inversa del cifrado)
def descifrado_cesar_visual(texto, desplazamiento):
    return cifrado_cesar_visual(texto, -desplazamiento)

# Descifrado Playfair
def descifrar_playfair(texto, clave):
    matriz = crear_matriz_clave(clave)
    pares = [(texto[i], texto[i+1]) for i in range(0, len(texto), 2)]
    texto_descifrado = ""
    for a, b in pares:
        fila_a, col_a = buscar_posicion(a, matriz)
        fila_b, col_b = buscar_posicion(b, matriz)
        if fila_a == fila_b:
            c1 = matriz[fila_a][(col_a - 1) % 5]
            c2 = matriz[fila_b][(col_b - 1) % 5]
        elif col_a == col_b:
            c1 = matriz[(fila_a - 1) % 5][col_a]
            c2 = matriz[(fila_b - 1) % 5][col_b]
        else:
            c1 = matriz[fila_a][col_b]
            c2 = matriz[fila_b][col_a]
        texto_descifrado += c1 + c2
    return texto_descifrado

# --- Funciones para Kasiski ---
def limpiar_texto(texto):
    return ''.join(c.upper() for c in texto if c.isalpha())

def encontrar_repeticiones(texto, longitud_min=3):
    repeticiones = {}
    for i in range(len(texto) - longitud_min + 1):
        subcadena = texto[i:i+longitud_min]
        for j in range(i + 1, len(texto) - longitud_min + 1):
            if texto[j:j+longitud_min] == subcadena:
                if subcadena not in repeticiones:
                    repeticiones[subcadena] = []
                repeticiones[subcadena].append(j - i)
    return repeticiones

def obtener_factores(n):
    return [i for i in range(2, n + 1) if n % i == 0]

def kasiski_examination(texto, longitud_min=3):
    repeticiones = encontrar_repeticiones(texto, longitud_min)
    posibles_longitudes = {}
    for distancias in repeticiones.values():
        for distancia in distancias:
            for factor in obtener_factores(distancia):
                posibles_longitudes[factor] = posibles_longitudes.get(factor, 0) + 1
    return sorted(posibles_longitudes.items(), key=lambda x: x[1], reverse=True)

def dividir_en_grupos(texto, clave_len):
    return [texto[i::clave_len] for i in range(clave_len)]

def letra_mas_frecuente(texto):
    frecuencias = {}
    for letra in texto:
        frecuencias[letra] = frecuencias.get(letra, 0) + 1
    return max(frecuencias, key=frecuencias.get)

def deducir_clave(grupos):
    clave = ""
    letra_esperada = 'E'  # Más frecuente en español
    for grupo in grupos:
        letra = letra_mas_frecuente(grupo)
        desplazamiento = (ord(letra) - ord(letra_esperada)) % 26
        clave += chr(ord('A') + desplazamiento)
    return clave

def descifrar_vigenere_kasiski(texto, clave):
    texto_limpio = limpiar_texto(texto)
    clave_repetida = (clave * (len(texto_limpio) // len(clave) + 1))[:len(texto_limpio)]
    descifrado = ""
    for i in range(len(texto_limpio)):
        t = ord(texto_limpio[i]) - ord(clave_repetida[i])
        descifrado += chr((t % 26) + ord('A'))
    return descifrado

# --- Rutas Flask ---
@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    log = []
    error = None
    clave = None
    longitudes = None
    mensaje = None

    if request.method == "POST":
        algoritmo = request.form.get("algoritmo")

        if algoritmo == "cesar":
            texto = request.form.get("texto", "")
            desplazamiento = request.form.get("desplazamiento", "")
            accion = request.form.get("accion", "cifrar")

            try:
                d = int(desplazamiento)
                if accion == "cifrar":
                    resultado, log = cifrado_cesar_visual(texto, d)
                else:
                    resultado, log = descifrado_cesar_visual(texto, d)
            except ValueError:
                error = "Desplazamiento inválido."

        elif algoritmo == "vigenere":
            texto = request.form.get("texto", "")
            clave = request.form.get("clave", "")
            accion = request.form.get("accion", "cifrar")

            if not clave.isalpha():
                error = "La clave debe contener solo letras para Vigenère."
            else:
                if accion == "cifrar":
                    resultado, log = cifrar_vigenere(texto, clave)
                else:
                    resultado, log = descifrar_vigenere(texto, clave)

        elif algoritmo == "playfair":
            texto = request.form.get("texto", "")
            clave = request.form.get("clave", "")
            accion = request.form.get("accion", "cifrar")

            if not clave.isalpha():
                error = "La clave debe contener solo letras para Playfair."
            else:
                if accion == "cifrar":
                    resultado = cifrar_playfair(texto, clave)
                    log.append("Texto cifrado con Playfair generado.")
                else:
                    resultado = descifrar_playfair(texto, clave)
                    log.append("Texto descifrado con Playfair generado.")

        elif algoritmo == "kasiski":
            mensaje = request.form.get("mensaje", "")
            texto_limpio = limpiar_texto(mensaje)
            resultados = kasiski_examination(texto_limpio)
            if resultados:
                longitudes = resultados[:5]
                clave_len = resultados[0][0]
                grupos = dividir_en_grupos(texto_limpio, clave_len)
                clave = deducir_clave(grupos)
                resultado = descifrar_vigenere_kasiski(mensaje, clave)
            else:
                resultado = "❌ No se encontraron repeticiones útiles para aplicar el método de Kasiski."

        else:
            error = "Algoritmo no válido."

    return render_template("index.html", resultado=resultado, log=log, error=error, clave=clave, longitudes=longitudes, mensaje=mensaje)

if __name__ == "__main__":
    app.run(debug=True)
