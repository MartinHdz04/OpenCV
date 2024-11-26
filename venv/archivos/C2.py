
import cv2

#Instrucción para cargar una imagen
imagen = cv2.imread('imagenes/rostro.jfif') 
imagen2=imagen.copy()

#Mostramos la imagen
cv2.imshow('Imagen Cargada',imagen)


## Mediante las funciones de Open Cv es posible hacer algunos dibujos básicos
# sobre las imágenes, esto será util en aplicaciones posteriores:

alto, ancho, _ = imagen.shape
color = [0, 0, 255]
grosor = 2

#la sintaxis es la siguiente:
#imagen = cv2.line(imagen, puntoInicial, puntoFinal, color, grosor)

imagen = cv2.line(imagen, (0, 0), (ancho, alto), color, grosor)
cv2.imshow('Linea', imagen)
cv2.waitKey(0)


cuadricula = 80

for x in range(0, ancho, cuadricula):
    imagen = cv2.line(imagen, (x, 0), (x, alto), color, grosor)
for y in range(0, alto, cuadricula):
    imagen = cv2.line(imagen, (0, y), (ancho, y), color, grosor)

cv2.imshow('cuadricula', imagen)
cv2.waitKey(0)

## RECTÁNGULOS

color = (0, 0, 255)
grosor = 2
RectanguloXInicial, RectanguloXFinal = 300, 550
RectanguloYInicial, RectanguloYFinal = 20, 220


imagen = cv2.arrowedLine(imagen, (200, 100), (300, 150), color, grosor)
cv2.imshow('flecha', imagen)
cv2.waitKey(0)
cv2.rectangle(imagen2, (RectanguloXInicial, RectanguloYInicial), (RectanguloXFinal, RectanguloYFinal),color, grosor)

cv2.imshow('cuadro', imagen2)
cv2.waitKey(0)

## CIRCULOS 

#SINTAXIS

# cv2.circle(imagen, (centro_x, centro_y), radio,color, grosor)

imagen = cv2.imread('imagenes/rostro.jfif') 

alto, ancho, canales = imagen.shape
color = (255, 0, 255)
incremento_radio = 80
grosor = 20

centro_x = int(ancho/2)
centro_y = int(alto/2)

for radio in range(0, int(alto/2), incremento_radio):
    cv2.circle(imagen, (centro_x, centro_y), radio,color, grosor)

cv2.imshow('Circulos', imagen)
cv2.waitKey(0)

## TEXTOS
# cv2.putText(img, "Texto", posicionDeInicio, fuente, escala, color, grosor)
# Se puede escribir en varias fuentes. 

color = (0, 255, 0)
grosor = 4
fuente = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
escala = 2
# Tarea investighar otras fuentes

cv2.putText(imagen, "Mi Texto", (100, 75), fuente, escala, color, grosor)

cv2.imshow('Texto', imagen)
cv2.waitKey(0)