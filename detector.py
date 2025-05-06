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

#returns a blurred version of the image using the kernel 
#that the user assigns
def Gauss_Blur(image, GaussianKernel):
    
    return (cv2.GaussianBlur(image,GaussianKernel,0))

#Image Declaration
img = cv2.imread('placa_2.jpg')

#Image resize to fit an standard (only for huge images 
#to fit into the screen)
#img = cv2.resize(img, (894, 451)) 

#Change the color palette to gray scale
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Blurring the image with a kernel (3x3)
imagen2 = Gauss_Blur(gris,(3,3))

#Applying black mask with values of 0,150
resultado = maskApplication(0,150,imagen2)

#Applying black mask with values of 0,70
resultado = maskApplication(0,70,resultado)

#Blurring the image with a kernel (7x7)
resultado = Gauss_Blur(resultado,(7,7))

#Blurring the image with a kernel (3x3)
resultado = Gauss_Blur(resultado,(3,3))

#Seeing how canny detects the edges of the letters
t_lower = 50
t_upper = 150
edge = cv2.Canny(resultado, t_lower, t_upper, L2gradient = True)

#Blurring the image with a kernel (9x9)
resultado = Gauss_Blur(resultado,(9,9))

#Using pytesseract to recognize the text in the image
text = pytesseract.image_to_string(resultado, 
    config='--psm 4 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

#Printing the detected text
print("Texto:", text.strip())


#Showing cv2 results
# cv2.imshow('edge', edge)
# cv2.imshow("img2", imagen2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()