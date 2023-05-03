import cv2
import numpy as np

# Carga la imagen a color
Original = cv2.imread('Fotos/paris.jpeg', 1)

# Crear matriz de 5x5 llena de 1's y dividirla entre la suma (25)
media = np.ones((5, 5), np.float32)/25

# Convolusionar con matriz creada
img_media = cv2.filter2D(Original, -1, media)

# Crear kernel gaussiano
gauss = [
    [1, 4, 6, 4, 1],
    [4, 16, 24, 16, 4],
    [6, 24, 36, 24, 6],
    [4, 16, 24, 16, 4],
    [1, 4, 6, 4, 1]
]

# Dividir el kernel entre la suma (256)
gauss2 = np.divide(gauss, 256)

# Convolusionar la imagen con kernel gaussiano
img_gauss = cv2.filter2D(Original, -1, gauss2)

# Muestra las imagenes
cv2.imshow('Original', Original)
cv2.imshow('Media', img_media)
cv2.imshow('Gauss', img_gauss)

# Tiempo de espera para mostrar las imagenes
cv2.waitKey(0)
cv2.destroyAllWindows()
