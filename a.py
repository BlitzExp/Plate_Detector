import cv2
import numpy as np
import easyocr


img = cv2.imread('C:/Users/jsnaj/Desktop/TEC/Semestre4/SemanaTEC/detector_de_placas/placa_q.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

euler = np.euler_gamma

Gauss_filter = np.array([[np.power(euler, -4), np.power(euler, -2),  np.power(euler, -4)],
                      [np.power(euler, -2), 1, np.power(euler, -2)],
                      [np.power(euler, -4), np.power(euler, -2),  np.power(euler, - 4)]]) / (4/np.pi) 

resultado_gauss = cv2.filter2D(img, -1, Gauss_filter)

lower_black = np.array([0, 0, 0])
upper_black = np.array([180, 255, 5])

black_mask = cv2.inRange(hsv, lower_black, upper_black)
resultado = cv2.bitwise_and(resultado_gauss,resultado_gauss, mask=black_mask)

kernel = np.ones((1, 1), np.uint8) 
eroded = cv2.erode(resultado, kernel)

# ksize 
ksize = (8, 8) 
  
# Using cv2.blur() method  
image = cv2.blur(resultado, ksize) 

t_lower = 100 
t_upper = 150
aperture_size = 3
edge = cv2.Canny(image, t_lower, t_upper, apertureSize=aperture_size)

# lector = easyocr.Reader(['es','en'])
# print(lector.readtext(resultado))


cv2.imshow("black", resultado)
cv2.imshow("Gauss lil wigga", resultado_gauss)
cv2.imshow('edge', edge)
cv2.imshow("Erode", eroded)
cv2.waitKey(0)
cv2.destroyAllWindows()