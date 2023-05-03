import cv2
import numpy as np

# Cargar imagenes
fondo = cv2.imread('Fotos/fondo.jpg', 1)
sujeto = cv2.imread('Fotos/sujeto.jpg', 1)
paris = cv2.imread('Fotos/paris.jpeg', 1)

# Mostrar imagenes
cv2.imshow('Sujeto', sujeto)
cv2.imshow('Fondo', fondo)
cv2.imshow('Paris', paris)

# Resta de imagenes
result = cv2.subtract(fondo, sujeto)
# Mostrar resta
cv2.imshow('Resta', result)

# Conversion a escala de grises
cv2.imwrite(
    "C:/Users/SZMik/OneDrive/Documentos/Mike/VisualStudio/Fotos/gray.jpg", result)
imgGray = cv2.imread('Fotos/gray.jpg', 0)
cv2.imwrite(
    "C:/Users/SZMik/OneDrive/Documentos/Mike/VisualStudio/Fotos/gray2.jpg", imgGray)
imgGray2 = cv2.imread('Fotos/gray2.jpg', 1)
# Mostrar escala de grises
cv2.imshow('GrayScale', imgGray2)

# Conversion a binaria
_, imgBin = cv2.threshold(imgGray2, 15, 255, cv2.THRESH_BINARY)
# Mostrar binaria
cv2.imshow('Binaria', imgBin)

# AND (A & U) = masked1
masked1 = cv2.bitwise_and(imgBin, sujeto)
# Mostrar masked1
cv2.imshow('MASKED1', masked1)

# Inversa de binaria
for i in np.nditer(imgBin, op_flags=['readwrite']):
    i[...] = 255 - i
    
# Mostrar binaria invertida
cv2.imshow('Binaria Invertida', imgBin)

# AND (F & ~U) = masked2
masked2 = cv2.bitwise_and(imgBin, paris)
# Mostrar masked2
cv2.imshow('MASKED2', masked2)

# OR (masked 1 OR masked 2) = masked3
masked3 = cv2.bitwise_or(masked1, masked2)
# Mostrar resultado final
cv2.imshow('FINAL', masked3)

# Mostrar y mantener pantallas
cv2.waitKey(0)
cv2.destroyAllWindows()
