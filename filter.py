import cv2
import numpy

def read_image(path):
    return cv2.imread(path, cv2.IMREAD_UNCHANGED)

def export_image(img, path):
    cv2.imwrite(path, img)

def gaussian_blur(path,x):
    image = read_image(path)
    dst = cv2.GaussianBlur(image, (x, x), cv2.BORDER_DEFAULT)
    return dst

def laplacian(filepathname, ksize=3):
    v = cv2.imread(filepathname)
    s = cv2.cvtColor(v, cv2.COLOR_BGR2GRAY)
    s = cv2.Laplacian(s, cv2.CV_16S, ksize)
    s = cv2.convertScaleAbs(s)
    return s