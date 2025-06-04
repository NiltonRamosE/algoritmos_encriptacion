def cifrado_cesar_visual(texto, desplazamiento):
    resultado = ""
    print("\nProceso de cifrado:\n")

    for caracter in texto:
        #isalpha() comprueba que el caracter pertenece al alfabeto
        if caracter.isalpha():
            #ord() convierte el valor a su código ASCII
            base = ord('A') if caracter.isupper() else ord('a')
            original_pos = ord(caracter) - base
            #aplicamos el módulo para que no supere las letras del alfabeto
            nueva_pos = (original_pos + desplazamiento) % 26
            #chr() convierte el número a su carácter correspondiente
            nueva_letra = chr(nueva_pos + base)

            print(f"'{caracter}' -> posición {original_pos} + {desplazamiento} -> {nueva_pos} -> '{nueva_letra}'")

            resultado += nueva_letra
        else:
            print(f"'{caracter}' no es letra, se mantiene igual.")
            resultado += caracter

    return resultado

mensaje = input("Ingresa el mensaje a cifrar: ")
while True:
    try:
        desplazamiento = int(input("Ingresa el desplazamiento (número entero): "))
        break
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

mensaje_cifrado = cifrado_cesar_visual(mensaje, desplazamiento)
print("\nMensaje cifrado final:", mensaje_cifrado)
