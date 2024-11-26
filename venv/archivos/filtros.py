import cv2

def erosión(mask):
  #Proceso de erosion:

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    eroded = cv2.erode(mask,kernel,iterations=2)
    filtrada= cv2.medianBlur(eroded, 5) #filtro mediana
    kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT,(15,5))

    dilated = cv2.dilate(filtrada,kernel2,iterations=2)

    return dilated

def gris(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)