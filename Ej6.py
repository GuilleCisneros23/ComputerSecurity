def cifrar_cesar(mensaje, clave):
    mensaje_cifrado = ""
    for letra in mensaje:
        if letra.isalpha():
            if letra.isupper():               
                letra_cifrada = chr(((ord(letra) - ord('A') + clave) % 26) + ord('A'))
            elif letra.islower():
                letra_cifrada = chr(((ord(letra) - ord('a') + clave) % 26) + ord('a'))
        else:
            letra_cifrada = letra
        mensaje_cifrado += letra_cifrada
    return mensaje_cifrado



def descifrar_cesar(mensaje_cifrado, clave):
    return cifrar_cesar(mensaje_cifrado, -clave)



mensaje_original = "ynkooejcpdanqxeykjrbdofgkq"
clave = -4


mensaje_descifrado = descifrar_cesar(mensaje_original, clave)
print("Mensaje descifrado:", mensaje_descifrado)
