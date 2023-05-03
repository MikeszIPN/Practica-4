import cv2
import numpy as np

# Cargar imagenes
fondo = cv2.imread('Fotos/escritorio.jpg', 1)
sujeto = cv2.imread('Fotos/mouse.jpg', 1)
background = cv2.imread('Fotos/back.jpg', 1)

# Resta de imagenes
result = cv2.subtract(fondo, sujeto)

# Conversion a escala de grises
cv2.imwrite(
    "C:/Users/SZMik/OneDrive/Documentos/Mike/VisualStudio/Fotos/gray.jpg", result)
imgGray = cv2.imread('Fotos/gray.jpg', 0)
cv2.imwrite(
    "C:/Users/SZMik/OneDrive/Documentos/Mike/VisualStudio/Fotos/gray2.jpg", imgGray)
imgGray2 = cv2.imread('Fotos/gray2.jpg', 1)

# Conversion a binaria
_, imgBin = cv2.threshold(imgGray2, 15, 255, cv2.THRESH_BINARY)

# Mostrar binaria
cv2.imshow('Binaria', imgBin)

# Crear kernel
estructurante = np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
])

# Obtiene el tamaño de la imagen
forma = np.shape(imgBin)

# Llena una matriz del tamaño de la imagen con 0's
imgBin2 = np.zeros(forma)
imgBin3 = np.zeros(forma)
imgBin4 = np.zeros(forma)
imgBin5 = np.zeros(forma)
imgBin6 = np.zeros(forma)

# Convolucion 0R 1
for x in list(range(1, forma[0]-1)):
    for y in list(range(1, forma[1]-1)):
        suma = 0
        for i in list(range(-1, 2)):
            for j in list(range(-1, 2)):
                suma = imgBin[x-i, y-j] * estructurante[i+1, j+1]+suma
        imgBin2[x, y] = suma
maxs = np.max(imgBin2)
imgBin2 = imgBin2*255/maxs
imgBin2 = imgBin2.astype(np.uint8)

# Conversion a binaria
_, imgBin2 = cv2.threshold(imgBin2, 15, 255, cv2.THRESH_BINARY)

# Mostrar binaria
cv2.imshow('Binaria OR 1', imgBin2)

# Convolucion OR 2
for x in list(range(1, forma[0]-1)):
    for y in list(range(1, forma[1]-1)):
        suma = 0
        for i in list(range(-1, 2)):
            for j in list(range(-1, 2)):
                suma = imgBin2[x-i, y-j] * estructurante[i+1, j+1]+suma
        imgBin3[x, y] = suma
maxs = np.max(imgBin3)
imgBin3 = imgBin3*255/maxs
imgBin3 = imgBin3.astype(np.uint8)

# Conversion a binaria
_, imgBin3 = cv2.threshold(imgBin3, 15, 255, cv2.THRESH_BINARY)

# Mostrar binaria
cv2.imshow('Binaria OR 2', imgBin3)

# Inversa de binaria
for i in np.nditer(imgBin3, op_flags=['readwrite']): # type: ignore
    i[...] = 255 - i # type: ignore

# Mostrar binaria invertida
cv2.imshow('Binaria OR 2 REVERSE', imgBin3)

# Convolucion AND 1
for x in list(range(1, forma[0]-1)):
    for y in list(range(1, forma[1]-1)):
        suma = 0
        for i in list(range(-1, 2)):
            for j in list(range(-1, 2)):
                suma = imgBin3[x-i, y-j] * estructurante[i+1, j+1]+suma
        imgBin4[x, y] = suma
maxs = np.max(imgBin4)
imgBin4 = imgBin4*255/maxs
imgBin4 = imgBin4.astype(np.uint8)

# Conversion a binaria
_, imgBin4 = cv2.threshold(imgBin4, 15, 255, cv2.THRESH_BINARY)

# Mostrar binaria
cv2.imshow('Binaria AND 1', imgBin4)

# Convolucion AND 2
for x in list(range(1, forma[0]-1)):
    for y in list(range(1, forma[1]-1)):
        suma = 0
        for i in list(range(-1, 2)):
            for j in list(range(-1, 2)):
                suma = imgBin4[x-i, y-j] * estructurante[i+1, j+1]+suma
        imgBin5[x, y] = suma
maxs = np.max(imgBin5)
imgBin5 = imgBin5*255/maxs
imgBin5 = imgBin5.astype(np.uint8)

# Conversion a binaria
_, imgBin5 = cv2.threshold(imgBin5, 15, 255, cv2.THRESH_BINARY)

# Mostrar binaria
cv2.imshow('Binaria AND 2', imgBin5)

# Convolucion AND 3
for x in list(range(1, forma[0]-1)):
    for y in list(range(1, forma[1]-1)):
        suma = 0
        for i in list(range(-1, 2)):
            for j in list(range(-1, 2)):
                suma = imgBin5[x-i, y-j] * estructurante[i+1, j+1]+suma
        imgBin6[x, y] = suma
maxs = np.max(imgBin5)
imgBin6 = imgBin6*255/maxs
imgBin6 = imgBin6.astype(np.uint8)

# Conversion a binaria
_, imgBin6 = cv2.threshold(imgBin6, 15, 255, cv2.THRESH_BINARY)

# Mostrar binaria
cv2.imshow('Binaria AND 3', imgBin6)

# Inversa de binaria FINAL
for i in np.nditer(imgBin6, op_flags=['readwrite']): # type: ignore
    i[...] = 255 - i # type: ignore

# Mostrar binaria
cv2.imshow('Binaria AND 3 REVERSE', imgBin6)

# AND (A & U) = masked1 ########################### ORIGINAL
masked1 = cv2.bitwise_and(imgBin, sujeto)
# AND (A & U) = masked1 ########################### NUEVA
masked12 = cv2.bitwise_and(imgBin6, sujeto)

# Inversa de binaria ############################## ORIGINAL
for i in np.nditer(imgBin, op_flags=['readwrite']): # type: ignore
    i[...] = 255 - i # type: ignore
# Inversa de binaria ############################## NUEVA
for i in np.nditer(imgBin6, op_flags=['readwrite']): # type: ignore
    i[...] = 255 - i # type: ignore


# AND (F & ~U) = masked2 ################################ ORIGINAL
masked2 = cv2.bitwise_and(imgBin, background)
# AND (F & ~U) = masked2 ################################ NUEVA
masked22 = cv2.bitwise_and(imgBin6, background)


# OR (masked 1 OR masked 2) = masked3 ############################# ORIGINAL
masked3 = cv2.bitwise_or(masked1, masked2)
# OR (masked 1 OR masked 2) = masked3 ############################# NUEVA
masked32 = cv2.bitwise_or(masked12, masked22)

# Mostrar resultado final ############### ORIGINAL
cv2.imshow('FINAL', masked3)
# Mostrar resultado final ############### NUEVA
cv2.imshow('FINAL2', masked32)

# Mostrar y mantener pantallas
cv2.waitKey(0)
cv2.destroyAllWindows()
