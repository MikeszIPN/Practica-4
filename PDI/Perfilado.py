import cv2
import numpy as np
import math

# Carga la imagen
Original = cv2.imread('Fotos/paris.jpeg', 1)

# Crear kernel's
sobelx = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])

sobely = np.array([
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]
])

laplaciana = np.array([
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]
])

perfilado = np.array([
    [0, -0.6, 0],
    [-0.6, 2.4, -0.6],
    [0, -0.6, 0]
])

forma = np.shape(Original)

sobelx2 = np.zeros(forma)
sobely2 = np.zeros(forma)
laplaciana2 = np.zeros(forma)
perfilado2 = np.zeros(forma)

# SobelX
for x in list(range(1, forma[0]-1)):
    for y in list(range(1, forma[1]-1)):
        suma = 0
        for i in list(range(-1, 2)):
            for j in list(range(-1, 2)):
                suma = Original[x-i, y-j] * sobelx[i+1, j+1]+suma
        sobelx2[x, y] = suma
maxs = np.max(sobelx2)
sobelx2 = sobelx2*255/maxs
sobelx2 = sobelx2.astype(np.uint8)

# SobelY
for x in list(range(1, forma[0]-1)):
    for y in list(range(1, forma[1]-1)):
        suma = 0
        for i in list(range(-1, 2)):
            for j in list(range(-1, 2)):
                suma = Original[x-i, y-j] * sobely[i+1, j+1]+suma
        sobely2[x, y] = suma
maxs = np.max(sobely2)
sobely2 = sobely2*255/maxs
sobely2 = sobely2.astype(np.uint8)

# Gradiente
alto, ancho, canal = Original.shape

def gradiente(img1, img2):
    gradiente2 = np.empty((alto, ancho, 3), np.uint8)
    for i in range(alto):
        for j in range(ancho):
            valor = math.sqrt((img1[i][j][0]**2)+(img2[i][j][0]**2))
            gradiente2[i][j][0] = valor
            gradiente2[i][j][1] = valor
            gradiente2[i][j][2] = valor
    return gradiente2

# Laplaciana
for x in list(range(1, forma[0]-1)):
    for y in list(range(1, forma[1]-1)):
        suma = 0
        for i in list(range(-1, 2)):
            for j in list(range(-1, 2)):
                suma = Original[x-i, y-j] * laplaciana[i+1, j+1]+suma
        laplaciana2[x, y] = suma
maxs = np.max(laplaciana2)
laplaciana2 = laplaciana2*255/maxs
laplaciana2 = laplaciana2.astype(np.uint8)

# Perfilado
for x in list(range(1, forma[0]-1)):
    for y in list(range(1, forma[1]-1)):
        suma = 0
        for i in list(range(-1, 2)):
            for j in list(range(-1, 2)):
                suma = Original[x-i, y-j] * perfilado[i+1, j+1]+suma
        perfilado2[x, y] = suma
maxs = np.max(perfilado2)
perfilado2 = perfilado2*255/maxs
perfilado2 = perfilado2.astype(np.uint8)

# Muestra las imagenes
cv2.imshow('Original', Original)
cv2.imshow('SobelX', sobelx2)
cv2.imshow('SobelY', sobely2)
cv2.imshow('Gradiente', gradiente(sobelx2, sobely2))
cv2.imshow('Laplaciana', laplaciana2)
cv2.imshow('Perfilado', perfilado2)

# Tiempo de espera para mostrar las imagenes
cv2.waitKey(0)
cv2.destroyAllWindows()