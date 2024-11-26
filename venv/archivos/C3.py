import cv2
import numpy as np

imagen = cv2.imread('imagenes/rostro.jfif') 



### CONVERSIÓN A ESCALA DE GRISES ###########
gris= cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)


#######   Umbralización - Si están en un rango passan a 255  o 0
val, binarizada1 = cv2.threshold(gris,130,255,cv2.THRESH_BINARY) #Cuando el pixel sea mayor a 130 se asignará 255
print("el umbral empleado fue:",val)

cv2.imshow('Binarizada',binarizada1)
cv2.waitKey(0)
cv2.destroyAllWindows()

#############################################
val, binarizada2 = cv2.threshold(gris,2,255,cv2.THRESH_OTSU) #asigna automáticamente el umbral
print("el umbral empleado POR otsu fue:",val)


cv2.imshow('Binarizada_Otsu',binarizada2)
cv2.waitKey(0)
cv2.destroyAllWindows()



val, binarizada = cv2.threshold(gris,130,255,cv2.THRESH_BINARY) #Cuando el pixel sea mayor a 130 se asignará 255
print("el umbral empleado fue:",val)
cv2.imshow('Binarizada',binarizada)
cv2.waitKey(0)


######################## MORFOLOGÍA ##################
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))

#Otras opciones:
#cv2.MORPH_RECT,(5,5)
#cv2.MORPH_ELLIPSE,(5,5)
#cv2.MORPH_CROSS,(5,5)

eroded = cv2.erode(binarizada,kernel)
cv2.imshow("Eroded Image",eroded)
cv2.waitKey(0)


dilated = cv2.dilate(binarizada,kernel)
cv2.imshow("Dilated Image",dilated)
cv2.waitKey(0)


invertida=cv2.bitwise_not(eroded)
cv2.imshow("Invertida",invertida)
cv2.waitKey(0)

opening = cv2.morphologyEx(binarizada, cv2.MORPH_OPEN, kernel)
cv2.imshow("opening",opening)
cv2.waitKey(0)

closing = cv2.morphologyEx(binarizada, cv2.MORPH_CLOSE, kernel)
cv2.imshow("closing",closing)
cv2.waitKey(0)





##################################
############ contornos ###########
##################################

contornos,hierarchy1 = cv2.findContours(invertida, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(imagen, contornos, -1, (0,255,0), 3)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(imagen,"Contornos",(400,400),font,0.75, (255,0,0),2,cv2.LINE_AA)
cv2.imshow('imagen',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()





### Video:

captura = cv2.VideoCapture(0)  #El cero es el número de la cámara conectada al equipo
while (captura.isOpened()):
  ret, imagen = captura.read()
  if ret == True:  ## Cuando si se está capturando video
    cv2.imshow('video', imagen)
    if cv2.waitKey(1) & 0xFF == ord('s'):
      break
  else: break
captura.release()
cv2.destroyAllWindows()


