import cv2
import numpy as np
from matplotlib import pyplot as plt

#Lectura de imagenes, img1 = grises, img2 =  colores
img1 = cv2.imread('bob.png', 0)
img2 = cv2.imread('bob.png', 1)

#Mostrar imagenes
cv2.imshow('Imagen1', img1)
cv2.imshow('Imagen2', img2)

#calcular histograma de imagen a color en azul, verde y rojo
histb=cv2.calcHist([img2], [0], None, [256], [0,256])
histg=cv2.calcHist([img2], [1], None, [256], [0,256])
histr=cv2.calcHist([img2], [2], None, [256], [0,256])

#Arreglo de 2x2
fig, ax=plt.subplots(2,2)

#Muestra los histogramas de las imagenes en el arreglo
ax[0,0].plot(histb, color ='b') # type: ignore
ax[0,0].set_title('histo_azul') # type: ignore

ax[0,1].plot(histg, color ='g') # type: ignore
ax[0,1].set_title('histo_verde') # type: ignore

ax[1,0].plot(histr, color ='r') # type: ignore
ax[1,0].set_title('histo_rojo') # type: ignore

ax[1,1].hist(img1.ravel (), 256, [0,256])# type: ignore
ax[1,1].set_title('histo_gris') # type: ignore

#Muestra el arreglo
plt.show()

#Mantiene las nuevas pantallas activas
cv2.waitKey(0)
cv2.destroyAllWindows()