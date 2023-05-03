import cv2
import numpy as np
from matplotlib import pyplot as plt

# Carga la imagen
original = cv2.imread('LAB.jpg', 1)

# Mostrar imagen original
cv2.imshow('Imagen original', original)

# Convertir imagen a arreglo
imgArray = np.asarray(original)

# Menu
def mostrar_menu(opciones):
   print('Seleccione una opción:')
   for clave in sorted(opciones):
       print(f' {clave}) {opciones[clave][0]}')
       
def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()
    
def generar_menu(opciones):
    opcion = None    
    mostrar_menu(opciones)
    opcion = leer_opcion(opciones)
    ejecutar_opcion(opcion, opciones)
    print() # se imprime una línea en blanco para clarificar la salida por pantalla
        
def menu_principal():
    opciones = {
        '1': ('Suma', accion1),
        '2': ('Resta', accion2),
        '3': ('Multiplicacion', accion3),
        '4': ('Division', accion4),
        '5': ('Gamma', accion5),
        '6': ('Inversa', accion6),
        '7': ('Ecualizacion', accion7)
    }
    generar_menu(opciones)

def accion1():
    print('Has elegido suma')
    
    valor = input('¿Qué valor aplicamos?')
    valor = float (valor)
    
    for i in np.nditer(imgArray, op_flags=['readwrite']):
        if ((i + valor) > 255):
            i[...] = 255
        else:
            i[...] = i + valor
    salir()


def accion2():
    print('Has elegido resta')
    
    valor = input('¿Qué valor aplicamos?')
    valor = float (valor)
    
    for i in np.nditer(imgArray, op_flags=['readwrite']):
        if ((i - valor) < 0):
            i[...] = 0
        else:
            i[...] = i - valor
    

def accion3():
    print('Has elegido multiplicacion')
    
    valor = input('¿Qué valor aplicamos?')
    valor = float (valor)
    
    for i in np.nditer(imgArray, op_flags=['readwrite']):
        if ((i * valor) > 255):
            i[...] = 255
        else:
            i[...] = i * valor


def accion4():
    print('Has elegido division')
    
    valor = input('¿Qué valor aplicamos?')
    valor = float (valor)
    
    for i in np.nditer(imgArray, op_flags=['readwrite']):
        if ((i / valor) > 255):
            i[...] = 255
        else:
            i[...] = i / valor


def accion5():
    print('Has elegido gamma')
    
    valor = input('¿Qué valor aplicamos?')
    valor = float (valor)
    
    for i in np.nditer(imgArray, op_flags=['readwrite']):
        i[...] = 255*(i/255)**(1/valor)


def accion6():
    print('Has elegido inversa')
    
    for i in np.nditer(imgArray, op_flags=['readwrite']):
        i[...] = 255 - i 


def accion7():
    print('Has elegido ecualizacion')
    
    valor = input('¿Qué valor aplicamos?')
    valor = float (valor)
    
    for i in np.nditer(imgArray, op_flags=['readwrite']):
        if ((i + valor) > 255):
            i[...] = 255
        else:
            i[...] = i + valor

def salir():
    print('Saliendo')
    
if __name__ == '__main__':
    menu_principal()

# Colores en el histograma
color = ('b', 'g', 'r')

# Calculo del histograma modificado
for i, col in enumerate(color):
    modif = cv2.calcHist([imgArray], [i], None, [256], [0, 256])
    plt.plot(modif, color=col)
    plt.xlim([0, 256])

# Muestra la imagen modificada y su histogramaz
cv2.imshow('Imagen modificada', imgArray)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
