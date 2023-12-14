import os
from collections import Counter

directorio = 'C:/Users/guill/Downloads/public/public'

def calcular_frecuencia_letras(archivo):
    with open(archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()
        conteo_letras = Counter(caracter for caracter in contenido.lower() if caracter.isalpha())
    return conteo_letras



archivos_txt = [os.path.join(directorio, archivo) for archivo in os.listdir(directorio) if archivo.endswith('.txt')]

frecuencia_total = Counter()
for archivo in archivos_txt:
    frecuencia_archivo = calcular_frecuencia_letras(archivo)
    frecuencia_total += frecuencia_archivo

frecuencia_ordenada = sorted(frecuencia_total.items(), key=lambda x: x[1], reverse=True)

for letra, frecuencia in frecuencia_ordenada:
    print(f'Letra: {letra}, Frecuencia: {frecuencia}')
