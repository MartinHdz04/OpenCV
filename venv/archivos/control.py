import cv2
import numpy as np
import math


def imageprocess(mask):
  #Proceso de erosion:

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    eroded = cv2.erode(mask,kernel,iterations=2)
    filtrada= cv2.medianBlur(eroded, 5) #filtro mediana
    kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT,(15,5))

    dilated = cv2.dilate(filtrada,kernel2,iterations=2)

    return dilated

def enmascarar (LimiteInferior, LimiteSuperior, frame):
   frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
   mask = cv2.inRange(frameHSV,LimiteInferior,LimiteSuperior)
   return imageprocess(mask)

    
def consigue_extremos(frameMasked,x,y,w,h):
    # LimiteInferior = np.array([100,100,20],np.uint8)
    # LimiteSuperior = np.array([125,255,255],np.uint8)
    # frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # mask = cv2.inRange(frameHSV,LimiteInferior,LimiteSuperior)
    # procesada = imageprocess(mask)




    sumaX=0
    sumaY=0
    sumaX2=0
    sumaY2=0
    contador=0
    contador2 = 0
    promedioX =0
    promedioY =0
    promedioX2 =0
    promedioY2 =0

    puntoIzq:tuple
    puntoDer:tuple
    
    for i in range(x,int(x+w*0.1)):
       for j in range(y,y+h):
          if frameMasked[j,i]==255:
             sumaX+=i
             sumaY+=j
             contador+=1

    for i in range(int(x+w*0.9),int(x+w)):
       for j in range(y,y+h):
          if frameMasked[j,i]==255:
             sumaX2+=i
             sumaY2+=j
             contador2+=1

    if contador!=0:
        promedioX=int(sumaX/contador)
        promedioY=int(sumaY/contador)
        puntoIzq = (promedioX, promedioY)
        cv2.circle(frame, (promedioX, promedioY), 2,(0,255,255), 3)
    
    if contador2!=0:
        promedioX2=int(sumaX2/contador2)
        promedioY2=int(sumaY2/contador2)
        puntoDer = (promedioX2, promedioY2)
        cv2.circle(frame, (promedioX2, promedioY2), 2,(0,255,255), 3)
    
    return frame, puntoIzq, puntoDer

def inclinacion(p1:tuple, p2:tuple, pMedio:tuple, frame):
   if (p1.count == 0) or (p2.count == 0): 
      return frame
   
   pendiente = (p2[1] - p1[1]) / (p2[0]-p1[0])
   angulo = math.atan(pendiente)
   cv2.line(frame,p1,p2,(0,255,255), 3)
   cv2.putText(frame,str(angulo), pMedio, cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, 4)
   return frame

LimiteInferior = np.array([100,100,20],np.uint8)
LimiteSuperior = np.array([125,255,255],np.uint8)


captura = cv2.VideoCapture(0)  #El cero es el número de la cámara conectada al equipo
while (captura.isOpened()):
  ret, frame = captura.read()
  if ret==True:
    procesada = enmascarar(LimiteInferior, LimiteSuperior, frame)
    contornos, y = cv2.findContours(procesada, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contornos:
       area = cv2.contourArea(c)
       if area>10000:
        x,y,w,h = cv2.boundingRect(c) 
        cv2.rectangle(frame, (x, y), (x+w, y+h),(0,0,255), 2) 
        #cv2.drawContours(frame, contornos, -1, (0,0,255), 3)
        pMedio = (int(x+w/2), int(y+h/2))
        cv2.circle(frame, pMedio, 2,(0,255,255), 3)
        frame, pIzq, pDer = consigue_extremos(procesada,x,y,w,h)
        frame = inclinacion(pIzq, pDer, pMedio, frame)
        cv2.imshow('video', frame)  
    if cv2.waitKey(1) & 0xFF == ord('s'):
      break
  else: break 
captura.release()
cv2.destroyAllWindows()






