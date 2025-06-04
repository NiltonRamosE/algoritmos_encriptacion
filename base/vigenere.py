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

    print("\nProceso de cifrado:")
    for i in range(len(texto)):
        char = texto[i]
        clave_char = clave_ext[i]
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            desplazamiento = ord(clave_char.lower()) - ord('a')
            cifrado = chr((ord(char) - base + desplazamiento) % 26 + base)
            resultado.append(cifrado)
            print(f"{char} + {clave_char} -> ({ord(char)} - {base} + {desplazamiento}) % 26 + {base} = {cifrado}")
        else:
            resultado.append(char)
            print(f"{char} no es letra, se mantiene igual")

    return "".join(resultado)

def descifrar_vigenere(texto, clave):
    clave_ext = generar_clave(texto, clave)
    resultado = []

    print("\nProceso de descifrado:")
    for i in range(len(texto)):
        char = texto[i]
        clave_char = clave_ext[i]
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            desplazamiento = ord(clave_char.lower()) - ord('a')
            descifrado = chr((ord(char) - base - desplazamiento + 26) % 26 + base)
            resultado.append(descifrado)
            print(f"{char} - {clave_char} -> ({ord(char)} - {base} - {desplazamiento} + 26) % 26 + {base} = {descifrado}")
        else:
            resultado.append(char)
            print(f"{char} no es letra, se mantiene igual")

    return "".join(resultado)

mensaje = input("Ingrese el mensaje: ")
clave = input("Ingrese la clave: ")

mensaje_cifrado = cifrar_vigenere(mensaje, clave)
print("\nMensaje cifrado:", mensaje_cifrado)

mensaje_descifrado = descifrar_vigenere(mensaje_cifrado, clave)
print("\nMensaje descifrado:", mensaje_descifrado)
