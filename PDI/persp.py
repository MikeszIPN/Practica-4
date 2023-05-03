import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image

# Primera imagen
img = Image.open("Pics/cuadrado.jpg")

img_aux = np.copy(img)

# Tamaño de la imagen
wid, hght = img.size
print("Image size: " + str(wid) + "x" + str(hght))

cv2.imshow('Imagen',img)

# Mostrar y mantener pantallas
cv2.waitKey(0)
cv2.destroyAllWindows()