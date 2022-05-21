import cv2
from utils import readb64

def gaussian_blur(path, x):
    image = readb64(path)
    dst = cv2.GaussianBlur(image, (x, x), cv2.BORDER_DEFAULT)
    return dst


def laplacian(filepathname, ksize=3):
    v = readb64(filepathname)
    s = cv2.cvtColor(v, cv2.COLOR_BGR2GRAY)
    s = cv2.Laplacian(s, cv2.CV_16S, ksize)
    s = cv2.convertScaleAbs(s)
    return s

def sobelx(filepathname, ksize=5):
    v = readb64(filepathname)
    gray = cv2.cvtColor(v, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(gray,(3,3),0)
    sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)  # x
    sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)  # y
    return sobelx

def sobely(filepathname, ksize=5):
    v = readb64(filepathname)
    gray = cv2.cvtColor(v, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(gray,(3,3),0)
    sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)  # x
    sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)  # y
    return sobely