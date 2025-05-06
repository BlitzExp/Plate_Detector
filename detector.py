import cv2
import numpy as np
import pytesseract

#Configurar tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


img = cv2.imread('placa_3.jpg')
img = cv2.resize(img, (894, 451)) 
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
imagen2 = cv2.GaussianBlur(gris, (3,3), 0)

lower_black = 0
upper_black = 150

mascara_black = cv2.inRange(gris, lower_black, upper_black)
resultado = cv2.bitwise_and(imagen2, imagen2, mask=mascara_black)

lower_black = 0
upper_black = 50

mascara_black = cv2.inRange(gris, lower_black, upper_black)
resultado = cv2.bitwise_and(imagen2, imagen2, mask=mascara_black)

resultado = cv2.GaussianBlur(resultado, (7,7), 0)
resultado = cv2.GaussianBlur(resultado, (3,3), 0)

t_lower = 50
t_upper = 150
edge = cv2.Canny(resultado, t_lower, t_upper, L2gradient = True)

resultado = cv2.GaussianBlur(resultado, (9,9), 0)

text = pytesseract.image_to_string(resultado, config='--psm 4 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
print("🔍 Texto detectado:", text.strip())

cv2.imshow('edge', edge)
cv2.imshow("img2", imagen2)
cv2.waitKey(0)
cv2.destroyAllWindows()