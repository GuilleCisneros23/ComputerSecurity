
ea_hex = "0x0345376e1e5406691d5c076c4050046e4000036a1a005c6b1904531d3941055d"
eb_hex = "0x0346303d1902033d1959003d1903553d1951553d1907593d1951511a3d190505"
pa_hex = "0x6161616161616161616161616161616161616161616161616161616161616161"

# La operación XOR con los tres resultados de flags
f_int = int(ea_hex, 16) ^ (int(pa_hex, 16) ^ int(eb_hex, 16))

# Resultado en hexadecimal
f_hex = '{:x}'.format(f_int)
print("El valor de flag en hexadecimal es:", f_hex)
# Valor hexadecimal a ASCII
f_ascii = bytes.fromhex(f_hex).decode('utf-8')
print("El valor de flag original es:", f_ascii)
