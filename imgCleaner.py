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

if "--help" in argv or "-h" in argv:
    print("imgCleaner.py [image path] [parameters]")
    print("\t-e\tset black precision (eg: if set to 0, pixel should be [0, 0, 0] in RGB to be kept)")
    print("\t-s\tname of the output file, if not specified no file will be saved")
    print("--nshow\t\tdon't show the output")
    print("--help\t-h\tshow this help")
    exit(0)

if len(argv)>1:
    filename = argv[1]
else:
    print("Please specify a filename")
    exit(0)

params = {"-e": 150, "-s": None, "--nshow": False}

i=2
while i<len(argv):
    if argv[i] == "--nshow":
        params["--nshow"] = True
    elif argv[i]=="-e" and i<len(argv)-1:
        params[argv[i]] = int(argv[i+1])
        i+=1
    elif i<len(argv)-1:
        params[argv[i]] = argv[i+1]
        i+=1
    i+=1

img= Image.open(filename)
ar = np.array(img)
newImg = np.array(ar)

nbpix = 0
for i in range(np.size(ar, 0)):
    for j in range(np.size(ar, 1)):
        rms = moyPixel(ar[i,j])
        if rms>params["-e"]:
            newImg[i,j] = [255, 255, 255]
            nbpix+=1

print("Nombre de pixel modifié : {}".format(nbpix))

if not params["--nshow"]:
    plt.subplot(121)
    plt.imshow(newImg)
    plt.title("New")
    plt.subplot(122)
    plt.imshow(img)
    plt.title("Old")
    plt.show()

if params["-s"]!=None:
    plt.imsave(params["-s"], newImg)