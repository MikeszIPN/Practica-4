#Librerias
from PIL import Image
import numpy as np
import math

#Lectura de imagen
im_path='Pics/paris.jpeg'

#Arreglo de n*m (de la imagen)
image=np.array(Image.open(im_path))

#Funcion de interpolacion bilineal (imagen, ancho, alto)
def BiLinear_interpolation(img,dstH,dstW):
    
    #Crea el arreglo con las dimensiones dadas
    scrH,scrW,_=img.shape 
    img=np.pad(img,((0,1),(0,1),(0,0)),'constant')
    
    #Llenar la matriz de 0's
    retimg=np.zeros((dstH,dstW,3),dtype=np.uint8)
    
    #Recorrido en ancho y alto 
    for i in range(dstH):
        for j in range(dstW):
            
            #Interpolacion en X
            scrx=(i+1)*(scrH/dstH)-1
            
            #Interpolacion en Y
            scry=(j+1)*(scrW/dstW)-1
            
            #Funcion piso
            x=math.floor(scrx)
            y=math.floor(scry)
            
            #Asignacion de los valores con funcion piso
            u=scrx-x
            v=scry-y
            
            #Llenar los valores de la nueva imagen redimensionada con el recorrido de for anidados
            retimg[i,j]=(1-u)*(1-v)*img[x,y]+u*(1-v)*img[x+1,y]+(1-u)*v*img[x,y+1]+u*v*img[x+1,y+1]
    return retimg

#Llamado de funcion al doble de tamaño
image2=BiLinear_interpolation(image,image.shape[0]*2,image.shape[1]*2)

#Conversion a imagen
image2=Image.fromarray(image2.astype('uint8')).convert('RGB')

#Guardar la imagen
image2.save('c:/Users/SZMik/OneDrive/Documentos/Mike/VisualStudio/Pics/BILINEAL.png')