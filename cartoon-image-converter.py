import cv2 as cv2
import numpy as np 
import os 
directory = os.getcwd()
num_down = 2
num_bilateral = 17
image = cv2.imread(".\\beagledog.jpg")
cv2.imshow("Image",image)
cv2.waitKey(15)
cv2.destroyAllWindows()
img_color= image
for _ in range(num_down):
  img_color=cv2.pyrDown(img_color)
for _ in range(num_bilateral):
  img_color = cv2.bilateralFilter(img_color,d=9,sigmaColor=19,sigmaSpace=17)
for _ in range(num_down):
  img_color = cv2.pyrUp(img_color)
img_gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
img_blur = cv2.medianBlur(img_gray,15)
img_edge = cv2.adaptiveThreshold(img_blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,blockSize=9,C=2)
img_edge = cv2.cvtColor(img_edge,cv2.COLOR_GRAY2RGB)
img_cartoon  =cv2.bitwise_and(img_color,img_edge)
cv2.imshow("Cartoon",img_cartoon)
cv2.waitKey(50)
cv2.destroyAllWindows()
image_name = "cartoon_image.jpg"
cv2.imwrite(image_name,img_cartoon)
print(os.listdir(directory))
