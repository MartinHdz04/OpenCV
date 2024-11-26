## OPEN CV ####

import cv2
import numpy as np

#Instrucción para cargar una imagen
imagenbgr = cv2.imread('imagenes/rostro.jfif') 

#Mostramos la imagen
cv2.imshow('Imagen Cargada',imagenbgr)
cv2.waitKey(0) # Esta instrucción espera a que se oprima una tecla para continuar



### CONVERSIÓN A ESCALA DE GRISES ###########
gris= cv2.cvtColor(imagenbgr, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grises',gris)

cv2.waitKey(0) # Esta instrucción espera a que se oprima una tecla para continuar


## Información de la imagen
# Mostramos ancho, alto y canales

print("tamaño: {} bytes".format( imagenbgr.size))
print("alto: {} pixels".format(imagenbgr.shape[0]))
print("ancho: {} pixels".format(imagenbgr.shape[1]))
print("canales: {} ".format(imagenbgr.shape[2]))

#lO MISMO DE OTRA MANERA:
print("ancho:" + str(imagenbgr.shape[1]) + " pixels")

########## COLOR ####################
## Canales de color BGR
# En opencv el orden de los canales es BGR.
b = imagenbgr[:,:,0]
g = imagenbgr[:,:,1]
r = imagenbgr[:,:,2]

cv2.imshow('B',b) 
cv2.waitKey(0)

cv2.imshow('G',g) 
cv2.waitKey(0)

cv2.imshow('R',r) 
cv2.waitKey(0)
#cv2.destroyAllWindows()

###################################################

print("Pixel (0,0) => Roja {}, Verde {}, Azul {}".format(r,g,b))

 
# operaciones
suma=imagenbgr+100

print("Pixel (0,0) => Roja {}, Verde {}, Azul {}".format(r,g,b))
 
# Mostramos la imagen en la pantalla
cv2.imshow("suma", suma)
cv2.waitKey(0)

resta=imagenbgr-100


 
# Mostramos la imagen en la pantalla
cv2.imshow("resta", resta)
cv2.waitKey(0)

## Modificar colores por separado y "Reconstruir"

Bmod = b+2
Gmod = g-3
Rmod = r*2

Modificada=imagenbgr.copy()
Modificada[:,:,0]=Bmod
Modificada[:,:,1]=Gmod
Modificada[:,:,2]=Rmod


# Mostramos la imagen en la pantalla
cv2.imshow("Modificada", Modificada)
cv2.waitKey(0)

##############################################################################
#Filtros Derivativos (Bordes)

laplacianFilt=cv2.Laplacian(gris,ddepth=cv2.CV_8U)
cv2.imshow("Laplaciano", laplacianFilt)
cv2.waitKey(0)

sobelFilt = cv2.Sobel(gris,ddepth=cv2.CV_8U,dx=1,dy=1,ksize=3) 
cv2.imshow("Sobel", sobelFilt)
cv2.waitKey(0)

CannyFilter = cv2.Canny(gris, 100, 200)
cv2.imshow("Canny", sobelFilt)
cv2.waitKey(0)


##################### FILTROS ###############

filtrada= cv2.medianBlur(imagenbgr, 3) #filtro mediana
cv2.imshow('Mediana', filtrada)
cv2.waitKey(0)


blur = cv2.blur(imagenbgr,(15,15))
cv2.imshow('Media', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()



cv2.imwrite('Filtrada.png',blur) #Guardar imagen
cv2.waitKey(0)
#cv2.destroyAllWindows()






