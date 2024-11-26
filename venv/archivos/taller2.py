import cv2
import numpy as np

imagen = cv2.imread('imagenes/taller2.png')
cv2.imshow("Original",imagen)
cv2.waitKey(0)

LimiteInferior = np.array([15,200,120],np.uint8)
LimiteSuperior = np.array([28,255,255],np.uint8)

frameHSV = cv2.cvtColor(imagen,cv2.COLOR_BGR2HSV)
cv2.imshow('HSV',frameHSV)
cv2.waitKey(0)

mask = cv2.inRange(frameHSV,LimiteInferior,LimiteSuperior)
cv2.imshow('Amarillo', mask)
cv2.waitKey(0)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
eroded = cv2.erode(mask,kernel,iterations=2)
filtrada= cv2.medianBlur(eroded, 5) #filtro mediana

cv2.imshow('Rombos', filtrada)
cv2.waitKey(0)

xs = []
ys = []


contornos, y = cv2.findContours(filtrada, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for c in contornos:
    area = cv2.contourArea(c)
    if area>1:
        x,y,w,h = cv2.boundingRect(c) 
        cv2.rectangle(imagen, (x, y), (x+w, y+h),(0,0,255), 2) 
        #cv2.drawContours(frame, contornos, -1, (0,0,255), 3)
        cv2.circle(imagen, (int(x+w/2), int(y+h/2)), 2,(0,255,255), 3)
        xs = xs+[int(x+w/2)]
        ys = ys+[int(y+h/2)]
        cv2.imshow("Final", imagen)
        cv2.waitKey(0)

color = (0, 0, 255)

imagen = cv2.arrowedLine(imagen, (xs[0], ys[0]), (xs[1], ys[1]), color, 3)
cv2.imshow('flecha', imagen)
cv2.waitKey(0)






