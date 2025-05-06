import cv2
import numpy as np
import pytesseract

#Configure tesseract
#pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


#Return an image with an applied mask using the lower and upper values
#along with the original image
def maskApplication(lower, upper, image):
    mask = cv2.inRange(image, lower, upper)
    return cv2.bitwise_and(image, image, mask=mask)    

#returns a blurred version of the image using the kernel that the user assigns
def Gauss_Blur(image, GaussianKernel):
    return (cv2.GaussianBlur(image,GaussianKernel,0))

img = cv2.imread('placa_2.jpg')
#img = cv2.resize(img, (894, 451)) 
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imagen2 = Gauss_Blur(gris,(3,3))

resultado = maskApplication(0,150,imagen2)
resultado = maskApplication(0,70,resultado)


resultado = Gauss_Blur(resultado,(7,7))
resultado = Gauss_Blur(resultado,(3,3))

t_lower = 50
t_upper = 150
edge = cv2.Canny(resultado, t_lower, t_upper, L2gradient = True)

resultado = Gauss_Blur(resultado,(9,9))

text = pytesseract.image_to_string(resultado, config='--psm 4 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
print("Texto:", text.strip())

cv2.imshow('edge', edge)
cv2.imshow("img2", imagen2)
cv2.waitKey(0)
cv2.destroyAllWindows()