import cv2 as cv
import numpy as np
import os

file = 'Dewei.jpg'
img = cv.imread(file)

os.system("cls")

if(len(img.shape)<3):
    waifu = cv.imread('waifu.jpg')
    cv.imshow("I don't accept Greyscale images.", waifu)
    cv.waitKey(0)
    cv.destroyAllWindows()
elif(len(img.shape)==3):
    cv.imshow("Dewei and Delayp", img)
    cv.waitKey(0)
    cv.destroyAllWindows()
    print("Specificy your desired Pixel:")
    X = int(input("X:"))
    Y = int(input("Y:")) 
    Channel = int(input("Color Channels \n0 - BLUE\n1 - GREEN\n2 - RED\nChannel:"))
    print(img.item(X, Y, Channel))
    print("Modify Image Pixel Value")
    blue = input("Blue Channel Value (0-255):")
    green = input("Green Channel Value (0-255):")
    red = input("Red Channel Value (0-255):")
    print("BEFORE: ", img[X, Y])
    img.itemset((X, Y, 0), blue)
    img.itemset((X, Y, 1), green)
    img.itemset((X, Y, 2), red)
    print("AFTER: ", img[X, Y])
    InDime = img.shape
    fixDime = (720, 700, 3)
    if(InDime[0]>=fixDime[0] and InDime[1]>=fixDime[1]):
        print("Image is within boundary")
    else:
        print("Image is out of boundary")
        size = img.size
        fixSize = 2764799
    if(size>fixSize):
        print("The set pixel is lower than Image total pixel count.")
    else:
        print("The set pixel is higher than Image total pixel count.")
    print("Loaded Image data type: ", img.dtype)