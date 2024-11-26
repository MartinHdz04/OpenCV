import cv2
import numpy as np

imagen = cv2.imread('imagenes/bottle.PNG')

limiteInferior = np.array([100,100,20], np.uint8)
limiteSuperior = np.array([125,255,255], np.uint8)


frameHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

mask = cv2.inRange(frameHSV, limiteInferior, limiteSuperior)

contornos , y = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(imagen, contornos, -1, (0,255,0), 3)


