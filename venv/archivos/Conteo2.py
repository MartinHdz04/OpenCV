import cv2
imagen = cv2.imread('imagenes/Moneda.png')
grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gris",grises)
cv2.waitKey(0)


_,binarizada =  cv2.threshold(grises, 140, 255, cv2.THRESH_BINARY_INV)


cv2.imshow('Umbralizada', binarizada)
cv2.waitKey(0)


kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
dilated = cv2.dilate(binarizada,kernel)
cv2.imshow("Dilated Image",dilated)
cv2.waitKey(0)



contornos,_ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print('Contornos: ', len(contornos))
font = cv2.FONT_HERSHEY_SIMPLEX

mensaje = 'Numero de Objetos:' + str(len(contornos))
cv2.putText(imagen,mensaje,(10,50),font,0.75,
    (255,0,0),2,cv2.LINE_AA)
for c in contornos:
  cv2.drawContours(imagen, [c], 0, (255,0,0),2)
  cv2.imshow('Imagen', imagen)
  cv2.waitKey(0)
    
cv2.destroyAllWindows()
