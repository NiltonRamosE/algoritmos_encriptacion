# ======================
# Funciones auxiliares
# ======================
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
    for secuencia, distancias in repeticiones.items():
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
    letra_esperada = 'E'  # Suponemos que 'E' es la más frecuente en español
    for grupo in grupos:
        letra = letra_mas_frecuente(grupo)
        desplazamiento = (ord(letra) - ord(letra_esperada)) % 26
        clave += chr(ord('A') + desplazamiento)
    return clave

def descifrar_vigenere(texto, clave):
    descifrado = ""
    clave_repetida = (clave * (len(texto) // len(clave) + 1))[:len(texto)]
    for i in range(len(texto)):
        t = ord(texto[i]) - ord(clave_repetida[i])
        descifrado += chr((t % 26) + ord('A'))
    return descifrado

# ======================
# Programa principal
# ======================
texto_usuario = input("🔐 Ingresa el mensaje cifrado: ")
texto_limpio = limpiar_texto(texto_usuario)

# Paso 1: Método de Kasiski
print("\n🔎 Aplicando análisis de Kasiski...")
resultados = kasiski_examination(texto_limpio)
if not resultados:
    print("❌ No se encontraron repeticiones útiles.")
    exit()

print("\n📊 Posibles longitudes de la clave:")
for longitud, frecuencia in resultados[:10]:
    print(f"➡ Longitud: {longitud} - Frecuencia: {frecuencia}")

# Paso 2: Elegimos automáticamente la longitud con mayor frecuencia
clave_len = resultados[0][0]
print(f"\n🧩 Usando automáticamente la longitud de clave con mayor frecuencia: {clave_len}")

# Paso 3: Análisis de frecuencia
grupos = dividir_en_grupos(texto_limpio, clave_len)
clave_deducida = deducir_clave(grupos)
print(f"\n🔐 Clave deducida: {clave_deducida}")

# Paso 4: Descifrado
mensaje_descifrado = descifrar_vigenere(texto_limpio, clave_deducida)
print(f"\n📥 Mensaje descifrado:\n{mensaje_descifrado}")
