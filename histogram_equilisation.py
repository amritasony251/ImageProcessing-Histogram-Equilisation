import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image
import math

img = cv2.imread("img6.bmp")
width, height, bit = np.shape(img)
x = np.linspace(0,255,256)

hist = [0]*256
p = [0]*256

size = width*height
for i in range(0, width):
   for j in range(0, height) :
      temp = img[i][j][0]
      hist[temp] = hist[temp] + 1      

hist_cumm = [0]*256      
for l in range(0, 256):
    hist_cumm[l] = float(hist[l])/float(size)  
    
for i in range(1, 256):
   hist_cumm[i] = float(hist_cumm[i]) + float(hist_cumm[i-1])   
   hist_cumm[i-1] = float(hist_cumm[i-1])*255.0
hist_cumm[i] = float(hist_cumm[i])*255.0        

for j in range(0, width):
  for i in range(0, height):
     a = img[i][j]
     img[i][j] = round(hist_cumm[a[0]])
     
cv2.imshow("image", img)
cv2.waitKey(0)     
      
