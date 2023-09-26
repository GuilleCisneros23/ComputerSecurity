def ROT13Encrypt(mensaje):
    resultado = ""

    for letra in mensaje:
        if letra.isalpha():
            base = ord('a') if letra.islower() else ord('A')
            encriptado = chr(((ord(letra) - base + 13) % 26) + base)
            resultado += encriptado
        else:
            resultado += letra

    return resultado



def ROT13Decrypt(mensaje):
    resultado = ""

    for letra in mensaje:
        if letra.isalpha():
            base = ord('a') if letra.islower() else ord('A')
            encriptado = chr(((ord(letra) - base - 13 + 26) % 26) + base)
            resultado += encriptado
        else:
            resultado += letra

    return resultado


if __name__ == "__main__":
    resultado = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ}"
    print("Antes de Desencriptación")
    print(resultado)
    desencriptado = ROT13Decrypt(resultado)
    print("")
    print("Después de Desencriptación...")
    print(desencriptado)

