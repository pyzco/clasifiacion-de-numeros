import os

import cv2
from PIL import Image

carpeta = r"C:\Users\Sebastian Chipana\Desktop\PROYECTO-CS-2\Imagenes\NUMEROS RECORTADOS CON FORMATO REQUERIDO"

matrices_imagenes = {}

for archivo in os.listdir(carpeta):
    ruta_completa = os.path.join(carpeta, archivo)

    imagen_matriz = cv2.imread(ruta_completa)

    matrices_imagenes[archivo] = imagen_matriz

print(matrices_imagenes.keys())

