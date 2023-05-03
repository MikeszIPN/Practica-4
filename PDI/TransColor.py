import cv2
import numpy as np

# Carga la imagen
original = cv2.imread('Fotos/LAB.jpg', 1)

# Mostrar imagen original
cv2.imshow('Imagen original', original)

# Separar las imagenes en 3 canales
B, G, R = cv2.split(original)

# Convertir cada canal en arreglo
ArrayR = np.asarray(R)
ArrayG = np.asarray(G)
ArrayB = np.asarray(B)

# Hacer las operaciones en cada arreglo para el gris preciso
for i in np.nditer(ArrayR, op_flags=['readwrite']):
    i[...] = i[...] * 0.21

for i in np.nditer(ArrayG, op_flags=['readwrite']):
    i[...] = i[...] * 0.72

for i in np.nditer(ArrayB, op_flags=['readwrite']):
    i[...] = i[...] * 0.07

# Sumar los 3 canales
suma1 = cv2.add(R, G)
suma2 = cv2.add(suma1, B)

# Guardar la imagen sumada y abrirla en 3 canales
cv2.imwrite(
    "C:/Users/SZMik/OneDrive/Documentos/Mike/VisualStudio/Fotos/suma2.jpg", suma2)
gray = cv2.imread('Fotos/suma2.jpg', 1)

# Mostrar la imagen en gris
cv2.imshow('Imagen gris', gray)

# Leer los valores de vr, vg y vb
vr = input('¿Cual es el valor en R?')
vg = input('¿Cual es el valor en G?')
vb = input('¿Cual es el valor en B?')
central = input('¿Cual es el punto central?')
vr = int(vr)
vg = int(vg)
vb = int(vb)
central = int(central)

# Separar las imagenes en 3 canales
b, g, r = cv2.split(gray)

# Convertir cada canal en un arreglo
ArrayGR = np.asarray(r)
ArrayGG = np.asarray(g)
ArrayGB = np.asarray(b)

# Hacer las operaciones en cada arreglo de acuerdo a la formula de la transformacion de color
for i in np.nditer(ArrayGR, op_flags=['readwrite']):
    if (i < central):
        i[...] = (vr * i[...])/central
    else:
        i[...] = vr + ((255 - vr) * (i[...] - central)) / central

for i in np.nditer(ArrayGG, op_flags=['readwrite']):
    if (i < central):
        i[...] = (vg * i[...])/central
    else:
        i[...] = vg + ((255 - vg) * (i[...] - central)) / central

for i in np.nditer(ArrayGB, op_flags=['readwrite']):
    if (i < central):
        i[...] = (vb * i[...])/central
    else:
        i[...] = vb + ((255 - vb) * (i[...] - central)) / central

# Muestra las imagenes modificadas en tonos de grises
cv2.imshow('Imagen r', ArrayGR)
cv2.imshow('Imagen g', ArrayGG)
cv2.imshow('Imagen b', ArrayGB)

# Sumar los 3 canales
final = cv2.merge([ArrayGR, ArrayGG, ArrayGB])

# Mostrar la imagen final
cv2.imshow('Imagen final', final)

# Esperar pantalla
cv2.waitKey(0)
cv2.destroyAllWindows()
