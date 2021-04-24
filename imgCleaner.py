from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
from sys import argv

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

if len(argv)>1:
    filename = argv[1]
else:
    print("Please specify a filename")
    exit(0)

if len(argv)>2:
    epsilon = int(argv[2])
else:
    epsilon = 150

img= Image.open(filename)
ar = np.array(img)
newImg = np.array(ar)

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
plt.title("New")
plt.subplot(122)
plt.imshow(img)
plt.title("Old")
plt.show()