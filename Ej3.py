def descifrar_cadena(cadena):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    resultado = ''
    numeros = []

    # Extraemos los números de la cadena
    for caracter in cadena:
        if caracter.isdigit():
            resultado += caracter
        elif resultado:
            numeros.append(int(resultado))
            resultado = ''

    # Procesamos los números y construir el texto descifrado
    for numero in numeros:
        if 1 <= numero <= 26:
            letra = alfabeto[numero - 1]
            resultado += letra
        else:
            resultado += '?'
    
    return resultado

cadena = "16 9 3 15 3 20 6 {20 8 5 14 21 13 2 5 18 19 13 1 19 15 14}"
texto_descifrado = descifrar_cadena(cadena)
print(texto_descifrado)
