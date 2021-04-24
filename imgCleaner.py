from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

def RMSPixel(pixel):
    summ = 0
    for val in pixel:
        summ += val*val
    return sqrt(summ/3)
def moyPixel(pixel):
    summ = 0
    for val in pixel:
        summ += val
    return summ/3

img= Image.open("/home/matt/OneDrivePerso/graph.jpg")
ar = np.array(img)
newImg = np.array(ar)
epsilon = 150

nbpix = 0
for i in range(np.size(ar, 0)):
    for j in range(np.size(ar, 1)):
        rms = moyPixel(ar[i,j])
        if rms>epsilon:
            newImg[i,j] = [255, 255, 255]
            nbpix+=1

print(nbpix)
plt.subplot(121)
plt.imshow(newImg)
plt.subplot(122)
plt.imshow(img)
plt.show()