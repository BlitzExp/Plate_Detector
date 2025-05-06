import cv2
import numpy as np
import pytesseract

#Configurar tesseract
#pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def mask_application(lower_black, upper_black, image):
    mascara_black = cv2.inRange(image, lower_black, upper_black)
    return cv2.bitwise_and(image, image, mask=mascara_black)    

img = cv2.imread('placa_3.jpg')
#img = cv2.resize(img, (894, 451)) 
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
imagen2 = cv2.GaussianBlur(gris, (3,3), 0)

resultado = mask_application(0,150,imagen2)
resultado = mask_application(0,70,resultado)


resultado = cv2.GaussianBlur(resultado, (7,7), 0)
resultado = cv2.GaussianBlur(resultado, (3,3), 0)

t_lower = 50
t_upper = 150
edge = cv2.Canny(resultado, t_lower, t_upper, L2gradient = True)

resultado = cv2.GaussianBlur(resultado, (9,9), 0)

text = pytesseract.image_to_string(resultado, config='--psm 4 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
print("Texto:", text.strip())

cv2.imshow('edge', edge)
cv2.imshow("img2", imagen2)
cv2.waitKey(0)
cv2.destroyAllWindows()