# TODOS ESTOS IMPORT SON DE LA CLASE EXCEPTO os XD

from sklearn.datasets import load_digits
import pandas as pd
import cv2
import numpy as np
import os

# IMPORTACION Y EXPORTACION
digits = load_digits()
data = pd.DataFrame(digits.data)
data["target"] = digits.target
data.to_excel("data.xlsx")

# TRANSOFRMAR IMAGEN A MATRIZ
carpeta = r"C:\Users\Sebastian Chipana\Desktop\PROYECTO-CS-2\Imagenes\NUMEROS RECORTADOS CON FORMATO REQUERIDO"

# DICCIONARIO USADO PARA GUARDAR UNA VEZ LAS IMAGENES PASADAS A MATRICES Y A 8x8
matrices_imagenes = {}

# BUCLE PARA NO HACERLO UNO POR UNO
for archivo in os.listdir(carpeta):
    ruta_completa = os.path.join(carpeta, archivo)

    # ESTO LO PASA A FONDO BLANCO Y LAPIZ NEGRO LUEGO LO SE INVIERTE EN EL SIGUIENTE FOR
    imagen_matriz = cv2.imread(ruta_completa, cv2.IMREAD_GRAYSCALE)
    imagen_reescalada = cv2.resize(imagen_matriz, (8,8))

    matrices_imagenes[archivo] = imagen_reescalada

# BUCLE PARA HACER TODAS LAS INVERSIONES DE UNA
for matriz_key in matrices_imagenes.keys():
    imagen_invertida = cv2.bitwise_not(matrices_imagenes[matriz_key])
    # AHORA PASANDO DE 0 A 16 XD
    imagen_normalizada = (imagen_invertida / 255.0 * 16).astype(int)
    # AHORA RECIEN INGRESAMOS XD
    matrices_imagenes[matriz_key] = imagen_normalizada

# CONVERSION A LISTAS PAPU :V XDDDD
lista_convertidos_a_lista = []
for matriz_key in matrices_imagenes.keys():
    lista_convertidos_a_lista.append(matrices_imagenes[matriz_key].flatten().astype(int))

# GUARDAMOS LAS DISTANCIAS AHORA XD OH MI LENTE DE CONTACTO
# OJO NO METEMOS TODO DE UNA PORQUE NO SABRIAMOS DE DONDE ES XD
# ABSTRACCION DE UNO A VARIOS PIENSA PE CHATO
distancias_por_imagen = []

# CODIGO COPIADO DEL PROFE XDD
dataset_imagenes = digits.data

# TODO ESTO ES PARA GUARDAR LAS DISTANCIAS POR NUMERITO PE PALA :V XD

for numerito in lista_convertidos_a_lista:
    distancia_de_imagen = []
    for i in range(1797):
        # TODO ESTE CODIGO ES COPIADO DE YARASCA XD
        imagen_dataset = dataset_imagenes[i]
        diferencia = numerito - imagen_dataset
        distancia = np.sqrt(np.sum(diferencia ** 2))

        distancia_de_imagen.append(distancia)

    distancias_por_imagen.append(distancia_de_imagen)

distancias_por_imagen = np.array(distancias_por_imagen)

# LINEA PA GUARDAR LOS MEJORES PE
seis_mas_cercanos = []

for distancia_de_un_numerito in distancias_por_imagen:
    # INDICES DE MENOR A MAYOR FAHHH
    indices_ordenados = np.argsort(distancia_de_un_numerito)

    # PA QUEDARNOS CON LOS 3 PRIMEROS
    tops_indices = indices_ordenados[0:10]

    seis_mas_cercanos.append(tops_indices)

print(seis_mas_cercanos)

etiquetas_reales = []
for archivo in matrices_imagenes.keys():
    etiqueta = int(archivo[0])
    etiquetas_reales.append(etiqueta)

etiquetas_reales = np.array(etiquetas_reales)

# IMPRIMIMOS LOS 3 DIGITOS MAS PARECIDOS A EL SAUUU
for i, top6_indices in enumerate(seis_mas_cercanos):
    top3_indices = top6_indices[0:3]
    targets_vecinos = digits.target[top3_indices]
    etiqueta_real = etiquetas_reales[i]

    print(f"IMAGEN {i+1} NUMERO REAL {etiqueta_real}")
    print(f"TARGETS MAS CERCANOS XD {targets_vecinos}")
    valores, conteos = np.unique(targets_vecinos, return_counts=True)
    max_conteo = np.max(conteos)


    # ESTO ES PA QUE DIGA MI MODELO PE XDD
    if max_conteo >= 2:
        numero_detectado = valores[np.argmax(conteos)]
        print(
            f"Soy la inteligencia artificial, y he detectado que el dígito ingresado corresponde al número {numero_detectado}")

    # LOL > DOTA 2
    else:
        targets_6_vecinos = digits.target[top6_indices]
        print(f"TARGETS MAS CERCANOS (top 10) {targets_6_vecinos}")
        valores6, conteos6 = np.unique(targets_6_vecinos, return_counts=True)
        numero_detectado = valores6[np.argmax(conteos6)]
        print(
            f"Soy la inteligencia artificial, y he detectado que el dígito ingresado corresponde al número {numero_detectado}")